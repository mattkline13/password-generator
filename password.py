#! /usr/bin/python

import string
import sys
import getopt
from random import randint 

argumentList = sys.argv[1:] 
options = "hrdc:f:ls"
long_options = ["help", "random", "dictionary", "count =", "files =", "seperator", "leadingSymbol"] 
characters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)
count = 0
password = ""
file = open("../Text Files/dictionary.txt", "r").readlines()
seperator = False
leadingSymbol = False

def main():
    global count, file, seperator, leadingSymbol

    try: 
        arguments, values = getopt.getopt(argumentList, options, long_options) 
        
        for currentArgument, currentValue in arguments: 
            if currentArgument in ("-h", "--help"): 
                print("-r, --random            Generate a random password.")
                print("                        Will default to 20 characters if no argument is supplied for '--count'.")
                print("                        Example usage: password.py -c <count> -r")
                print("-d, --dictionary        Generate a random password using a dictionary of words.")
                print("                        Will default to 3 words if no argument is supplied for '--count'.")
                print("                        Will default to built in dictionary if no list is supplied using '--file'.")
                print("                        Example usage passoword.py -c <count> -file <dictionary> -d")
                print("-c, --count             Specify the number of characters in the '--random' option or number of words in the '--dictionary' option.")
                print("-f, --file              Specify a custom dictionary file to be used in the '--dictionary' option.")
                print("-s, --seperator         Specify if the words in the '--dictionary' option should be seperated with a '-'.")
                print("-l, --leadingSymbol     Specify if the password should start with a symbol in the '--dictionary' option .")
            elif currentArgument in ("-r", "--random"): 
                random() 
            elif currentArgument in ("-d", "--dictionary"): 
                dictionary()
            elif currentArgument in ("-c", "--count"): 
                count = int(currentValue)
            elif currentArgument in ("-f", "--file"): 
                file = open(currentValue, "r").readlines()
            elif currentArgument in ("-s", "--seperator"): 
                seperator = True
            elif currentArgument in ("-l", "--leadingSymbol"): 
                leadingSymbol = True
                
    except getopt.error as err: 
        print (str(err)) 

def random():
    global count, file, password

    if count == 0: count = 20

    for x in range(count):
        value = randint(0, 20)
        if (value % 20) == 0: password = password + symbols[randint(0, len(symbols) - 1)]
        elif (value % 4) == 0: password = password + digits[randint(0, len(digits) - 1)]
        else: password = password + characters[randint(0, len(characters) - 1)]
    
    print("The generated password is: " + password)

def dictionary():
    global count, file, password, seperator, leadingSymbol

    if count == 0: count = 3
    if leadingSymbol: password = symbols[randint(0, len(symbols) - 1)]

    for x in range(count):
        password = password + file[randint(0, len(file) - 1)].capitalize().rstrip("\n").replace(" ", "_")
        if seperator and x + 1 < count: password = password + "-"

    print("The generated password is: " + password)

main()