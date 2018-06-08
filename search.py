#!/usr/bin/python2

import os
import commands
import webbrowser
se = raw_input("what you want to search.............")

webbrowser.open_new_tab('https://www.google.com/#q={0}'.format(se))

