import pyping
import os
from sys import platform

__Author__ = "HiiZun"
username = "HiiZun"
passcode = "cheesecake"

print 'welcome back please login'
login = raw_input("login as:")
if login != "HiiZun":
    print "error: this user don't exist ! "
    exit(1)
else:
    print "welcome back HiiZun please write your password"
    password = raw_input("password:")
    while password != passcode:
        codeword = raw_input("wrong password please retry:")
        if codeword == passcode:
            break

print "welcome to your terminal "
while "true" == "true":
    command = raw_input("$")
    if command == "exit":
        print "goodbye"
        exit(0)
    elif command == "ping":
        print "please enter the host to ping"
        toping = raw_input("to ping:")

        response = pyping.ping(toping)

        if response.ret_code == 0:
            print("ping: reachable")
        else:
            print("ping: unreachable")
    elif command == "help":
        print "commands:"
        print "======================"
        print "help => show this page"
        print "exit => exit the terminal"
        print "ipconfig => get network informations (windows only)"
        print "wget => download files from the web (Unix systems only)"
        print "ls => get list of files in the folder (Unix systems only)"
        print "======================"
    elif command == "russia":
        print "Cyka Blyat"
    elif command == "ls":
        if platform == "linux" or platform == "linux2":
            print "[ ok ] showing all files here"
            os.system('ls')
        elif platform == "darwin":
            print "showing all files here"
            os.system('ls')
        elif platform == "win32":
            print "[ ok ] showing all files here"
            os.system('tree')
        else:
            print "internal error please communicate this error code to the support: re400"
    elif command == "wget":
        wgeturl = raw_input("insert the url please:")
        os.system('wget ' + wgeturl)
    elif command == "ipconfig":
        os.system('ipconfig')
    elif command == "reboot":
        if platform == "linux" or platform == "linux2":
            print "[ ok ] processing..."
            print "rebooting"
            os.system('reboot')
        elif platform == "darwin":
            print "processing..."
            print "rebooting"
            os.system('reboot')
        elif platform == "win32":
            print "rebooting..."
            os.system("shutdown /r")
        else:
            print "internal error please communicate this error code to the support: re400"
    else:
        print "Error: this command don't exist !"
