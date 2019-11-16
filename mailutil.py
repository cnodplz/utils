#!/usr/bin/env python
from time import gmtime, strftime, localtime
import os
import hashlib
import smtplib

tobj = strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())

h1 = hashlib.sha256()
h2 = hashlib.sha512()
h3 = hashlib.sha1()

h1.update("hash")
h2.update("hash")

pathstr = '/home/u/user001/pdata1.csv'
homestr = '/home/u/user001/'
sudir = '/etc/sudoers'
servlist = ['admin1.example.gov',
            'admin2.example.gov',
            'security.example.gov',
            'security2.example.gov']

paths = []
hashed = []
exists = []
mtime = []

for x in servlist:
    paths.append(homestr + x + sudir)

for x in paths:
    with open(x, 'rb') as fo:
        buf = fo.read()
        h3.update(buf)
        hashed.append(h3.hexdigest())
        exists.append(os.path.exists(x))
        mtime.append(strftime("%a, %d %b %Y %H:%M:%S",localtime(os.path.getmtime(x))))

with open(pathstr, 'rb') as fo:
    buf = fo.read()
    h3.update(buf)

thispath = os.path.abspath(pathstr)
thispath1 = os.path.getmtime(pathstr)

tobj1 = strftime("%a, %d %b %Y %H:%M:%S",localtime(thispath1))
'''
print "File Check\n------------\n{0:10} : {5}\n{1:10} : {6}\n{2:10} : {7}\n{3:10} : {8}\n{4:10} : {9}\n".format("Date: ", "Modified: ", "Path: ", "Exists: ", "SHA1: ", tobj, tobj1, thispath, os.path.exists(pathstr), h3.hexdigest(), end="")
'''

wform = open("hdat.txt", "r+")

for a, b, c, d in zip(mtime, paths, exists, hashed):
    wform.write(str("SI-07 - File Check\n------------\n{0:10} : {5}\n{1:10} : {6}\n{2:10} : {7}\n{3:10} : {8}\n{4:10} : {9}\n\n".format("Path: ", "Date: ", "Modified: ", "Exists: ", "SHA1: ", b, tobj, a, c, d, end="")))

wform.close()
wform = open("hdat.txt", "r+")
readhdat = wform.read()
print readhdat

sender = 'admin@admin1.example.gov'
receive = ['user@example.gov']
message = """From: From <%s>
             To: To <%s>
             Subject: Subject Line
             %s
             --
          """ % (sender, receive, readhdat)
try:
    s = smtplib.SMTP('localhost')
    s.sendmail(sender, receive, message)
    print "smtp ok"
except:
    print "smtp fail"
