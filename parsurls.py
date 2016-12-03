#! /usr/bin/python

# Find all internet shortcut files in folder (Windows only).
# Write to a text file the filename and URL of each shortcut.

import os

# Set path to shortcut file(s)
P = os.getcwd()
# Get filenames of all URL shortcut files
ulist = [s for s in os.listdir(P) if s.endswith('.url') or s.endswith('.URL')]

# Iterate thru list
# open url file, read it
# Find "URL=" and read to end of line
# Write that to text file along with name of shortcut it came from

nurls = []  # List of tuples of filenames and urls
    
for u in ulist:
    try:
        with open(u, 'r') as fo:
            fr = fo.read()
            i = fr.find('URL=') + 4
            j = fr.find('\n', i)
            url_str = fr[i:j]
            nurls.append((u[:-4], url_str))
    except Exception as err:
        print('Can not parse ' + u)
        continue
        
with open('readinglinks.txt', 'a') as fo:
    for n in nurls:
        fo.write(n[0] + '\n' + n[1] + '\n'*2)
