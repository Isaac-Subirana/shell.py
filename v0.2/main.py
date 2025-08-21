from subprocess import run as subprocess_run
import help_utility
from random_utility import random_utility_main
from install_utility import install_utility_main

command = ""

shellcommands = ["help", "default-help", "random", "install"]

def runcommand():
    command_lst = input("\nshell.py 0.2> ").split(", ")
    for i in range(0, len(command_lst)):
        command = command_lst[i]
        isnotexit(command)
        try:
            for i in shellcommands:
                if i in command.lower():
                    runshellcommand(command)
                    runcommand()
            else: 
                print(command)
                subprocess_run(command)
                runcommand()
        except FileNotFoundError:
            print(f"Error: Your system does not recognize the command ('{command}') you tried to run.")
    runcommand()
    

def isnotexit(command):
    exitaliases = ["exit", "quit", "e", "q"]
    if command.lower() in exitaliases:
        exit()
 
def runshellcommand(command):
    if command == "help":
        help_utility.help_utility_main()
    elif command == "default-help":
        subprocess_run("help")
    elif command == "random":
        random_utility_main()
    elif "install" in command:
        install_utility_main(command)

def main():
    print("Basic shell in Python, works fully only in Windows.\nVersion 0.2")
    #Version 0.2: the shell now allows you to install python modules and winget apps through it.
    runcommand()

main()