import random

score_db = {}
with open('e:/github/python_learning/guess_score.txt') as scores:
    for line in scores.readlines():
        if line[-1] == '\n':
            line = line.replace('\n', '')  # remove \n from every lines
        line = line.split(' ')
        score_db[line[0]] = line[1:]
    print(score_db)  # test output score_db

times_db = {}
with open('e:/github/python_learning/guess_times.txt') as times:
    for user_time in times.readlines():
        if user_time[-1] == '\n':
            user_time = user_time.replace('\n', '')  # remove \n from every lines
        user_time = user_time.split(' ')
        times_db[user_time[0]] = user_time[1:]
    print(times_db)  # test output times_db

user_name = input('Please input your name:')
if user_name not in score_db:   # if user name  not in file create data 0, 0, 0
    score_db[user_name] = [0, 0, 0]
min_time = int(score_db[user_name][0])
avg_time = float(score_db[user_name][1])
total_time = int(score_db[user_name][2])

if user_name not in times_db:    # if user name not in times.txt create empty list
    times_db[user_name] = []
current_time = 0


def ave_list(str_list):
    sum = 0
    for i in str_list:
        sum += int(i)
    ave = sum/len(str_list)
    return ave


again = 'Y'
while again == 'Y':
    com = random.randint(1, 100)
    current_time += 1
    ave_time = ave_list(times_db[user_name])
    print('\n\nI already choose 1 number which is between 1 to 99,\nYou have 10 chances to guess that number.')
    print('You are play this game for total %d time.' % total_time)
    print('Your average success time is %.2f and shortest success time is %d.' % (ave_time, min_time))
    for i in range(1, 11):
        if i < 10:
            ans = eval(input('Guess what i think:'))
            if ans < com:
                print('The number is too small.')
                print('You already try for %d times,%d times remaining.' % (i, 10-i))
            elif ans > com:
                print('The number is too big.')
                print('You already try for %d times,%d times remaining.' % (i, 10-i))
            else:
                print('You are right!\n')
                current_time = i
                times_db[user_name] = times_db[user_name].append(current_time)
                break
        elif i == 10:
            ans = eval(input('This is your last chance!\nGuess what i think:'))
            if ans == com:
                print('You are right!\n')
                current_time = i
            else:
                print('10 times running out, game is over.My number is %d.\n' % com)
            
        else:
            print('10 times running out, game is over.My number is %d.\n' % com)
    print('Your average success time is %.2f.' % (success/count))
    again = input('Do you want to start again?(Y or N):')
