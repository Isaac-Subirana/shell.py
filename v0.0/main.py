from subprocess import run as subprocess_run

command = ""

def run():
    command = input("\n> ")
    isnotexit(command)
    try:
        subprocess_run(command)
        run()
        command = input("\n> ")
    except FileNotFoundError:
        print("Error: Your system does not recognize the command you tried to run.")
        run()
        command = input("\n> ")

def isnotexit(command):
    if command.lower() == "exit":
        exit()


def main():
    print("Basic shell in Python.\nVersion 0.0")
    #It's version 0.0 because it does nothing on its own and just calls the system shell for all commands.
    run()

main()
