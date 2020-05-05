"""
Программа для спама в vk.
Bta 1.0.
Автор: Денис Юрков.
"""

import pyautogui as pg

# Настройка и подготовка к спаму.

# Включает отказоустойчивый режим.
# Перемещение мышь в верхний левый угол вызовет, pyautogui.FailSafeException который может прервать вашу программу.
protection = pg.FAILSAFE = True

pg.hotkey("winleft")
pg.typewrite("chrome\n", 0.5)

pg.hotkey("winleft", "up")
pg.typewrite("vk.com/im\n")
pg.moveTo(752, 183, 0.5)
pg.click()

pg.typewrite("Denis Yurkov", 0.5)
pg.press("enter")

# Запуск цикла и настройка спама.
while True:
    pg.typewrite("test", 0.3)
    pg.press("enter")
