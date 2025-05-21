"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Filip Hnilica
email: filip.hnilica@gmail.com
"""
import random
from time import sleep

def genereate_unique_number():
    """
    Generates a unique 4-digit number with no repeating digits and not starting with 0.
    """
    first_digit = random.randint(1, 9)
    other_digits = random.sample(range(10), 3)
    unique_number = str(first_digit) + ''.join(map(str, other_digits))
    return int(unique_number)

def get_user_input():
    """
    Prompts the user for a 4-digit number and checks if it is valid.
    """
    while True:
        user_input = input("Enter a 4-digit number with no repeating digits: ")
        if len(user_input) == 4 and user_input.isdigit() and len(set(user_input)) == 4 and user_input[0] != '0':
            return int(user_input)
        else:
            print("Invalid input. Please try again.")

def compare_numbers(secret_number, user_number):
    """
    Compares the secret number with the user's number and returns the count of bulls and cows.
    """
    secret_str = str(secret_number)
    user_str = str(user_number)
    
    bulls = sum(s == u for s, u in zip(secret_str, user_str))
    cows = sum(min(secret_str.count(d), user_str.count(d)) for d in set(user_str)) - bulls
    
    return bulls, cows
def print_bulls_and_cows(bulls, cows):
    """
    Prints bull or bulls and cow or cows.
    """
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"Bulls: {bulls} {bull_word}, Cows: {cows} {cow_word}")

def you_win():
    """
    Prints a congratulatory message.
    """
    print(f"Congratulations! You've guessed the number in {count_attempts} attempts. You win!")
    sleep(2)
    print("Have a piece of cake!")
    sleep(2)
    print("""
                ,:/+/-
                /M/              .,-=;//;-
        .:/= ;MH/,    ,=/+%$XH@MM#@:
        -$##@+$###@H@MMM#######H:.    -/H#
    .,H@H@ X######@ -H#####@+-     -+H###@X
    .,@##H;      +XM##M/,     =%@###@X;-
    X%-  :M##########$.    .:%M###@%:
    M##H,   +H@@@$/-.  ,;$M###@%,          -
    M####M=,,---,.-%%H####M$:          ,+@##
    @##################@/.         :%H##@$-
    M###############H,         ;HM##M$=
    #################.    .=$M##M$=
    ################H..;XM##M$=          .:+
    M###################@%=           =+@MH%
    @#################M/.         =+H#X%=
    =+M###############M,      ,/X#H+:,
    .;XM###########H=   ,/X#H+:;
        .=+HM#######M+/+HM@+=.
            ,:/%XM####H/.
                ,.:=-.
        """)
    print("Thank you for playing!")

print("Welcome to the Bulls and Cows game!")
x = genereate_unique_number()
print(f"Secret number generated: {x}")  # For debugging purposes, remove in production
bulls, cows = 0, 0
count_attempts = 0
while bulls != 4:
    y = get_user_input()
    bulls, cows = compare_numbers(x, y)
    print_bulls_and_cows(bulls, cows)
    count_attempts += 1
you_win()