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
while gem != 0:
    gem_im = Image.open('D:/Arknights/PIC/gem.jpg')
    box = (0, 0, 0, 0)  # confirm GEM window or not
    gem_p = ImageGrab.grab(box)
    gem_p.save('D:/Arknights/PIC/gem_p.jpg')
    if equal_im(gem_p, gem_im) is True:
        mouse.move(0,0)
        mouse.click(button='left')
        gem = gem - 1
        time.sleep(2)

    else:


    prts_im = Image.open('D:/Arknights/PIC/prts.jpg')
    time.sleep(5)
    box = (2118, 1248, 2149, 1279)  # confirm PRTS option is checked
    prts_p = ImageGrab.grab(box)
    prts_p.save('D:/Arknights/PIC/prts_p.jpg')
    if equal_im(prts_p, prts_im) is False:
        mouse.move(1070, 630)
        mouse.click(button='left')
        print(equal_im(prts, prts_im))
    else:
        mouse.move(mouse_p[0], mouse_p[1] + 60)




