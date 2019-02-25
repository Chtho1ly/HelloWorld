from random import randint

flag = True
while flag:
    sum = 0
    message = input('Enter 1 to wager on large and enter anything else for the other side.')
    if message == '1':
        big = True
        print('You chose large.')
    else:
        big = False
        print('You chose small.')
    time = int(input('How many times would you like to roll?'))
    for i in range(1, time+1):
        dice = randint(1, 6)
        print(str(i) + ': ' + str(dice))
        sum += dice
    average = sum / time
    print('Average: ' + str(average))
    if (average > 3.5) == big:
        print('You win, congratulation!')
    else:
        print('Unfortunately, you lost.')
    message = input('Enter \'y\' to continue.')
    if message != 'y':
        flag = False
