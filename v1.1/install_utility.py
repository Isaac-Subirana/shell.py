from subprocess import run as subprocess_run

def install_pip_modules_list(sure):
    if "y" in sure:
        print("Updating pip...")
        subprocess_run("python.exe -m pip install --upgrade pip -q")
        print("Installing pycryptodome, unidecode, numpy, matplotlib, pillow, pygame, chess, pyinstaller, phonenumbers and pip-review...")
        subprocess_run("pip install pycryptodome unidecode numpy matplotlib pillow pygame chess pyinstaller phonenumbers pip-review")
    elif "n" in sure:
        wait()
    else:
        sure= input("Please input [Y]es or [N]o.\t") 
        install_pip_modules_list(sure)

def install_pip_module(target):
        print("Updating pip...")
        subprocess_run(f"python.exe -m pip install --upgrade pip -q")
        print(f"Installing {target}...")
        subprocess_run(f"pip install {target}") 

def install_winget_apps_list(sure):
    if "y" in sure:
        print("Installing 7zip, Microsoft Edit, Microsoft Powershell, Notepad++, Bulk Rename Utility, XnView MP and VLC media player...")
        subprocess_run("winget install 7zip.7zip Microsoft.Edit Microsoft.Powershell Notepad++.Notepad++ TGRMNSoftware.BulkRenameUtility XnSoft.XnViewMP VideoLAN.VLC")
    elif "n" in sure:
        wait()
    else:
        sure= input("Please input [Y]es or [N]o.\t") 
        install_winget_apps_list(sure)

def install_winget_app(target):
        print(f"Installing {target}...")
        subprocess_run(f"winget install {target}") 

def install_apt_app(target):
        print(f"Installing {target}...")
        subprocess_run(f"sudo apt install {target}") 

def wait():
    input("\n---------- Press ENTER to go back to the shell ----------")

def install_utility_main(command):
    c = command.split()
    if c[0].lower() == "install" and c[1].lower() == "pip" and c[2].lower() == "list":
        sure = input("You have chosen to install a bunch of pip libraries that the editor recommends. These are:" \
        "\npycryptodome, unidecode, numpy, matplotlib, pillow, phonenumbers, pygame, chess, pyinstaller and pip-review." \
        "\n\n Are you sure you want to continue (Y/N)?\n >_ ").lower()
        install_pip_modules_list(sure)
    elif c[0].lower() == "install" and c[1].lower() == "pip":
        install_pip_module((" ").join(c[2:]))

    elif c[0].lower() == "install" and c[1].lower() == "winget" and c[2].lower() == "list":
        sure = input("You have chosen to install a bunch of winget-available apps that the editor recommends. These are:" \
        "\n7zip, Microsoft Edit, Microsoft Powershell, Notepad++, Bulk Rename Utility, XnViewMP and VLC media player." \
        "\n\n Are you sure you want to continue (Y/N)?\n >_ ").lower()
        install_winget_apps_list(sure)
    elif c[0].lower() == "install" and c[1].lower() == "winget":
        install_winget_app((" ").join(c[2:]))
    elif c[0].lower() == "install" and (c[1].lower() == "apt" or c[1].lower() == "apt-get"):
        install_apt_app((" ").join(c[2:]))
    
    else: 
        try: 
            print(command)
            subprocess_run(command)
        except FileNotFoundError:
            print(f"Error: Your system does not recognize the command you tried to run (' {command} ').")