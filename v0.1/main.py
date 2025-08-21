from subprocess import run as subprocess_run
import help_utility
from random_utility import random_utility_main

command = ""

shellcommands = ["help", "default-help", "random"]

def panic():
    print("Something went wrong. Please try again.")
    runcommand()

def runcommand():
    command = input("\nshell.py 0.1> ")
    isnotexit(command)
    try:
        if command.lower() in shellcommands:
            runshellcommand(command)
            runcommand()
        else: 
            subprocess_run(command)
            runcommand()
    except FileNotFoundError:
        print("Error: Your system does not recognize the command you tried to run.")
        runcommand()
    

def isnotexit(command):
    exitaliases = ["exit", "quit", "q", "kill", "k"]
    if command.lower() in exitaliases:
        exit()
 
def runshellcommand(command):
    if command == "help":
        help_utility.help_utility_main()
    elif command == "default-help":
        subprocess_run("help")
    elif command == "random":
        random_utility_main()

def main():
    print("Basic shell in Python, designed for all Operating Systems.\nVersion 0.1")
    #Version 0.1: the shell now has help, aliases for "exit" and a utility to generate random things.
    runcommand()

main()