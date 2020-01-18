import subprocess as s
import pyautogui as pg 
import time
path_chrom = "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
#s.Popen(path_chrom)
s.Popen('mspaint.exe')
time.sleep(2)
pg.hotkey('win','up')

pg.press('alt')
pg.press('f')
pg.press('e')
time.sleep(1)
pg.typewrite("1000")
pg.press('tab')
pg.typewrite("500")
pg.press("enter")

import random
a = random.randint(5,5+1000)
b = random.randint(212,212+500)
pg.moveTo(a,b)
for i in range (100):
    print('Line : ',i)
    x = random.randint(5,5+1000)
    y = random.randint(212,212+500)
    pg.dragTo(x,y,button='left')

#5,212
