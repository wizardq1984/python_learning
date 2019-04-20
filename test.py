import random


def test(l):
    if l[0] + l[1] + l[2] == l[3] + l[4] + l[5] == l[6] + l[7] + l[8] == l[0] + l[3] + l[6] == l[1] + l[4] + l[7]\
            == l[2] + l[5] + l[8] == l[0] + l[4] + l[8] == l[2] + l[4] + l[6]:
        result = l[0] + l[1] + l[2]
    else:
        result = 0
    return result


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while test(test_list) == 0:
    random.shuffle(test_list)
    print(test_list)
print(test(test_list))
