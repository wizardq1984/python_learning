import mouse
from PIL import Image
from PIL import ImageGrab

im1 = Image.open()
im2 = Image.open()
im3 = Image.open()
im4 = Image.open()

im = ImageGrab.grab()
print(im.getbbox())
mo = mouse.get_position()
print(mo)
Image.register_save()

def analyseimage(gim, mim):
    if gim == min:
        return True
    else:
        return False

