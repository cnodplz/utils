#!/usr/bin/env python3
import string
import sys

def encrypt1(a, b):
    hash2 = b
    hash3 = ""
    '''error if value in string not in dictionary'''
    for x in hash2:
        if x == ' ':
            hash3 += ' '
        else:
            try:
                hash3 += a[x]
            except:
                print("Values: a-z and spaces.")
    return hash3
    
def main(argv):

    ''' alpha1 = a-z
        alpha2 = z-a
        alpha3 = 0-26

        dictio1 = 0 a, 1 b, 2 c
        dictio2 = 0 z, 1 y, 2 c
        dictio3 = a 0, b 1, c 2
    '''
    alpha1 = []
    alpha2 = []
    alpha3 = []

    dictio1 = dict()
    dictio2 = dict()
    dictio3 = dict()

    message1 = "hello this is puzz"
    if len(sys.argv) > 1:
        for x in range(1,len(sys.argv)):
            message1 += " {0}".format(str(sys.argv[x]))
    message2 = 'hello this is puzz'

    for x in string.ascii_lowercase:
        alpha1.append(x)
    
    for x in reversed(string.ascii_lowercase):
        alpha2.append(x)

    for x in range(0,26):
        alpha3.append(str(x))
   
    dictio3 = dict(zip(alpha1, alpha3))
 
    for x in range(0,26):
        dictio1[str(x)] = alpha1[x]
        dictio2[str(x)] = alpha2[x]

    ''' Spaces handled in function
    dictio1[27] = " "
    dictio2[27] = " "
    dictio3[" "] = '27'
    '''

    '''Main Calls'''
    hash1 = encrypt1(dictio3, message1)
    hash2 = encrypt1(dictio3, message2)

    print("alpha1: {0}\nalpha2: {1}\nalpha3: {2}\ndictio1: {3}\ndictio2: {4}\ndictio3: {5}\nhash1: {6}\nhash2: {7}".format(alpha1, alpha2, alpha3, dictio1, dictio2, dictio3, hash1, hash2))
        
if __name__=='__main__':
    main(sys.argv[1:])
