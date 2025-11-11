from colorama import Fore

def help_utility_main():
    print("\nAvailable commands: ")
    print("\n Built-in commands:" \
    "      \n - " + Fore.YELLOW + "help" + Fore.RESET + " : shows this help menu." \
    "      \n - " + Fore.YELLOW + "system-help" + Fore.RESET + ": shows your system's help menu." \
    "      \n - " + Fore.YELLOW + "random" + Fore.RESET + " : launches the random generator utility." \
    "      \n\n - " + Fore.YELLOW + "exit / quit" + Fore.RESET + " : exits the shell. " \
    
    "      \n\n" + Fore.GREEN + "If you are on Linux, you can run the commands you'd normally run to install/update/uninstall packages through this shell." \
    
    "      \n\n" + Fore.RESET + "Searching for and installing packages:" \
    "      \n - " + Fore.YELLOW + "search pip [package]" + Fore.RESET + " : opens your browser showing you pypi.org's results for that package." \
    "      \n - " + Fore.YELLOW + "install pip [package]" + Fore.RESET + " : installs the provided package." \
    "      \n - " + Fore.YELLOW + "search [package]" + Fore.RESET + " : searches for the provided name in winget's repository                                    - Works only for Windows." \
    "      \n - " + Fore.YELLOW + "install [package]" + Fore.RESET + " : installs the provided package (if winget finds it)                                      - Works only for Windows." \
   
    "      \n\n Updating packages:" \
    "      \n - " + Fore.YELLOW + "search pip updates" + Fore.RESET + " : shows a list of all the outdated pip libraries." \
    "      \n - " + Fore.YELLOW + "search app updates" + Fore.RESET + " : shows a list of all the outdated winget-available apps.                                - Works only for Windows." \
    "      \n - " + Fore.YELLOW + "search all updates" + Fore.RESET + " : runs the two commands above                                                            - Works only for Windows." \
    
    "      \n - " + Fore.YELLOW + "update all pip" + Fore.RESET + " : updates (interactively) all of the outdated pip libraries." \
    "      \n - " + Fore.YELLOW + "update pip [target]" + Fore.RESET + " : updates the provided package (if it isn't installed, it installs it)." \
    
    "      \n - " + Fore.YELLOW + "update all apps" + Fore.RESET + " : updates all of the outdated winget-available apps.                                        - Works only for Windows." \
    "      \n - " + Fore.YELLOW + "update all apps" + Fore.RESET + " : updates all of the outdated winget-available apps.                                        - Works only for Windows." \
    "      \n - " + Fore.YELLOW + "update all" + Fore.RESET + " : updates (interactively) pip libraries and (non-interactively) winget-available apps.           - Works only for Windows." \
        
    "      \n\n Listing and uninstalling packages:" \
    "      \n - " + Fore.YELLOW + "list pip" + Fore.RESET + " : lists all pip-managed packages." \
    "      \n - " + Fore.YELLOW + "uninstall pip [package]" + Fore.RESET + " : uninstalls the provided package." \
    "      \n - " + Fore.YELLOW + "list apps" + Fore.RESET + " : lists all installed apps                                                                          - Works only for Windows." \
    "      \n - " + Fore.YELLOW + "uninstall [package]" + Fore.RESET + " : uninstalls the provided package (if winget finds it)                                    - Works only for Windows." \
   
    "      \n - " + Fore.YELLOW + "list" + Fore.RESET + " : runs the 'list pip' command and the 'list apps' command                                                - Works only for Windows." \
    "      \n - " + Fore.YELLOW + "system [command]" + Fore.RESET + " : runs the specified command in the default system shell.")
    print(Fore.YELLOW + "\nNote that you can run multiple commands at once using '&&' between them." + Fore.RESET)