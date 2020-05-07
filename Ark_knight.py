import mouse
import time
from PIL import Image
from PIL import ImageGrab


def equal_im(grab_im, main_im):
    gimc = grab_im.getcolors()
    gimcl = []
    for i in gimc:
        gimcl.append(i[1])
    mimc = main_im.getcolors()
    mimcl = []
    for j in mimc:
        mimcl.append(j[1])
    print('Grab image color is:', gimcl)
    print('Main image color is:', mimcl)
    if gimcl == mimcl:
        return True
    else:
        return False


gem = int(input('How many GEMs you want to use:'))
print('Please get game window ready!')
print('The process will start after 5 Secs.')
time.sleep(5)
battle_count = 0

while True:
    prts_im = Image.open('D:/Arknights/PIC/prts.jpg')
    prts_box = (2118, 1333, 2148, 1357)  # confirm PRTS option is checked
    prts_p = ImageGrab.grab(prts_box)
    prts_p.save('D:/Arknights/PIC/prts_p.jpg')
    print('start process PRTS window')
    if equal_im(prts_p, prts_im) is False:
        print('PRTS image is not same')
        mouse.move(1070, 670)
        mouse.click(button='left')
        time.sleep(3)
    else:
        print('PRTS image is same')

    start_im = Image.open('D:/Arknights/PIC/start.jpg')
    start_box = (2530, 260, 2540, 270)
    start_p = ImageGrab.grab(start_box)
    start_p.save('D:/Arknights/PIC/start_p.jpg')
    print('start process Start window')
    if equal_im(start_p, start_im) is True:
        print('Start image is same')
        mouse.move(1100, 720)
        mouse.click(button='left')
        time.sleep(3)
    else:
        print('Start image is not same')
        break

    gem_im = Image.open('D:/Arknights/PIC/gem.jpg')
    gem_box = (2160, 1205, 2175, 1220)
    gem_p = ImageGrab.grab(gem_box)
    gem_p.save('D:/Arknights/PIC/gem_p.jpg')
    print('Start process Gem window')
    if equal_im(gem_p, gem_im) is True and gem != 0:
        print('Gem image is same.')
        mouse.move(1082, 610)
        mouse.click(button='left')
        gem -= 1
        time.sleep(2)
        mouse.move(1100, 720)
        mouse.click(button='left')
        time.sleep(2)
    elif equal_im(gem_p, gem_im) is True and gem == 0:
        print('Gem = 0, end of whole process.')
        break

    team_im = Image.open('D:/Arknights/PIC/team.jpg')
    team_box = (2300, 820, 2320, 840)
    team_p = ImageGrab.grab(team_box)
    team_p.save('D:/Arknights/PIC/team_p.jpg')
    print('start process team window')
    if equal_im(team_p, team_im) is True:
        print('team image is same')
        mouse.move(1100, 520)
        mouse.click(button='left')
        time.sleep(3)
    else:
        print('team image is not same')
        break

    result_im = Image.open('D:/Arknights/PIC/result.jpg')
    result_box = (115, 1480, 120, 1485)
    result_p = ImageGrab.grab(result_box)
    result_p.save('D:/Arknights/PIC/result_p.jpg')
    print('start process battle window')
    while equal_im(result_p, result_im) is False:
        print('result image is not same')
        result_p = ImageGrab.grab(result_box)
        time.sleep(4)
    print('result image is same')
    mouse.move(980, 560)
    mouse.click(button='left')
    battle_count += 1
    time.sleep(5)

print('Work is done, battle count is:', battle_count)





