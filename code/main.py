internal_libraries = ["help_utility", "random_utility", "install_utility", "update_utility", "uninstall_utility"]

print("Initializing...")

print("\nImporting some of python's default external libraries...")

from subprocess import run as subprocess_run
from webbrowser import open
from os import getcwd, chdir
from os.path import exists
from time import sleep
from sys import stdout

print("Done! I can now run commands, among other things!")

print("\nChecking whether colorama is installed, installing it if it isn't..."), stdout.flush()
subprocess_run("python -m pip install colorama")
from colorama import Fore
print(Fore.GREEN + "\nDone!" + Fore.YELLOW +" I can now print in color!" + Fore.RESET)

print(Fore.YELLOW + "\nChecking file integrity and importing internal libraries:")
sleep(0.250)
for i in internal_libraries:
    print(Fore.RESET + f"   Importing {i}... ", end=""), stdout.flush()
    if exists(f"{i}.py"):
        print(Fore.GREEN + "Done!")
    else:
        print(Fore.RED + f"\n\tERROR! {i}.py not found!")
        print("\tPlease, redownload the code from github and re-run!")
        print("\tWill automatically open the GitHub project and exit the shell in ", end=""), stdout.flush()
        for i in range(0, 15):
            print(15 - i, end=", "), stdout.flush()
            sleep(1)
        open("https://github.com/Isaac-Subirana/shell.py")
        exit()
sleep(0.500)

import help_utility
from random_utility import random_utility_main
from install_utility import install_utility_main
from update_utility import update_utility_main
from uninstall_utility import uninstall_utility_main


shellcommands = ["help", "system-help", "random", "install", "search", "update", "upgrade", "cd", "list", "uninstall", "system"]

command = ""

def runcommand():
    command_lst = input(Fore.YELLOW + "\nshell.py" + Fore.RESET + f" - {getcwd()} > ").split("&&")
    for i in range(0, len(command_lst)):
        command = command_lst[i]
        isnotexit(command)
        try:
            cmd = command.split()
            if cmd[0].lower() in shellcommands:
                runshellcommand(command)

            else:
                print("Could not find this command in shell.py. Fallback to your system shell...")
                subprocess_run(command, shell=True)

        except:
            print(Fore.RED + f"Error: Your system does not recognize the command you tried to run ('{command}')." + Fore.RESET)
    runcommand()
    

def isnotexit(command):
    exitaliases = ["exit", "quit", "e", "q"]
    if command.lower() in exitaliases:
        print("Exit... Done!")
        exit()
 
def runshellcommand(command):
    command = command.lower()

    if command == "help":
        help_utility.help_utility_main()

    elif command == "cd":
        print(getcwd())

    elif command[:2] == "cd":
        cd_to = getcwd() + "/" + command[3:]
        if exists(command[3:]):
            chdir(command[3:])
            print(getcwd())
        elif exists(cd_to):
            chdir(cd_to)
            print(getcwd())
        else:
            print(Fore.RED + "The path you specified does not exist, so I can not 'cd' into it." + Fore.YELLOW + "\nDid you want to create a folder? Try 'mkdir'!" + Fore.RESET)

    elif command[:11] == "system-help":
        subprocess_run("help" + command[11:])

    elif command[:6] == "system": # no li sap
        print(Fore.YELLOW + "Running the command you specified on your system shell..." + Fore.RESET)
        subprocess_run(command[7:], shell = True)

    elif command == "random":
        random_utility_main()

    elif "update" in command or "upgrade" in command:
        update_utility_main(command)

    
    elif "uninstall" in command or "list" in command:
        uninstall_utility_main(command)

    elif "install" in command or "search" in command:
        install_utility_main(command)   

def main():
    subprocess_run("cls", shell=True)
    print(Fore.RESET + "Welcome to " + Fore.YELLOW + "shell.py" + Fore.RESET + ", a basic shell in Python!")
    sleep(1)
    runcommand()

main()