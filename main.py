from subprocess import run as subprocess_run
import help_utility
from random_utility import random_utility_main
from install_utility import install_utility_main
from update_utility import update_utility_main

command = ""

shellcommands = ["help", "system-help", "random", "install", "update", "upgrade"]

def echo(string):
    print(string)

def runcommand():
    command_lst = input("\nshell.py 1.1> ").split(", ")
    for i in range(0, len(command_lst)):
        command = command_lst[i]
        isnotexit(command)
        try:
            for cmd in shellcommands:
                if cmd in command.lower():
                    runshellcommand(command)
                    break
            else: 
                subprocess_run(command, shell=True)
        except:
            print(f"Error: Your system does not recognize the command you tried to run (' {command} ').")
    runcommand()
    

def isnotexit(command):
    exitaliases = ["exit", "quit", "e", "q"]
    if command.lower() in exitaliases:
        exit()
 
def runshellcommand(command):
    if command.lower() == "help":
        help_utility.help_utility_main()
    elif command.lower()[:11] == "system-help":
        subprocess_run("help" + command[11:])
    elif command.lower() == "random":
        random_utility_main()
    elif "install" in command.lower():
        install_utility_main(command)
    elif "update" in command.lower() or "upgrade" in command.lower():
        update_utility_main(command)

def main():
    print("Basic shell in Python. Version 1.1")
    runcommand()

main()