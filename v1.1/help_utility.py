def help_utility_main():
    print("\nAvailable commands: ")
    print("\n Built-in commands:" \
    "      \n - help : shows this help menu." \
    "      \n - system-help : shows your system's help menu." \
    "      \n - random : launches the random generator utility." \
    "      \n\n - exit / quit : exits the shell. " \
    "      \n\n Installing packages:" \
    "      \n - install pip [package] : installs the provided package." \
    "      \n - install pip list : installs a list of python libraries that the editor recommends." \
    "      \n - install winget [package] : installs the provided package                                        - Works only for Windows." \
    "      \n - install winget list : installs a list of winget-available apps that the editor recommends       - Works only for Windows." \
    "      \n - install apt [package] : installs the provided package                                                 - Works only for Linux distros that use APT." \
    "      \n\n Updating packages:" \
    "      \n - search updates pip : shows a list of all the outdated pip libraries." \
    "      \n - update pip all : updates (interactively) all of the outdated pip libraries." \
    "      \n - update pip [target] : updates the provided package (if it isn't installed, it installs it first)." \
    "      \n\n - search updates winget : shows a list of all the outdated winget-available apps.               - Works only for Windows." \
    "      \n - update winget all : updates all of the outdated winget-available apps.                          - Works only for Windows." \
    "      \n - update winget [target] : updates the provided package.                                          - Works only for Windows." \
    "      \n\n - search updates apt : shows a list of all the outdated apt-available apps.                             - Works only for Linux distros that use APT." \
    "      \n - update apt all : updates all of the outdated apt-available apps.                                      - Works only for Linux distros that use APT." \
    "      \n - update apt [target] : updates only the provided package.                                              - Works only for Linux distros that use APT.")