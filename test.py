from PIL import Image
import time
import mouse

print('Get ready will start after 5 Secs')
time.sleep(5)
print('before', mouse.get_position())
time.sleep(2)
print('after', mouse.get_position())

