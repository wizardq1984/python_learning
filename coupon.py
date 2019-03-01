import random
import string


def coupletter():
    letter_list = [x for x in string.ascii_letters]
    random.shuffle(letter_list)
    coup = ''.join(letter_list[:8])
    return coup


couplist = []
while len(couplist) < 200:
    coup1 = coupletter()
    if coup1 in couplist:
        coup1 = coupletter()
    else:
        couplist.append(coup1)
print(couplist)
print('coupon number is:', len(couplist))

