import random


# Generate count number of random numbers from [start to end]
def generate_random_numbers_in_range(start, end, count):
    ran = list(range(start, end + 1))
    random.shuffle(ran)
    return ran[:count]


def prepare_bingo_game():
    # Generate 24 random numbers in respective ranges ( middle box is empty )

    first_col = generate_random_numbers_in_range(1, 15, 5)
    second_col = generate_random_numbers_in_range(16, 30, 5)

    # make 13th element as empty *
    third_col = generate_random_numbers_in_range(31, 45, 4)
    third_col = third_col[:2] + ['*'] + third_col[2:]

    fourth_col = generate_random_numbers_in_range(46, 60, 5)
    fifth_col = generate_random_numbers_in_range(61, 75, 5)

    # Add all the columns to the bingo list
    bingo_list = first_col + second_col + third_col + fourth_col + fifth_col
    return bingo_list


def play():
    bingo_list = prepare_bingo_game()
    balls = list(range(1, 76))
    random.shuffle(balls)
    draw_list = [0] * 25
    draw_list[12] = 1  # 13th is FREE
    count = 1
    tries = 0
    current = 0
    while count < 25:
        ball_drawn = balls.pop()
        if 1 <= ball_drawn <= 15:
            type = 'B'
        elif 16 <= ball_drawn <= 30:
            type = 'I'
        elif 31 <= ball_drawn <= 45:
            type = 'N'
        elif 46 <= ball_drawn <= 60:
            type = 'G'
        else:
            type = 'O'
        print('Ball drawn: ', type, ball_drawn,sep='')

        if ball_drawn in bingo_list:
            count += 1
            ind = bingo_list.index(ball_drawn)
            draw_list[ind] = 1
        tries += 1
        print(bingo_list)
        print(draw_list)
    print('It took ',tries,' balls to get bingo!')
play()

