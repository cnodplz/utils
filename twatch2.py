#!/usr/bin/python3
import re
import sys
import fileinput
import os
import subprocess

def procs(x="all_argv_files", y="re_string_compiled"):
    fn2 = x.filename()
    results = []
    results1 = []
    results2 = []
    d = 0
    atr = 0
    ctr = 0
    for line in x:
        fn1 = x.filename()
        z = re.search(y, line)
        z1 = re.findall(y, line)
        if z1:
            results2.append(z1)
        if z:
            results.append(z.group(0))
            d = {x3:results.count(x3) for x3 in results}
            if fn1 != fn2:
                '''print("_____[ {0} ]_____".format(fn1))'''
                '''results.append("_____[ {0} ]_____".format(fn1))'''
                d.update({fn1:fn1})
                del results[1:]
                fn2 = fn1
                '''for zz in d.keys():
                if d[zz] > 1:
                    print("{0: <16} {1}".format(zz, d[zz]))
                else:
                    print("{0: <16}".format(zz))'''
    try:
        for z1 in sorted(d.keys()):
            if d[z1] > 1:
                '''print("({1}) {0: <16} ({1}) {2}".format(z1, d[z1], subprocess.run(["dig", "+short", "-x", "{0}".format(z1)], stdout=subprocess.PIPE)))'''
                print("({1: <3}) {0: <24} {2: <64}".format(z1, d[z1], subprocess.getoutput("dig +short -x {0}".format(z1))))
                ctr+=1
            elif d[z1] == 1:
                '''print("{0: <16} ({1}) {2}".format(z1, " ", subprocess.run(["dig", "+short", "-x", "{0}".format(z1)], stdout=subprocess.PIPE)))'''
                print("({1: <3}) {0: <24} {2: <64}".format(z1, " ", subprocess.getoutput("dig +short -x {0}".format(z1))))
        print("TOTAL FOUND: {0}".format(len(results2)))
    except:
        print("No Address Found.")
            
def main():
    '''ipv4=re.compile(r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", re.MULTILINE)'''
    ipv4=re.compile("((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])", re.MULTILINE)
    '''ipv6=re.compile(r"([0-9a-zA-Z]{1,4}\:[0-9a-zA-Z]{1,4}\:[0-9a-zA-Z]{1,4}\:[0-9a-zA-Z]{1,4}\:[0-9a-zA-Z]{1,4}\:[0-9a-zA-Z]{1,4})", re.MULTILINE)'''
    ipv6=re.compile("(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))", re.MULTILINE)
#   patt2=re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
#   with open(sys.argv[1:], 'r+') as file1:
#   for line in fileinput.input():
#       #print("----- {0} -----".format(fileinput.filename()))
#        y = re.search(ipv4, line)
#        if y:
#            print(y.group(0))
#       '''for x in line:
#           y = re.search(ipv4, x)
#           if y:
#               print(y.group(0))'''
    '''fileinput iterates over lines from multiple input streams ie sys.argv[1:] defaulting to sys.stin if the list is empty'''
    print("-----IPv4-----")
    procs(fileinput.input(), ipv4)
    print("-----IPv6-----")
    procs(fileinput.input(), ipv6)

if __name__ == '__main__':
    main()
        
