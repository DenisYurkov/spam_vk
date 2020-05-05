"""
Программа для спама в vk.
Beta 2.0.
Автор: Денис Юрков.
"""

import pyautogui as pg

# Настройка и подготовка к спаму.
# Включает отказоустойчивый режим.
# Перемещение мышь в верхний левый угол вызовет, pyautogui.FailSafeException который может прервать вашу программу.
protection = pg.FAILSAFE = True

pg.hotkey("winleft")
pg.typewrite("chrome\n", 0.3)

pg.hotkey("winleft", "up")
pg.typewrite("vk.com/im\n", 0.1)
pg.moveTo(752, 183, 0.1)
pg.click()

# Оступы у переменной нужно для того чтобы vk правильно ввело имя и фамалию не пропуская буквы.
name_surname = "       Denis Yurkov\n"
pg.typewrite(str(name_surname), 0.6)

# Запуск цикла и настройка спама.
while True:
    pg.typewrite("test\n", 0.1)

    # обход капчи.
    pg.moveTo(832, 470, 0.5)
    pg.click()

    pg.moveTo(1067, 497, 0.5)
    pg.click()

    pg.moveTo(824, 528, 0.5)
    pg.click()

    pg.moveTo(1101, 390, 0.5)
    pg.click()
