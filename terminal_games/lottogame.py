from random import randint


def lotto():
    """
    :rtype: int
    :return: number of hit numbers
    """

    # draw 6 numbers
    draw_numbers = []
    while len(draw_numbers) != 6:
        number = randint(1, 49)
        if number not in draw_numbers:
            draw_numbers.append(number)

    # user input
    user_numbers = []
    while len(user_numbers) != 6:
        user_number = input("Enter number: ")

        try:
            user_number = int(user_number)
            if user_number in range(1, 49):
                if user_numbers not in user_numbers:
                    user_numbers.append(user_number)
                else:
                    print("You heave already entered this number!")
            else:
                print("Number out of range!")
                continue
        except ValueError:
            print("It's not a number!")
            continue

    draw_numbers.sort()
    user_numbers.sort()
    print(f"Draw numbers: {draw_numbers}")
    print(f"Your numbers: {user_numbers}")
    # List of hit numbers
    hit_numbers = []
    for item in user_numbers:
        if item in draw_numbers:
            hit_numbers.append(item)
    print(f'You hit {len(hit_numbers)}')
    print(f'Your hit numbers: {hit_numbers}')


if __name__ == "__main__":
    lotto()
