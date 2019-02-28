times_db = {}
with open('e:/github/python_learning/guess_times.txt') as times:
    for user_time in times.readlines():
        if user_time[-1] == '\n':
            user_time = user_time.replace('\n', '')  # remove \n from every lines
        user_time = user_time.split(' ')
        times_db[user_time[0]] = user_time[1:]
    print(times_db)
