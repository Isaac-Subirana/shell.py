from subprocess import run as subprocess_run
from colorama import Fore
import sys

def update_pip_modules_all():
    subprocess_run("python -m pip install --upgrade pip-review -q")
    print(f"\nAvailable updates: (confirm to update)")
    subprocess_run("pip-review -i")

def update_pip_module(target):
        print(f"Updating {target}...")
        subprocess_run(f"python -m pip install --upgrade {target}") 

def search_pip_updates():
    print("\nSearching for Python library updates...", end="\r")
    subprocess_run("python -m pip list --outdated")

def update_winget_apps_all():
    subprocess_run("winget upgrade --all --include-unknown")

def update_winget_app(target):
        subprocess_run(f"winget update {target}") 

def search_winget_updates():
    subprocess_run("winget upgrade --include-unknown")

def update_utility_main(command):
    c = list(map(str.lower, command.split()))

    if c[0] == "update" or c[0] == "upgrade":

        if c[1] == "all":
            if len(c) == 2:
                update_winget_apps_all()
                update_pip_modules_all()
            else:
                if c[2] == "pip":
                    update_pip_modules_all()
                elif c[2] == "app":
                    update_winget_apps_all()
        
        elif c[1] == "pip":
            update_pip_module((" ").join(c[2:]))
        
        elif c[1] == "app":
            update_winget_app((" ").join(c[2:]))
        
        else:
            print("This 'update' command does not exist. Run 'help' to see which commands exist.")
    
    elif c[0] == "search":
        if c[1] == "pip" and c[2] == "updates":
            search_pip_updates()
        elif c[1] == "app" and c[2] == "updates":
            search_winget_updates()
        elif c[1] == "all" and c[2] == "updates":
            search_winget_updates()
            search_pip_updates()
        else:
            print("This search command does not exist. Run 'help' to see which commands exist.")

    else: 
        try:
            print("Could not find this command in shell.py. Fallback to your system shell...")
            subprocess_run(command, shell=True)
        except:
            print(Fore.RED + f"Error: Your system does not recognize the command you tried to run  ('{command}')." + Fore.RESET)