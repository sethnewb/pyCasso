import os
import functools
import pygetwindow as gw
import time
import pyautogui as ag
from PIL import Image, ImageGrab

ag.FAILSAFE = True

os.system('start mspaint.exe')

time.sleep(2)

pw = gw.getWindowsWithTitle('Untitled - Paint')[0]

time.sleep(2)

pw.maximize()
ag.click(x=187, y=87, clicks=1, button='left')  # open resize
time.sleep(1)
ag.click(x=222, y=156, clicks=1, button='left')  # change to pixels
time.sleep(1)
ag.click(x=74, y=267, clicks=1, button='left')  # turn off maintain ratio
time.sleep(1)
ag.click(x=244, y=192, clicks=2, button='left', interval=.2)
time.sleep(1)
ag.typewrite('715', interval=.2)  # enter height
time.sleep(1)
ag.click(x=235, y=229, clicks=2, button='left', interval=.2)
time.sleep(1)
ag.typewrite('461', interval=.2)  # enter width
time.sleep(1)
ag.click(x=155, y=452, clicks=1, button='left')


pw.resizeTo(988, 796)


im = Image.open('shiba.jpg')
im.show()
time.sleep(1)
ph = gw.getWindowsWithTitle('Photos')[0]


grey_tuple = (34, 34, 34)
ag.moveTo(1348, 322)
x_move_from = 1348
y_move_from = 322
x_start = 0
y_start = 0

while x_start == 0:
    x_tuple = ImageGrab.grab().load()[x_move_from, y_move_from]
    if grey_tuple != x_tuple:
        x_move_from = x_move_from - 1
        ag.moveTo(x_move_from, y_move_from)
    else:
        x_start = x_move_from + 3

x_move_from = 1348

while y_start == 0:
    y_tuple = ImageGrab.grab().load()[x_move_from, y_move_from]
    if grey_tuple != y_tuple:
        y_move_from = y_move_from - 1
        ag.moveTo(x_move_from, y_move_from)
    else:
        y_start = y_move_from + 3

print(x_start)
print(y_start)

# start at x 68
# pick brush at 383 136
# edit color at 860 78
# activate window 839 344
# activate red 681 463
# activate green 677 484
# activate blue 678 510
# confirm color at 302 533

start_paint_x = 68
start_paint_y = y_start


def click_paint():
    ag.click(x=839, y=344, clicks=1, button='left')


click_paint()
ag.click(x=269, y=102, clicks=1, button='left')
time.sleep(.1)
ag.moveTo(383, 136)
ag.click(x=383, y=136, clicks=1, button='left')
# get color from picture start


def choose_color(red, green, blue):
    ag.click(x=860, y=78, clicks=1, button='left')
    time.sleep(.1)
    ag.click(x=681, y=463, clicks=2, button='left', interval=.1)
    time.sleep(.1)
    ag.typewrite(str(red), interval=.1)
    ag.click(x=678, y=485, clicks=2, button='left', interval=.1)
    time.sleep(.1)
    ag.typewrite(str(green), interval=.1)
    ag.click(x=679, y=508, clicks=2, button='left', interval=.1)
    time.sleep(.1)
    ag.typewrite(str(blue), interval=.1)
    ag.click(x=302, y=533, clicks=2, button='left', interval=.1)


ag.moveTo(x_start, y_start)
x_photo = x_start
y_photo = y_start
# pic_height = 198
# pic_width = 298
pic_height = 0
pic_width = 0

# where it starts paintng in paint
x_paint = 68
y_paint = y_start

painting = True
while painting:
    if pic_width <= 298:
        color_tup = ImageGrab.grab().load()[x_photo, y_photo]
        click_paint()
        choose_color(color_tup[0], color_tup[1], color_tup[2])
        ag.moveTo(x_paint, y_paint)
        ag.click(x=x_paint, y=y_paint, clicks=1, button='left', duration=1)
        pic_width += 1
        x_photo += 1
        x_paint += 1
    elif pic_height <= 198:
        pic_width = 0
        x_photo = x_start
        x_paint = 68
        pic_height += 1
        y_photo += 1
        y_paint += 1
    else:
        painting = True


# print(ag.position())

# ag.moveTo(383, 136)
