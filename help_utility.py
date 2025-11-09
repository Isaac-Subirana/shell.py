from colorama import Fore

def help_utility_main():
    print("\nPlease note that you can run multiple commands at once using '&&' between them.")
    print("\nAvailable commands: ")
    print("\n Built-in commands:" \
    "      \n - help : shows this help menu." \
    "      \n - system-help : shows your system's help menu." \
    "      \n - random : launches the random generator utility." \
    "      \n\n - exit / quit : exits the shell. " \
    
    "      \n\nIf you are on Linux, you can run the commands you'd normally run to install/update/uninstall packages through this shell." \
    
    "      \n\n Searching for and installing packages:" \
    "      \n - search pip [package] : opens your browser showing you pypi.org's results for that package." \
    "      \n - install pip [package] : installs the provided package." \
    "      \n - search [package] : searches for the provided name in winget's repository                                    - Works only for Windows." \
    "      \n - install [package] : installs the provided package (if winget finds it)                                      - Works only for Windows." \
   
    "      \n\n Updating packages:" \
    "      \n - search pip updates : shows a list of all the outdated pip libraries." \
    "      \n - search app updates : shows a list of all the outdated winget-available apps.                                - Works only for Windows." \
    "      \n - search all updates : runs the two commands above                                                            - Works only for Windows." \
    
    "      \n - update all pip : updates (interactively) all of the outdated pip libraries." \
    "      \n - update pip [target] : updates the provided package (if it isn't installed, it installs it)." \
    
    "      \n - update all apps : updates all of the outdated winget-available apps.                                        - Works only for Windows." \
    "      \n - update all apps : updates all of the outdated winget-available apps.                                        - Works only for Windows." \
    "      \n - update all : updates (interactively) pip libraries and (non-interactively) winget-available apps.           - Works only for Windows." \
        
    "      \n\n Listing and uninstalling packages:" \
    "      \n - list pip : lists all pip-managed packages." \
    "      \n - uninstall pip [package] : uninstalls the provided package." \
    "      \n - list apps : lists all installed apps                                                                          - Works only for Windows." \
    "      \n - uninstall [package] : uninstalls the provided package (if winget finds it)                                    - Works only for Windows." \
   
    "      \n - list : runs the 'list pip' command and the 'list apps' command                                                - Works only for Windows.")