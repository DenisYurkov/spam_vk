"""
Программа для спама в vk.
Beta 3.0.
Автор: Денис Юрков.
"""

import pyautogui as pg

# Настройка и подготовка к спаму.


def bypass_captcha():
    """Обход капчи."""

    # Скорость капчи.
    speed_captcha = 0.3

    pg.moveTo(832, 470, speed_captcha)
    pg.click()

    pg.moveTo(1067, 497, speed_captcha)
    pg.click()

    pg.moveTo(824, 528, speed_captcha)
    pg.click()

    pg.moveTo(1135, 400, speed_captcha)
    pg.click()


# Включает отказоустойчивый режим.
# Перемещение мышь в верхний левый угол вызовет, pyautogui.FailSafeException который может прервать вашу программу.
protection = pg.FAILSAFE = True

pg.hotkey("winleft")
pg.PAUSE = 0.5
pg.typewrite("chrome\n", 0.3)

pg.hotkey("winleft", "up")
pg.typewrite("vk.com/im\n", 0.1)
pg.moveTo(752, 183, 0.1)
pg.click()

# Оступы у переменной нужно для того чтобы vk правильно ввело имя и фамалию не пропуская буквы.
name_surname = "       Denis Yurkov\n"
pg.typewrite(str(name_surname), 0.6)

# Запуск цикла и настройка спама.
check = 0
while True:
    pg.typewrite("test\n", 0.1)

    check += 1
    if check == 3:
        # запуск обхода капчи.
        bypass_captcha()
        check = 0
