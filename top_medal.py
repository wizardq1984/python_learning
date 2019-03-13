class Medal:
    def __init__(self, c_name, go_num, si_num, br_num):
        self.country_name = c_name
        self.golden_num = go_num
        self.silver_num = si_num
        self.bronze_num = br_num

    def get_place(self, race_result):
        if race_result == 1:
            print('You got the Golden Medal for %s' % self.country_name)
            self.golden_num += 1
        elif race_result == 2:
            print('You got the Silver Medal for %s' % self.country_name)
            self.silver_num += 1
        elif race_result == 3:
            print('You got the Bronze Medal for %s' % self.country_name)
            self.bronze_num += 1
        else:
            print('Your race result cannot get any Medal.')

    @property
    def count(self,):
        return self.golden_num + self.silver_num + self.bronze_num

    def __str__(self):
        return '%s: Golden %d, Silver %d, Bronze %d' % (self.country_name, self.golden_num, self.silver_num, self.bronze_num)


if __name__ == '__main__':
    CN = Medal('CN', 30, 25, 20)
    US = Medal('US', 38, 30, 30)
    UK = Medal('UK', 18, 20, 17)
    print(CN)
    print(US)
    print(UK)
    print('China got 1st in Man basketball game.')
    CN.get_place(1)
    print(CN)
    medal_list = [CN, US, UK]
    # print(medal_list)
    print('Golden Metal broad:')
    sort_sum = sorted(medal_list, key=lambda x: x.golden_num, reverse=True)
    # print(sort_sum)
    for i in sort_sum:
        print(i)
    print('Total Metal broad:')
    total_sum = sorted(medal_list, key=lambda x: x.count, reverse=True)
    for j in total_sum:
        print(j)
