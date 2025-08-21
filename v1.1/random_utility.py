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

def wait():
    input("\n---------- Press ENTER to go back to the random utility menu ----------")
    random_utility_main()

def random_utility_main():
    print(" \nWelcome to the random generator utility!\n What do you want to do?\n")
    print(" 1. Roll a dice \n 2. Toss a coin \n 3. Generate a random number between two given numbers \n 4. Generate a random choice from a given list \n\n Q. Quit this utility but stay in the shell. \n E. Completely exit the shell.")
    inp = input("\n random > ").lower()
    if "1" in inp:
        print(f"\n Your number has turned out to be a {dice()}!")
        wait()
    elif "2" in inp:
        print(f"\n Your coin toss has come up {coin()}!")
        wait()
    elif "3" in inp:
        try:
            minvalue = int(input(" What's the minimum your number can be? "))
            try:
                maxvalue = int(input(" What's the maximum your number can be? "))
                print(f"\n Your number has turned out to be {random_number(minvalue, maxvalue)}")
                wait()
            except ValueError:
                print("\n You are supposed to input a number!")
                wait()
        except ValueError:
            print("\n You are supposed to input a number!")
            wait()
    elif "4" in inp:
        l=[]
        try:
            length = int(input(" How many items do you want your list to have? "))
            for i in range(0, length):
                item = input(f" Input your list's item number {i+1}: ")
                l.append(item)
            print(f"\n Your list's random item is '{random_choice(l)}'!")
            wait()
        except ValueError:
            print("\n You are supposed to input a number!")
            wait()
    elif "q" in inp.lower():
        pass
    elif "e" in inp.lower():
        exit()
    else: 
        print("\n Sorry, this option does not exist (yet!).")
        wait()