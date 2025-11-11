from subprocess import run as subprocess_run
from time import sleep
from webbrowser import open
from colorama import Fore

def install_pip_module(target):
        print("Updating pip...")
        subprocess_run(f"python -m pip install --upgrade pip -q")
        print(f"Installing {target}..." + Fore.RESET)
        subprocess_run(f"python -m pip install {target}") 

def search_pip(target):
        print("Opening pypi.org page for the target specified in your default web browser... (3 seconds)")
        sleep(3)
        open(f"https://pypi.org/search/?q=%2F{target}&o=")

def install_winget_app(target):
        print(f"Installing {target}...")
        subprocess_run(f"winget install {target}") 

def search_winget(target):
        subprocess_run(f"winget search {target}")

def install_utility_main(command):
    c = command.split()

    if c[0].lower() == "install":
        if c[1].lower() == "pip":
            install_pip_module((" ").join(c[2:]))
        else:
            install_winget_app((" ").join(c[2:]))

    elif c[0].lower() == "search":
        if c[1].lower() == "pip":
            search_pip((" ").join(c[2:]))
        else:
            search_winget((" ").join(c[2:]))
 
    else: 
        try: 
            print("Could not find this command in shell.py. Fallback to your system shell...")
            subprocess_run(command, shell=True)
        except:
            print(Fore.RED + f"Error: Your system does not recognize the command you tried to run ('{command}')." + Fore.RESET)