score_db = {}
with open('e:/github/python_learning/guess_score.txt') as scores:
    for line in scores.readlines():
        if line[-1] == '\n':
            line = line.replace('\n', '')  # remove \n from every lines
        line = line.split(' ')
        score_db[line[0]] = line[1:]

times_db = {}
with open('e:/github/python_learning/guess_times.txt') as times:
    for user_time in times.readlines():
        if user_time[-1] == '\n':
            user_time = user_time.replace('\n', '')  # remove \n from every lines
        user_time = user_time.split(' ')
        times_db[user_time[0]] = user_time[1:]


score_final = ''
times_final = ''
for name in score_db:
    score_final += name + ' ' + ' '.join(score_db[name]) + '\n'
for names in times_db:
    times_final += names + ' ' + ' '.join(times_db[names]) + '\n'
print(score_final)
print(times_final)
with open('e:/github/python_learning/guess_score.txt', 'w') as score_result:
    score_result.write(score_final)
with open('e:/github/python_learning/guess_times.txt', 'w') as times_result:
    times_result.write(times_final)

