import colorama
from colorama import Fore, Style, Back
import platform
import sys
import os


class ScanOutput():

    def __init__(self):
        colorama.init()
        self.lastInLine = False
        self.terminal_size = self.__get_terminal_size()
        self.system = platform.system()


    def __get_terminal_size(self):
        try:
            columns = os.get_terminal_size().columns
        except Exception:
            columns = 100
        return columns


    def print_info(self, message):
        if self.system == "Windows":
            self.new_line(Fore.LIGHTYELLOW_EX + Style.NORMAL + "[*] {0}".format(message) + Style.RESET_ALL)
        else:
            self.new_line(Fore.LIGHTGREEN_EX + Style.NORMAL + "[*] {0}".format(message) + Style.RESET_ALL)


    def print_warning(self, message):
        self.new_line(Fore.LIGHTYELLOW_EX + '[!] {0}'.format(message) + Style.RESET_ALL)


    def print_error(self, message):
        self.new_line(Fore.RED + '[-] {0}'.format(message) + Style.RESET_ALL)


    def print_special(self, message):
        self.new_line(Fore.LIGHTMAGENTA_EX + '[*] {0}'.format(message) + Style.RESET_ALL)


    def print_lastLine(self, message):

        self.inLine(
            Fore.LIGHTYELLOW_EX + Back.CYAN + '[~] {0}'.format(message) + Back.RESET + Fore.RESET + Style.RESET_ALL)


    def print_info_green(self, message):
        self.new_line(Fore.GREEN + '[*] {0}'.format(message) + Style.RESET_ALL)


    def print_history(self, res, url):
        mes = ""
        history_res = res.history[0]
        mes += str(history_res.status) + " - " + Fore.LIGHTMAGENTA_EX + str(
            url) + Fore.GREEN + " => "
        mes += ScanOutput.get_status_color(res.status) + Fore.GREEN + " - " + Fore.LIGHTMAGENTA_EX + str(
            res.url) + Style.RESET_ALL
        self.print_info_green(mes)


    def inLine(self, string):
        self.erase()
        if len(string) > self.terminal_size:
            string = string[:self.terminal_size - 7] + "..." + Back.RESET + Fore.RESET
        sys.stdout.write(string)
        sys.stdout.flush()
        self.lastInLine = True


    def new_line(self, message):
        if self.lastInLine:
            self.erase()

        if self.system == 'Windows':
            sys.stdout.write(message)
            sys.stdout.flush()
            sys.stdout.write('\n')

        else:
            sys.stdout.write(message + '\n')

        sys.stdout.flush()
        self.lastInLine = False


    def erase(self):
        if self.system == 'Windows':
            sys.stdout.write(Style.RESET_ALL + '\r' + ' ' * (self.terminal_size - 2) + '\r')
            sys.stdout.flush()

        else:
            sys.stdout.write('\033[1K')
            sys.stdout.write('\033[0G')
            sys.stdout.flush()


    def print_banner(self):
        self.new_line(Fore.LIGHTMAGENTA_EX + r"""
        ___      ____________________ _______ 
        __ | /| / /_  ___/  ___/  __ `/_  __ \
        __ |/ |/ /_(__  )/ /__ / /_/ /_  / / /
        ____/|__/ /____/ \___/ \__,_/ /_/ /_/ 
        """ + Style.RESET_ALL)
        self.new_line(Fore.LIGHTYELLOW_EX + " " * 10+ "Blog: <https://www.wzsite.cn>" + Style.RESET_ALL)
        self.new_line(Fore.LIGHTYELLOW_EX + " " * 10 + "Email: <testzero.wz@gmail.com>\n\n" + Style.RESET_ALL)


    @staticmethod
    def get_status_color(status):
        if status == 200:
            color = Fore.LIGHTGREEN_EX
        elif status == 404:
            color = Fore.RED
        elif status in [301, 302, 307]:
            color = Fore.LIGHTYELLOW_EX
        else:
            color = Fore.CYAN
        return color + str(status)


if __name__ == "__main__":
    pass
