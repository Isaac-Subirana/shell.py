from colorama import Fore
from random import choice, randint

def dice():
    num = randint(1, 6)
    return num

def coin():
    c = choice(["heads", "tails"])
    return c

def random_number(minvalue, maxvalue):
    num = randint(minvalue, maxvalue)
    return num

def random_choice(l):
    c = choice(l)
    return c

def random_utility_main():
    print("\nWelcome to the " + Fore.CYAN + "random generator utility!" + Fore.RESET + "\n What do you want to do?\n")
    print(Fore.CYAN + " 1. Roll" + Fore.RESET + " a dice. \n " + Fore.CYAN + "2. Toss" + Fore.RESET + " a coin. \n" + Fore.CYAN + " 3. Generate a random integer" + Fore.RESET + " between two given numbers. \n" + Fore.CYAN + " 4. Generate a random choice" + Fore.RESET + " from a given list. \n\n " + Fore.CYAN + "Q. Quit " + Fore.RESET + "this utility but stay in the shell. \n" + Fore.CYAN + " E." + Fore.RESET + " Completely " + Fore.CYAN + "exit" + Fore.RESET + " the shell." + Fore.RESET)
    inp = input(Fore.CYAN + "\n random > " + Fore.RESET).lower()
    if "1" in inp:
        print("\n Your number has turned out to be a" + Fore.CYAN + f"'{dice()}'" + Fore.RESET + "!")
        random_utility_main()
    elif "2" in inp:
        print("\n Your coin toss has come up " + Fore.CYAN + f"'{coin()}'" + Fore.RESET + "!")
        random_utility_main()
    elif "3" in inp:
        try:
            minvalue = int(input(" From: "))
            try:
                maxvalue = int(input(" To: "))
                print("\n Your number has turned out to be" + Fore.CYAN + f"'{random_number(minvalue, maxvalue)}'" + Fore.RESET)
                random_utility_main()
            except ValueError:
                print(Fore.RED + "\n You are supposed to input a number!" + Fore.RESET)
                random_utility_main()
        except ValueError:
            print(Fore.RED + "\n You are supposed to input a number!" + Fore.RESET)
            random_utility_main()
    elif "4" in inp:
        l=[]
        try:
            length = int(input(" How many items do you want your list to have? "))
            for i in range(0, length):
                item = input(f" Input your list's item number {i+1}: ")
                l.append(item)
            print("\n Your list's random item is " + Fore.CYAN + f"'{random_choice(l)}'" + Fore.RESET + "!")
            random_utility_main()
        except ValueError:
            print(Fore.RED + "\n You are supposed to input a number!" + Fore.RESET)
            random_utility_main()
    elif "quit" == inp.lower() or "q" == inp[0].lower():
        pass
    elif "exit" == inp.lower() or "e" == inp[0].lower():
        exit()
    else: 
        print(Fore.CYAN + "\n Sorry, this option does not exist (yet!)." + Fore.RESET)