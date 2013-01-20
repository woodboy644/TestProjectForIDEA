#coding: utf-8

import os, sys
from module import Hoge
from module import Greeting

# exit script
def ending():
	dummy = raw_input('Press Enter to Exit')
	sys.exit()

if __name__ == '__main__':
	hoge = Hoge.Hoge()
	hoge.printMsg("hogehoge")

	print '-' * 30

	greeting = Greeting.Greeting()
	greeting.howAreYou()

	ending()
