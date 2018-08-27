import sys
import os
from wscan.lib.io.Argument import Argument
from wscan.lib.controller.Controller import Controller


if sys.version_info < (3, 5):
    sys.stdout.write("Requires Python 3.5 or higher ")
    sys.exit(1)


class wscan():

    def __init__(self):
        self.base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"wscan")
        self.args = Argument(self.base_path)
        self.control = Controller(args=self.args)
        self.control.start()


if __name__ == "__main__":
    wscan()
