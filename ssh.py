#!/usr/bin/python2

import os
import getpass
import signal
import commands

def mystop(x,y):
        print "\n Goodbye....."
        exit()

signal.signal(2 , mystop)

os.system("tput setaf 4")
print "\t\t\t\tWant to search !!"
print "\t\t\t\t................."

os.system("tput setaf 1")
print "\t\twait checking internet connectivity"

ss=commands.getstatusoutput("ping www.google.com")
if (ss[0]==0):
	print "good internet connectivity"
else:
	print "check your internet connection"

se = raw_input("what you want to search.............")

webbrowser.open_new_tab('https://www.google.com/#q={0}'.format(se))







