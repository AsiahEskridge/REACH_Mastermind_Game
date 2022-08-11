import random
from timeit import repeat
from tkinter.tix import MAX
import requests
import time
import winsound

tic = time.perf_counter() # Start Time
frequency = 1000
duration = 2000 #ms

winsound.Beep(frequency,duration)

# Generates list of random integers
def random_numbers(max_range):
    random_numbers = []
    for i in range(4):
        random_numbers.append(random.randint(0, max_range))
    return random_numbers

def random_numbers_from_internet(max_range):
    response = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new')
    parsedResponse = response.text.split() # string array
    out = [] # int array
    for c in parsedResponse:
        out += [int(c)]

    return out

# Safely query user input and returns integer
def getUserInt(userPrompt):
    userInput = input(userPrompt)
    while True:
        try:
            num = int(userInput)
            if num < 0 or num > 7:
                raise Exception("number out of range")
            return num
        except:
            print("Invalid input. Try again")
            userInput = input(userPrompt)


player_name = input("WARNING!!!! GAME HAS COMMENCED! Enter Your Name Here: ")

# Mastermind list = variable to be put inside of the print statement.
#mastermind_list = random_numbers(7)
mastermind_list = random_numbers_from_internet(7)
print(mastermind_list)

# Master
print("--------------------------------------------------------------")
print("|                      Mastermind Game                       |")
print("\n  Welcome", player_name, ", to the Official Mastermind Game!")
print("\n To be crowned as the ultimate Mastermind Guru, dare to guess the 4-digit code.")
print("\n   Can you guess the 4-digit code in it's corresponding order?")
print("\n           Let's play and see!                       ")
print("\n        * * * Instructions! * * *                     ")
print("\n       * Guess the 4-digit number in it's corresponding order. ")
print("\n       * You have a total of 10 guesses to crack the code.")
print("\n       * Numbers may duplicate.                     ")
print("\n       * Feedback will be given in this order:       ")
print("           Correct numbers in the correct position  ")
print("           Incorrect numbers in the wrong position  ")
print("           NOTE: Duplicates count as 1 correct number or 1 incorrect number")
print("\n       ---------- Good Luck,", player_name, "! ----------\n")
print()

MAX_ATTEMPTS = 10
attempts = 0
attempts_left = MAX_ATTEMPTS 
isGameStillGoing = True
while isGameStillGoing:
    guess1 = getUserInt("First Number: ")
    guess2 = getUserInt("Second Number: ")
    guess3 = getUserInt("Third Number: ")
    guess4 = getUserInt("Fourth Number: ")
    attempts += 1

    guesses = [guess1, guess2, guess3, guess4]
    history_lst = guesses
    correct = 0  # Total guesses that are in the list , but may not be in the correct possition
    matches = 0  # Total guesses that in the list at the correct possition
    for i in range(4):
        if (guesses[i] == mastermind_list[i]):
            correct += 1
        elif (guesses[i] in mastermind_list):
            correct += 1
            matches += 1

        for i in range(4):
            if (guesses[i] == mastermind_list[i]):
                correct != 1
            elif (guesses[i] in mastermind_list):
                correct != 1
                matches != 1

    if correct == 4:
        if attempts == MAX_ATTEMPTS:
            print("\nCongratulations, ", player_name,
                  " you guessed all four numbers! It took you " +
                  str(attempts) + " attempt!\n")
        else:
            print(
                "Congratulations, you guessed all four numbers! It took you " +
                str(attempts) + " attempts!\n")

    elif attempts == MAX_ATTEMPTS:
        print("Unfortunately, you have reached your maximum amount of attempts.")
        playerIsMakingTheirMindUp = True
        while playerIsMakingTheirMindUp:
            again = input("\nDo you want to play again? [y/n]: ").lower()
            if again == 'y':
                print("\n---------- New Game ----------")
                playerIsMakingTheirMindUp = False
                attempts = 0 
            elif again == 'n':
                playerIsMakingTheirMindUp = False
                isGameStillGoing = False
            else:
                print("Invalid input")

    else:
        print("You guessed " + str(matches) + " numbers in the wrong position!")
        print("You guessed " + str(correct) + " numbers in the correct position!")
        print("Your previous guesses are: ", history_lst)

# Created for immutable integers
    def attempts_left():
        for MAX_aTTEMPTS in attempts:
            attempts_lefts = MAX_ATTEMPTS - 1
        return attempts_left
    (print("Be careful, you have", str(attempts_left), "attempts left!\n"))
    


print("\n               Thank You For Playing! See You Soon! ;) ")
print("\n        ---------- Game End ----------")

toc = time.perf_counter() #End Time

print(f"Total game time has finished in {(toc - tic)/60:0.0f} minutes {(toc - tic)%60.:0.0f} seconds")
winsound.Beep(frequency,duration)

