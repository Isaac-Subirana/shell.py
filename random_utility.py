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
    print(Fore.YELLOW + " \nWelcome to the random generator utility!\n What do you want to do?\n")
    print(" 1. Roll a dice. \n 2. Toss a coin. \n 3. Generate a random integer between two given numbers. \n 4. Generate a random choice from a given list. \n\n Q. Quit this utility but stay in the shell. \n E. Completely exit the shell." + Fore.RESET)
    inp = input(Fore.YELLOW + "\n random > " + Fore.RESET).lower()
    if "1" in inp:
        print(f"\n Your number has turned out to be a {dice()}!")
        random_utility_main()
    elif "2" in inp:
        print(f"\n Your coin toss has come up {coin()}!")
        random_utility_main()
    elif "3" in inp:
        try:
            minvalue = int(input(" From: "))
            try:
                maxvalue = int(input(" To: "))
                print(f"\n Your number has turned out to be {random_number(minvalue, maxvalue)}")
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
            print(f"\n Your list's random item is '{random_choice(l)}'!")
            random_utility_main()
        except ValueError:
            print(Fore.RED + "\n You are supposed to input a number!" + Fore.RESET)
            random_utility_main()
    elif "quit" == inp.lower() or "q" == inp[0].lower():
        pass
    elif "exit" == inp.lower() or "e" == inp[0].lower():
        exit()
    else: 
        print(Fore.YELLOW + "\n Sorry, this option does not exist (yet!)." + Fore.RESET)