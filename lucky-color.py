import random
def guess_lucky_color():
    colors = ['red','blue', 'green','purple', 'yellow']
    lucky_color = random.choice(colors)
    for i in range(3):
        print ('There are {} colors' .format(colors))
        guess = input ('Guess Your Lucky Color: ')
        if guess != lucky_color:
            colors.remove(guess)
            print ('Seems like {} is not your lucky color \n' .format(guess))
        else:
            break
    if guess == lucky_color:
        print ('Great {} is your lucky color' .format(lucky_color))
    else:
        print ('Actually {} is your lucky color' .format(lucky_color))

guess_lucky_color()