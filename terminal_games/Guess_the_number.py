from random import randint


def guess_the_number():

    print("""
    This is guess the number game.
    Rules are simple :
    * Computer Draws Number
    * You write you number
    * You can't write anything else then a number
    * Computer checking your number
    """)

#  Computer draw a number

    random_num = randint(1, 100)

#  Main part of game
    while True:
        number = input("Guess the number: ")

        try:
            number = int(number)
        except ValueError:
            print("It's not a number!")
            continue

        if number < random_num:
            print("Too small!")
        elif number > random_num:
            print("To big!")
        else:
            print("You win")
            break


if __name__ == "__main__":
    guess_the_number()

