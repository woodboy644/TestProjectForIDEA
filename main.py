#coding: utf-8

import os, sys
from module import Hoge

# exit script
def ending():
	dummy = raw_input('Press Enter to Exit')
	sys.exit()

if __name__ == '__main__':
	hoge = Hoge.Hoge()
	hoge.printMsg("hogehoge")

	ending()
