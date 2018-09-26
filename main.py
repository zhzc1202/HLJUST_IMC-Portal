#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys, getopt

username = ''
password = ''
DebugFlag   =    0
LogoutFlag  =    0

def arguments(argv):
    #module reference : http://www.runoob.com/python3/python3-command-line-arguments.html
    global username 
    global password
    global DebugFlag
    global LogoutFlag
    #global variance referecne : https://www.cnblogs.com/yanfengt/p/6305542.html
    try:
        opts, args = getopt.getopt(argv,"hdqu:p:")
    except getopt.GetoptError:
                print ('err: main.py -u <UserName> -p <Password> -d <Debug Mode> -q <Logout>')
                sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
                print ('main.py -u <UserName> -p <Password> -d <Debug Mode> -q <Logout>')
                sys.exit()
        elif opt in ("-d"):
                    DebugFlag = 1
        elif opt in ("-q"):
                    LogoutFlag = 1
        elif opt in ("-u"):
                    username = arg
        elif opt in ("-p"):
                    password = arg
                    
    print ('UserName:', username)
    print ('Password:', password)
    print ('Debug Mode:', DebugFlag)
    print ('LogoutFlag:', LogoutFlag)

def Login():
    print ('UserName:', username)
    print ('Password:', password)
    print ('Debug Mode:', DebugFlag)
    print ('LogoutFlag:', LogoutFlag)


if __name__ == "__main__":
    arguments(sys.argv[1:])
    Login()
