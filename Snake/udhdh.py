import pyautogui as pg
import time

time.sleep(10)
pg.write("FUCK")
pg.press("Enter")

pg.scroll(-500)FUCK
pg.rightClick(100,100)
print(pg.position())