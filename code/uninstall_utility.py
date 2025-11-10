from subprocess import run as subprocess_run
from colorama import Fore

def uninstall_pip_module(target):
        print("Updating pip...")
        subprocess_run(f"python -m pip install --upgrade pip -q")
        print(f"Uninstalling {target}...")
        subprocess_run(f"python -m pip uninstall {target}") 

def list_pip():
       subprocess_run("python -m pip list")

def uninstall_winget_app(target):
        print(f"Uninstalling {target}...")
        subprocess_run(f"winget uninstall {target}") 

def list_winget():
        subprocess_run(f"winget list") 

def uninstall_utility_main(command):
    c = command.split()

    if c[0].lower() == "uninstall":
        if c[1].lower() == "pip":
            uninstall_pip_module((" ").join(c[2:]))
        else:
            uninstall_winget_app((" ").join(c[2:]))

    elif c[0].lower() == "list":
        if c[1].lower() == "pip":
            list_pip()
        elif c[1].lower() == "apps":
            list_winget()
        else:
            list_pip()
            list_winget()
 
    else: 
        try: 
            subprocess_run(command, shell=True)
        except:
            print(Fore.RED + f"Error: Your system does not recognize the command you tried to run ('{command}')." + Fore.RESET)