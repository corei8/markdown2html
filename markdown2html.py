# Author: https://github.com/corei8
# Date: 02.07.20

import sys
import os

user_input = input("Enter the path of your file: ")
assert os.path.exists(os.path.dirname(os.path.abspath(user_input))), 'No file found at ' + str(user_input)
f = open(user_input,'r+')
for line in f:
    if line[0] == '#': tago, tagc = '<h1>', '</h1>'
    else: tago, tagc = '<p>', '</p>'
    print(tago + line + tagc)
f.close()
