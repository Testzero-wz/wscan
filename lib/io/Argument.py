import argparse


class Argument():

    def __init__(self, base_path=None):
        parser = argparse.ArgumentParser(prog="wscan.py",
                                         usage="wscan.py [-u URL] [-f] [-m] [Extend options]",
                                         description="""
         A Fast & Simple web site scanner. 
        """, epilog=" Example: wscan.py -u \"http://www.example.com/\" -f -m -v")

        parser.add_argument('-u', dest='url', action="store", required=True,
                            help='Target URL')

        parser.add_argument('-f', dest='fuzz', action="store_true",
                            help='\nFuzz target url with dictionary. ', default=False)

        parser.add_argument('-m', dest='map', action="store_true",
                            help='\nCrawl all URL on the target to get a map. ',
                            default=False)

        parser.add_argument('-max', dest="max_num", type=int,
                            help="""\nMax num of co-routine. [Default: 20]""", default=20)

        parser.add_argument('-b', dest="base",
                            help="""\nBase URL of fuzz e.g -b /cms/app [Default: /]""", default="/")

        parser.add_argument('-e', dest="extend",
                            help="""\nSuffix name used in fuzz [Default: php]""", default="php")


        parser.add_argument("--no-img", dest="no_img", action="store_true",
                            help="\nDon't crawl image url when mapping target", default=False)

        parser.add_argument("--no-re", dest="no_re", action="store_true",
                            help="\nDon't redirect when requesting", default=False)

        detail_group = parser.add_mutually_exclusive_group()

        detail_group.add_argument('-v', dest="v", action="store_true",
                                  help="\nShow more detail", default=False)

        detail_group.add_argument('-vv', dest="vv", action="store_true",
                                  help="\nShow the most detailed details", default=False)

        self.args = parser.parse_args()
        self.args.base_path = base_path


    def get_args(self):
        return self.args


if __name__ == "__main__":
    Argument()
