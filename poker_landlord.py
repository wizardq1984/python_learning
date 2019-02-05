import random
card_color = ['H', 'D', 'C', 'S']  # H Hearts, D Diamonds, C Clubs, S Spades
card_num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_joker = ['Big Joker', 'Little Joker']
card52 = [x+y for x in card_color for y in card_num]  # 生成52张扑克牌
card_full = card52 + card_joker
random.shuffle(card_full)  # 洗牌


def generate_card(x):
    player_card = []
    for i in range(x, 51, 3):  # 从第x张开始，每隔3张要一张
        player_card.append(card_full[i])
    return ','.join(player_card)


player1 = generate_card(0)  # 从第一张牌开始要
player2 = generate_card(1)  # 从第二张牌开始要
player3 = generate_card(2)  # 从第三张牌开始要
other_card = ',' + ','.join(card_full[51:])  # 底牌前加逗号，隔开地主牌最后一张和底牌第一张之间
print('Send card complete, card remain is:', other_card)
print('Who want to be the landlord?')
landlord = int(input('1 for player1\n2 for player2\n3 for player3'))
while landlord > 3:
    landlord = int(input('Please input number between 1 -3:'))
if landlord == 1:
    player1 += other_card
    print('Player1 is the landlord!')
elif landlord == 2:
    player2 += other_card
    print('Player2 is the landlord!')
else:
    player3 += other_card
    print('Player3 is the landlord!')

print('Player1 card:', player1)
print('Player2 card:', player2)
print('Player3 card:', player3)

