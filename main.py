#coding: utf-8

import sys
from module import hoge
from module import Greeting

# exit script
def ending():
    dummy = raw_input('Press Enter to Exit')
    print 'exit script ...'
    sys.exit()

if __name__ == '__main__':
    insHoge = hoge.Hoge()
    insHoge.printMsg("Hello world")

    print '-' * 30

    greeting = Greeting.Greeting()
    greeting.howAreYou()

    print '-' * 30

    ending()
