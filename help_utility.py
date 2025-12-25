from colorama import Fore

def help_utility_main():
    print("\nAvailable commands: ")
    print("\n Built-in commands:" \
    "      \n - " + Fore.CYAN + "help" + Fore.RESET + " : shows this help menu." \
    "      \n - " + Fore.CYAN + "random" + Fore.RESET + " : launches the random generator utility." \
    "      \n - " + Fore.CYAN + "system [command]" + Fore.RESET + " : runs the specified command in the default system shell." \
    "      \n - " + Fore.CYAN + "isay [command]" + Fore.RESET + " : runs the specified command in the default system shell, with admin privileges.             - Works only for Windows." \
    "      \n - " + Fore.CYAN + "cd / cd [folder/path]" + Fore.RESET + " : shows the path you are currently working in / changes your working directory."
    "      \n - " + Fore.CYAN + "mkdir [folder/path]" + Fore.RESET + " : creates the folder/path you pass it."
    "      \n - " + Fore.CYAN + "delete [folder/file/path]" + Fore.RESET + " : deletes the folder/file/path you pass it."
    "      \n - " + Fore.CYAN + "rick / canyouhearme" + Fore.RESET + " : ... what do you think this command does?" \
    "      \n - " + Fore.CYAN + "max / maxwell" + Fore.RESET + " : Max. Isn't he cute?"
    "      \n\n - " + Fore.CYAN + "exit / quit" + Fore.RESET + " : exits the shell. " \
    
    "      \n\n" + Fore.GREEN + "If you are on Linux, you can run the commands you'd normally run to install/update/uninstall packages through this shell." \
    
    "      \n\n" + Fore.RESET + "Searching for and installing packages:" \
    "      \n - " + Fore.CYAN + "search pip [package]" + Fore.RESET + " : opens your browser showing you pypi.org's results for that package." \
    "      \n - " + Fore.CYAN + "install pip [package]" + Fore.RESET + " : installs the provided package." \
    "      \n - " + Fore.CYAN + "search [package]" + Fore.RESET + " : searches for the provided name in winget's repository                                    - Works only for Windows." \
    "      \n - " + Fore.CYAN + "install [package]" + Fore.RESET + " : installs the provided package (if winget finds it)                                      - Works only for Windows." \
   
    "      \n\n Updating packages:" \
    "      \n - " + Fore.CYAN + "search pip updates" + Fore.RESET + " : shows a list of all the outdated pip libraries." \
    "      \n - " + Fore.CYAN + "search app updates" + Fore.RESET + " : shows a list of all the outdated winget-available apps.                                - Works only for Windows." \
    "      \n - " + Fore.CYAN + "search all updates" + Fore.RESET + " : runs the two commands above                                                            - Works only for Windows." \
    
    "      \n - " + Fore.CYAN + "update all pip" + Fore.RESET + " : updates (interactively) all of the outdated pip libraries." \
    "      \n - " + Fore.CYAN + "update pip [target]" + Fore.RESET + " : updates the provided package (if it isn't installed, it installs it)." \
    
    "      \n - " + Fore.CYAN + "update all apps" + Fore.RESET + " : updates all of the outdated winget-available apps.                                        - Works only for Windows." \
    "      \n - " + Fore.CYAN + "update app [target]" + Fore.RESET + " : updates the provided package via winget.                                              - Works only for Windows." \
    "      \n - " + Fore.CYAN + "update all" + Fore.RESET + " : updates (interactively) pip libraries and (non-interactively) winget-available apps.           - Works only for Windows." \
        
    "      \n\n Listing and uninstalling packages:" \
    "      \n - " + Fore.CYAN + "list pip" + Fore.RESET + " : lists all pip-managed packages." \
    "      \n - " + Fore.CYAN + "uninstall pip [package]" + Fore.RESET + " : uninstalls the provided package." \
    "      \n - " + Fore.CYAN + "list apps" + Fore.RESET + " : lists all installed apps                                                                         - Works only for Windows." \
    "      \n - " + Fore.CYAN + "uninstall [package]" + Fore.RESET + " : uninstalls the provided package (if winget finds it)                                   - Works only for Windows." \
    "      \n - " + Fore.CYAN + "list" + Fore.RESET + " : runs the 'list pip' command and the 'list apps' command                                               - Works only for Windows.")
    print(Fore.CYAN + "\nNote that you can run multiple commands at once using ';' between them. You can also use '&&' for your system's default shell commands." + Fore.RESET)