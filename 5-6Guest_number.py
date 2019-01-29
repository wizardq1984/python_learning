#Guest number game
import random
again = 'Y'
count = 0  #游戏进行了多少次
sucess = 0  #猜中时的论数

while again == 'Y':
    com = random.randint(1,100)
    count +=1
    print('\n\nI already choose 1 number which is between 1 to 100,\nYou have 10 chances to guess that number.')
    print('You are currently play this game for %d time.'%count)
    for i in range(1,11):
        if i < 10:
            ans = eval(input('Guess what i think:'))
            if ans < com:
                print('The number is too small.')
                print('You alreay try for %d times,%d times remaining.'%(i,10-i))
            elif ans > com:
                print('The number is too big.')
                print('You alreay try for %d times,%d times remaining.'%(i,10-i))
            else:
                print('You are right!\n')
                sucess = i
                break
        elif i == 10:
            ans = eval(input('This is your last chance!\nGuess what i think:'))
            if ans == com:
                print('You are right!\n')
                sucess = i
            else:
                print('10 times running out, game is over.My number is %d.\n'%com)
                #again = input('Do you want to start again?(Y or N):')
            
        else:
            print('10 times running out, game is over.My number is %d.\n'%com)
            #again = input('Do you want to start again?(Y or N):')
    print('Your average sucess time is %.2f.'%(sucess/count))
    again = input('Do you want to start again?(Y or N):')
