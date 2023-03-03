
def guess_the_number_reverse():
    """
    :rtype: str
    :return: if user not cheating :) = user number
    """

    print("""
        This is guess the number game - - - reverse.
        Rules are simple :
        * Enter your number in range 1 to 1000
        * Then computer try to figure out what it's your number in max. 10 moves
        * You answer computer:
            * Too small
            * Too Big
            * You win
        """)

    while True:
        number = input("Enter your number in range of 1 to 1000: ")
        try:
            number = int(number)
            if number not in range(1, 1000):
                print("Number out of range")
                continue
            else:
                break
        except ValueError:
            print("It's not a number!")

    min_value = 1
    max_value = 1000
    guess = 500
    while True:
        print(f'My typing is {guess}')
        user_answer = input('Enter answer: ').lower()
        answers = ['too small', 'too big', 'you win']

        if user_answer in answers:
            if user_answer == answers[0]:
                min_value = guess
                guess = (max_value - min_value) // 2 + min_value
                if min_value > number:
                    print('Cheater!')
                    break

            elif user_answer == answers[1]:
                max_value = guess
                guess = (max_value - min_value) // 2 + min_value
                if max_value < number:
                    print('Cheater!')
                    break

            else:
                print('I know that i win, ha!')
                break

        else:
            print("Answer out of possible")
            continue


if __name__ == "__main__":
    guess_the_number_reverse()