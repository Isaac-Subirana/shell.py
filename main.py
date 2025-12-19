internal_libraries = ["help_utility", "random_utility", "install_utility", "update_utility", "uninstall_utility"]

print("Initializing...")

print("\nImporting some of python's default external libraries...")

from subprocess import run as subprocess_run
from webbrowser import open as open_browser
from os import getcwd, chdir, getlogin, remove
from os.path import exists
from time import sleep
from sys import stdout

print("Done! I can now run commands, among other things!")

print("\nChecking whether colorama is installed, installing it if it isn't..."), stdout.flush()
subprocess_run("python -m pip install colorama")
from colorama import Fore
print(Fore.GREEN + "\nDone!" + Fore.CYAN +" I can now print in color!" + Fore.RESET)

print(Fore.CYAN + "\nImporting internal libraries..." + Fore.RESET, end=""), stdout.flush()
try:
    import help_utility
    from random_utility import random_utility_main
    from install_utility import install_utility_main
    from update_utility import update_utility_main
    from uninstall_utility import uninstall_utility_main
    print(Fore.GREEN + " Done!")
except: 
    print(Fore.RED + " NOT DONE!\nError: internal libraries not found! Please redownload this project from its github project (github.com/Isaac-Subirana/shell.py) which should open in your default browser in 3 seconds.")
    sleep(3)
    open_browser("https://github.com/Isaac-Subirana/shell.py")
    input("\n" + Fore.RESET + "-" * 50 + "Press ENTER to exit." + "-" * 50)
    exit()

eastereggs = ["rick", "canyouhearme", "max", "maxwell"]
extra = ["search", "install", "update", "upgrade", "list", "uninstall"]
basic = ["help", "random", "cd", "system", "isay", "echo"]
shellcommands = basic + extra + eastereggs

command = ""

def runcommand():
    command_lst = input(Fore.CYAN + "\nshell.py" + Fore.RESET + f" - {getcwd()} > ").split(";")
    for i in range(0, len(command_lst)):
        command = command_lst[i]
        isnotexit(command)
        try:
            cmd = command.split()
            if cmd[0].lower() in shellcommands:
                runshellcommand(command)

            else:
                print(Fore.CYAN + "Could not find this command in shell.py. " + Fore.RESET + "Fallback to your system shell..." + Fore.RESET)
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

    if command[:4] == "isay":
        command = command[5:]
        print(Fore.CYAN + f"Running '{command}' in the default system shell as administrator (it will open in a separate window)..." + Fore.RESET)
        
        with open(f"C:\\Users\\{getlogin()}\\Documents\\isay_command-runner.bat", "w") as file:
            file.write(f"""@echo off\nnet session >nul 2>&1 || (powershell start-process -filepath '%~f0' -verb runas && exit /b)\n{command}\npause\ndel "%~f0" >nul 2>&1""")
        subprocess_run(f"C:\\Users\\{getlogin()}\\Documents\\isay_command-runner.bat", shell = True)

    elif command == "help":
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
            print(Fore.RED + "The path you specified does not exist, so I can not 'cd' into it." + Fore.CYAN + "\nDid you want to create a folder? Try 'mkdir'!" + Fore.RESET)

    elif command[:4] == "echo":
        specialfunctions = ["<", ">", "|", "&", "%", '"', "!", "^", "*", "(", ")", "?", "[", "]", ":", "{", "}"]
        specialfunction = False

        for i in specialfunctions:
            if i in command:
                specialfunction = True
                break

        if specialfunction == True:
            subprocess_run(command)
        else:
            print(command[5:])

    elif command[:6] == "system":
        print(Fore.CYAN + "Running the command you specified on your system shell..." + Fore.RESET)
        subprocess_run(command[7:], shell = True)

    elif command == "random":
        random_utility_main()

    elif "update" in command or "upgrade" in command:
        update_utility_main(command)

    
    elif "uninstall" in command or "list" in command:
        uninstall_utility_main(command)

    elif "install" in command or "search" in command:
        install_utility_main(command)   
    
    elif command == "rick" or "canyouhearme" in command:
        print("You can exit the following trick using Ctrl + C, and still be in this shell. " +  Fore.CYAN + "\nGood luck!" + Fore.RESET)
        for i in range(0, 5):
            print(5 - i)
            sleep(1)
        sleep(1.500)
        print(Fore.CYAN + "Thought you could save yourself?" + Fore.RESET)
        sleep(1)
        subprocess_run("curl ascii.live/rick")
    
    elif command == "max" or command == "maxwell":
        print("You can exit the following trick using Ctrl + C, and still be in this shell. " +  Fore.CYAN + "\nGood luck!" + Fore.RESET)
        sleep(3)
        subprocess_run("curl ascii.live/maxwell")

def main():
    subprocess_run("cls", shell=True)
    print(Fore.RESET + "Welcome to " + Fore.CYAN + "shell.py" + Fore.RESET + ", a basic shell in Python!")
    sleep(1)
    runcommand()

main()