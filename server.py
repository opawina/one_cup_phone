#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Beautiful code!
'''

import socket
import sys
import getopt

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:p:", ["help", "addr=", "port="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    a = 1
    # output = None
    # verbose = False
    # for o, a in opts:
    #     if o == "-v":
    #         verbose = True
    #     elif o in ("-h", "--help"):
    #         usage()
    #         sys.exit()
    #     elif o in ("-o", "--output"):
    #         output = a
    #     else:
    #         assert False, "unhandled option"