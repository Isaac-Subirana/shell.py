from subprocess import run as subprocess_run

def update_pip_modules_all():
    print("\nUpdating pip...")
    subprocess_run("python.exe -m pip install --upgrade pip -q")
    subprocess_run("pip install --upgrade pip-review -q")
    print(f"\nAvailable updates: (confirm to update)")
    subprocess_run("pip-review -i")

def update_pip_module(target):
        print("\nUpdating pip...")
        subprocess_run(f"python.exe -m pip install --upgrade pip -q")
        print(f"\nUpdating {target}...")
        subprocess_run(f"pip install --upgrade {target}") 

def search_pip_updates():
    print("\nUpdating pip...")
    subprocess_run("python.exe -m pip install --upgrade pip -q")
    print("Searching for updates...\n")
    subprocess_run("pip list --outdated")

def update_winget_apps_all():
    subprocess_run("winget upgrade --all --include-unknown")

def update_winget_app(target):
        print(f"Updating {target}...")
        subprocess_run(f"winget update {target}") 

def search_winget_updates():
    subprocess_run("winget upgrade --include-unknown")

def update_apt_apps_all():
    subprocess_run("sudo apt update && sudo apt upgrade")

def update_apt_app(target):
    subprocess_run(f"sudo apt update && sudo apt install --only-upgrade {target}")

def search_apt_updates():
    subprocess_run("sudo apt update")

def wait():
    input("\n---------- Press ENTER to go back to the shell ----------")

def update_utility_main(command):
    c = list(map(str.lower, command.split()))

    if c[0] == "update" or c[0] == "upgrade":
        if c[1] == "pip" and c[2] == "all":
            update_pip_modules_all()
        elif c[1] == "pip":
            update_pip_module((" ").join(c[2:]))
        
        elif c[1] == "winget" and c[2] == "all":
            update_winget_apps_all()
        elif c[1] == "winget":
            update_winget_app((" ").join(c[2:]))
        
        elif (c[1] == "apt" or c[1] == "apt-get") and c[2] == "all":
            update_apt_apps_all()
        elif (c[1] == "apt" or c[1] == "apt-get"):
            update_apt_app((" ").join(c[2:]))
    
    elif c[0] == "search" and ("update" in c[1] or "upgrade" in c[1]):
        if c[2] == "pip":
            search_pip_updates()
        elif c[2] == "winget":
            search_winget_updates()
        elif c[2] == "apt":
            search_apt_updates()


    else: 
        try: 
            print(command)
            subprocess_run(command)
        except FileNotFoundError:
            print(f"Error: Your system does not recognize the command you tried to run  (' {command} ').")