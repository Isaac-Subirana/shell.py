import help_utility
from random_utility import random_utility_main
from install_utility import install_utility_main
from update_utility import update_utility_main

from subprocess import run as subprocess_run
from os import getcwd, chdir
from time import sleep

command = ""

shellcommands = ["help", "system-help", "random", "install", "update", "upgrade", "cd"]

def echo(string):
    print(string)

def runcommand():
    command_lst = input(f"\nshell.py - {getcwd()} > ").split(", ")
    for i in range(0, len(command_lst)):
        command = command_lst[i]
        isnotexit(command)
        try:
            for cmd in shellcommands:
                if cmd in command.lower():
                    runshellcommand(command)
            else: 
                subprocess_run(command, shell=True)
        except:
            print(f"Error: Your system does not recognize the command you tried to run ('{command}').")
    runcommand()
    

def isnotexit(command):
    exitaliases = ["exit", "quit", "e", "q"]
    if command.lower() in exitaliases:
        exit()
 
def runshellcommand(command):
    command = command.lower()

    if command == "help":
        help_utility.help_utility_main()
    elif command == "cd":
        getcwd()
    elif command[:3] == "cd ":
        chdir(command[3:])
    elif command[:11] == "system-help":
        subprocess_run("help" + command[11:])
    elif command == "random":
        random_utility_main()
    elif "install" in command:
        install_utility_main(command)
    elif "update" in command or "upgrade" in command:
        update_utility_main(command)

def main():
    print("Initializing...")
    sleep(0.600)
    subprocess_run("cls", shell=True)
    print("Welcome to shell.py, a basic shell in Python!")
    sleep(1)
    runcommand()

main()