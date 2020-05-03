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
    print('gimcl is:', gimcl)
    print('mimcl is:', mimcl)
    if gimcl == mimcl:
        return True
    else:
        return False


gem = int(input('How many GEMs you want to use:'))
print('Please get game window ready!')
print('The process will start after 5 Secs.')
time.sleep(5)
prts_im = Image.open('D:/Arknights/PIC/gem.jpg')
box = (2118, 1333, 2148, 1357)
prts_p = ImageGrab.grab(box)
prts_p.save('D:/Arknights/PIC/gem_p.jpg')
if equal_im(prts_p, prts_im) is False:
    mouse.move(1070, 670)
    mouse.click(button='left')
    print(equal_im(prts_p, prts_im))
else:
    mouse.move(1100, 735)