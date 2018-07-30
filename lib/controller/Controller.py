import asyncio
import re
import aiohttp
import os, sys
from bs4 import BeautifulSoup
from lib.tree.DirTree import DirTree
import time
import random
from colorama import Fore, Style
from lib.io.ColorOutput import ScanOutput
from lib.exception.ScanException import *


class Controller(object):

    header = {
        'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8',
        'Accept-Language': 'Zh-CN, zh;q=0.8, en-gb;q=0.8, en-us;q=0.8',
        'Accept-Encoding': 'identity',
        'Keep-Alive': '300',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }


    def __init__(self, args=None):

        self.args = args
        self.output = ScanOutput()
        self.detail = self.args.v
        self.more_detail = self.args.vv
        self.init_url = self.args.url

        self.protocol, self.host, self.port, self.path, self.query = self.__parse_url(self.init_url)
        self.port = 80 if self.port == "" else self.port
        self.prefix = self.protocol + "://" + self.host + ("" if self.port == 80 else (":" + str(self.port)))
        self.output.print_info(self.prefix)
        self.fuzz_prefix = self.prefix + self.args.base

        self.queue = asyncio.Queue()
        self.tree = DirTree()
        self.urls = []
        self.time_out_times = 0
        self.map_finish = False

        self.__init_ua()
        self.loop = asyncio.get_event_loop()
        self.session = aiohttp.ClientSession(loop=self.loop)

        self.__init_fuzz_list(os.path.join(self.args.base_path, "fuzz", "dirList.txt"))
        self.max_threads = self.args.max_num
        self.alive_routine = self.args.max_num



        self.output.print_banner()


    def __parse_url(self, _url):
        """
        Use regex parse url into (Protocol, Domain, Port, Path, Query)
        :param _url:
        :return: <tuple> (Protocol, Domain, Port, Path, Query)
        """
        url = _url[:-1] if _url[-1] == "/" else _url
        try:
            protocol, domain, port, path, query = re.findall("(.*?)://([^/:]+):?([0-9]+)?(/?[^\?]*)?(\??.*)?$", url)[0]
        except Exception:
            self.output.print_error("Parameter url format error. e.g http://www.example.com")
            sys.exit(1)
        return protocol, domain, port, path if path != "" else "/", query


    def __init_ua(self):
        """
        Read UA from file
        """
        path = os.path.join(self.args.base_path, "fuzz", "user_agent.txt")
        with open(path, "r") as file:
            self.UA = list(map(lambda x: x[:-1], file.readlines()))


    def __init__crawler_list(self):
        """
        Initial first page & collete urls and put it into Tree.
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__page_url_collect(self.init_url, init_page_flag=True))


    async def __page_url_collect(self, response=None, init_page_flag=False):
        """
        Parse the content, filter out urls.
        :param html: Content
        :param headers: Response header
        :param init_page_flag: Differentiate between init_first_page or fuzzing
        :return: None
        """

        if init_page_flag:
            url = self.__check_href(response)
            if url is None:
                return
            self.tree.add(url)
            node = self.tree.get_node(url)
            response = (await self.get_response(response))
            node.set_status(response.status)
            node.set_access(True)

        headers = response.headers

        if headers.get('content-type').find("text/html") == -1:
            return

        charset = re.findall("charset=(.*?)$", headers.get('content-type'))
        if len(charset) == 1:
            charset = charset[0]
        else:
            charset = None
        html = await response.read()
        self.__parse_results(html, charset=charset)
        for node in self.tree.enum_tree():
            if not node.is_access():
                node.set_access()
                self.queue.put_nowait(node.get_full_path())


    def __init_fuzz_list(self, url_list):
        """
        Initial fuzz list by reading urls from /fuzz/dirList.txt
        :param url_list: <str> file path | <list> fuzz urls list
        """
        if isinstance(url_list, str):
            dir_file = open(url_list)
            for dirs in dir_file.readlines():
                self.urls.append(dirs[:-1].replace("%EXT%", self.args.extend))
        elif isinstance(url_list, list):
            self.urls = url_list
        else:
            raise TypeError("Fuzz_list is required to be str or list , But a %s was given." % type(url_list))


    def __parse_results(self, html, charset=None):
        """
        Adding URLs collected from html to web Tree
        :param html: Html want to be parsed
        :param charset: html decode charset
        """
        try:
            soup = BeautifulSoup(html, 'html.parser', from_encoding=charset)
            href_list = soup.find_all('a')
            if not self.args.no_img:
                src_list = soup.find_all('img')
                src_list.extend(soup.find_all('script'))

        except Exception as e:
            raise e

        # Collect href of tag <a>
        for href in map(lambda tag: tag.get('href'), href_list):
            try:
                self.tree.add(self.__check_href(href))
            except Exception:
                pass

        # Collect image URLs
        if not self.args.no_img:
            for href in map(lambda tag: tag.get('src'), src_list):
                try:
                    self.tree.add(self.__check_href(href))
                except Exception:
                    pass


    def __check_href(self, href):
        """
        Check the URL whether belongs to host
        :param href: URL
        :return: URL belongs to host or None
        """
        # If relative path
        if href.find("/") == 0:
            return href

        # Standard url
        elif href.find(self.protocol + "://" + self.host) == 0:
            return self.__parse_url(href)[3]

        return None


    async def get_response(self, url, allow_redirects=True):
        headers = self.header.copy()
        headers['User-agent'] = random.choice(self.UA)
        return await self.session.get(url, timeout=8, allow_redirects=allow_redirects)


    async def co_routine(self):

        """
         Co-routine hang up flag
         In order to keep co-routine alive while queue is empty but other co-routines aren't
         finish is't task which may put urls into queue again.
        """
        hang_up = False

        while self.alive_routine:
            if not self.queue.empty():
                url = await self.queue.get()
                if hang_up:
                    self.alive_routine += 1
                    hang_up = False
            else:
                if not hang_up:
                    self.alive_routine -= 1
                    hang_up = True
                await asyncio.sleep(0.5)
                continue

            if not self.map_finish:
                full_url = self.prefix + url
            else:
                full_url = self.fuzz_prefix + url

            self.output.print_lastLine("Processing: %s" % url)
            try:

                res = await self.get_response(full_url, allow_redirects=(self.args.no_re is False))
                status = res.status

                # Log status

                # If redirect
                if len(res.history) != 0 and (status != 404 or self.more_detail):
                    self.output.print_history(res, url)

                # Log status which response code isn't 404
                elif status != 404:
                    self.output.print_info("{0} - {1}".format(status, Fore.GREEN + url + Style.RESET_ALL))

                """
                Try to get node from Tree.
                if doesn't raise a error, indicate that this url was collected by web crawler,
                then setting the response status code & access flag for  corresponding node
                """
                if status != 404:
                    self.tree.add(url)

                    try:
                        node = self.tree.get_node(url)
                        node.set_status(status)
                        node.set_access(True)

                    except KeyError:
                        pass
                    except Exception as e:
                        raise Exception(e)

                    if status == 200 and not self.map_finish:
                        await self.__page_url_collect(res)

            except aiohttp.client_exceptions.ClientError as e:
                if e.errno == 104:
                    if self.detail:
                        self.output.print_error("RST - :%s" % (
                                Fore.BLUE + url + Style.RESET_ALL))
                else:
                    if self.more_detail:
                        self.output.print_error("An unknown network error occurred when Requesting url:%s" % (
                                Fore.BLUE + url + Style.RESET_ALL))
                        self.output.print_error("Error:%s" % e)
            except asyncio.TimeoutError:
                if self.detail:
                    self.output.print_warning("OUT - %s" % url)
                self.time_out_times += 1

            except Exception as e:
                if self.more_detail:
                    self.output.print_error(
                        "An unknown error occurred when Requesting url:%s" % (Fore.BLUE + full_url + Style.RESET_ALL))
                    self.output.print_error("Error:%s" % e)

            finally:
                pass


    def __start_co_routine(self):
        self.alive_routine = self.max_threads
        tasks = [self.co_routine() for i in range(self.max_threads)]
        self.loop.run_until_complete(asyncio.wait(tasks))


    def __start(self):
        if self.args.map:
            self.output.print_info("Start Mapping...")
            self.__init__crawler_list()
            self.__start_co_routine()

        self.map_finish = True
        if self.args.fuzz:
            self.output.print_info("Start Fuzzing...")
            for url in self.urls:
                self.queue.put_nowait(("/" if url[0] != '/' else "") + url)
            self.__start_co_routine()


    def start(self):

        start = time.time()
        self.output.print_info("Start: %s" % time.strftime("%H:%M:%S"))

        try:
            self.__start()

        except KeyboardInterrupt:
            self.output.print_error("Aborted by user!")

        except Exception as e:
            self.output.print_error("Fatal error occurs!")
            self.output.print_error("Error: %s" % e)
            sys.exit(-1)

        if self.time_out_times >= 5:
            self.output.print_warning(
                "There are too many time out queries, \
                You can make it better by reducing the num of co-routine. ")

        self.output.print_info("End: %s" % time.strftime("%H:%M:%S"))
        self.output.new_line(Fore.LIGHTYELLOW_EX + "=" * (self.output.terminal_size) + Style.RESET_ALL)

        # Print tree
        self.output.new_line(Fore.LIGHTYELLOW_EX + "Web site map:" + Style.RESET_ALL)
        self.print_tree()
        self.output.new_line("\n" + Fore.LIGHTYELLOW_EX + "=" * (self.output.terminal_size) + Style.RESET_ALL)

        # Print cost
        self.output.print_info("Scan finished. Cost %.2f s." % (time.time() - start))


    def print_tree(self):
        """
        Print web site map
        """
        for node in self.tree.enum_tree():
            print(Fore.WHITE + " │   " * node.get_depth() + " +-- " + Style.RESET_ALL, end="")
            status = node.get_status()

            if status == 200:
                print(Fore.YELLOW + node.get_name() + Style.RESET_ALL, end=" ")

            elif status == 404:
                print(Fore.RED + node.get_name() + Style.RESET_ALL, end=" ")

            elif status in [301, 302, 307]:
                print(Fore.GREEN + node.get_name() + Style.RESET_ALL, end=" ")
            else:
                print(Fore.LIGHTMAGENTA_EX + node.get_name() + Style.RESET_ALL, end=" ")

            print(Fore.BLACK + str(status) + Style.RESET_ALL)


    def __del__(self):
        """
        Close session by accessing a protected member _connector
        Learn from StackOverflow
        """
        try:
            if not self.session.closed:
                if self.session._connector.close():
                    self.session._connector.close()
                self.session._connector = None
        except Exception:
            self.output.print_error("Session was not closed or didn't exit.")


if __name__ == '__main__':
    pass
