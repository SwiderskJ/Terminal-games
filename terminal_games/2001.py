from random import randint


def dice(type_of_dices):
    """
    :parameter: type of throwing dices
    :rtype: int
    :return: sum of throwing 2 times dices d6
    """
    result = 0
    for item in range(2):
        result += randint(1, type_of_dices)
    return result


def game():
    print("""
        Simple game about achieve 2001 point.
        * First player toss a dices chosen by user two times.
        * Next computer toss a dices chosen by user two times too.
        Rules:
        * If result of toss is 7, then actual points divided by this number.
        * If result of toss is 11, then actual points are multiplication by this number.
        
          """)

    while True:
        type_of_dice = input('''
            Chose the dice between:
            D3 => Enter 3
            D4 => Enter 4
            D6 => Enter 6
            D8 => Enter 8
            D10 => Enter 10 
            D12 => Enter 12
            D20 => Enter 20
            D100 => Enter 100
            Enter your choice:  ''')
        try:
            type_of_dice = int(type_of_dice)
            if type_of_dice not in [3, 4, 6, 8, 10, 12, 100]:
                print("There's no that type of Dice!")
                continue
            else:
                break
        except ValueError:
            print("It's not a number!")

    user_points = 0
    computer_points = 0

    while True:
        if user_points >= 2001 and computer_points >= 2001:
            print(f'''
                It's a draw!
                User {user_points} points!
                Computer {computer_points} points! 
                                ''')
            break
        elif user_points >= 2001:
            print(f'''
                User wins with {user_points} points!
                Computer {computer_points} points! 
            ''')
            break
        elif computer_points >= 2001:
            print(f'''
                Computer wins with {computer_points} points!
                User {user_points} points!
                ''')
            break
        else:
            user_toss = dice(type_of_dice)
            computer_toss = dice(type_of_dice)
            user_break = input("Push enter to toss")
            print(f'You toss {user_toss}!')
            print(f'Computer toss {computer_toss}!')
            if user_toss == 7:
                user_points = user_points // user_toss
                print(f'Your points dived by 7 now you have: {user_points}.')
            elif user_toss == 11:
                user_points = user_points * user_toss
                print(f'Your points multiplied by 11 now you have: {user_points}.')
            else:
                user_points += user_toss
                print(f"Your toss added to your point's now you have {user_points}.")

            if computer_toss == 7:
                computer_points = computer_points // computer_toss
                print(f'computer points dived by 7 now you have: {computer_points}.')
            elif computer_toss == 11:
                computer_points = computer_points * computer_toss
                print(f'computer points multiplied by 11 now you have: {computer_points}.')
            else:
                computer_points += computer_toss
                print(f"Your toss added to your point's now you have {computer_points}.")


if __name__ == "__main__":
    game()
