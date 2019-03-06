import random

score_db = {}
with open('e:/github/python_learning/txt/guess_score.txt') as scores:
    for line in scores.readlines():
        if line[-1] == '\n':
            line = line.replace('\n', '')  # remove \n from every lines
        line = line.split(' ')
        score_db[line[0]] = line[1:]

times_db = {}
with open('e:/github/python_learning/txt/guess_times.txt') as times:
    for user_time in times.readlines():
        if user_time[-1] == '\n':
            user_time = user_time.replace('\n', '')  # remove \n from every lines
        user_time = user_time.split(' ')
        times_db[user_time[0]] = user_time[1:]

print('Welcome! This is a simple guess number game.')
user_name = input('Input your name to start(only english allowed):')
user_score_list = []
if user_name not in score_db:   # if user name  not in file create data 0, 0, 0
    score_db[user_name] = ['10', '0', '0']
user_score_list = score_db[user_name]
min_time = int(user_score_list[0])
avg_time = float(user_score_list[1])
total_time = int(user_score_list[2])


user_time_list = []
if user_name not in times_db:    # if user name not in times.txt create empty list
    times_db[user_name] = []
user_time_list = times_db[user_name]


def ave_list(str_list):
    sum = 0
    if len(str_list) == 0:  # in case of new user's time list is empty
        ave = 0
    else:
        for i in str_list:
            sum += int(i)
        ave = sum/len(str_list)
    return ave


def list_min(str_list):
    min_list = []
    for i in str_list:
        min_list.append(int(i))
    return min(min_list)


again = 'y'
while again == 'y':
    com = random.randint(1, 99)
    current_time = 0
    total_time += 1
    ave_time = ave_list(user_time_list)
    print('\n\nI already choose 1 number which is between 1 to 99,\nYou have 8 chances to guess that number.')
    print('You are play this game for total %d time.' % total_time)
    print('Your average success time is %.2f and shortest success time is %d.' % (ave_time, min_time))
    for i in range(1, 9):
        if i < 8:
            ans = eval(input('Guess what i think:'))
            if ans < com:
                print('The number is too small.')
                print('You already try for %d times,%d times remaining.' % (i, 8-i))
            elif ans > com:
                print('The number is too big.')
                print('You already try for %d times,%d times remaining.' % (i, 8-i))
            else:
                print('You are right!\n')
                current_time = i
                user_time_list.append(str(current_time))
                user_score_list[0] = str(list_min(user_time_list))
                user_score_list[1] = str(ave_time)
                user_score_list[2] = str(total_time)
                break
        else:
            ans = eval(input('This is your last chance!\nGuess what i think:'))
            if ans == com:
                print('You are right!\n')
                current_time = i
                user_time_list.append(str(current_time))
                user_score_list[0] = str(list_min(user_time_list))
                user_score_list[1] = str(ave_time)
                user_score_list[2] = str(total_time)
            else:
                print('8 times running out, game is over.My number is %d.\n' % com)
                user_score_list[2] = str(total_time)
    score_db[user_name] = user_score_list
    times_db[user_name] = user_time_list
    again = input('%s, Do you want to try again?(Y or N):' % user_name).lower()


# output all result to txt file.
score_final = ''
times_final = ''
for name in score_db:
    score_final += name + ' ' + ' '.join(score_db[name]) + '\n'
for names in times_db:
    times_final += names + ' ' + ' '.join(times_db[names]) + '\n'
with open('e:/github/python_learning/txt/guess_score.txt', 'w') as score_result:
    score_result.write(score_final)
with open('e:/github/python_learning/txt/guess_times.txt', 'w') as times_result:
    times_result.write(times_final)
