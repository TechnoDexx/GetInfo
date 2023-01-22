#!/usr/bin/python3.10
import GetInfo as Gi
import sys
import subprocess as sp
# from GetInfo import Icon, Title
from GetInfo import *

icons = []
geticon = False


def main(argv):
    global geticon, icons
    sp.call("clear")
    try:
        _url = argv[1]

    except IndexError:
        print("Введите URL")
        exit(0)
    else:
        icons, geticon = Icon.get(argv[1])      # get_icon(argv[1])
        try:
            print("\n Url: {}".format(argv[1]))
            print("\n Title: {}".format(Title.get(argv[1])))  # get_title(argv[1])))
        except IndexError:
            exit(0)
        except UnboundLocalError:
            exit(0)
        print("\n Icon: {}".format(icons[0]))


if __name__ == '__main__':
    main(sys.argv)
