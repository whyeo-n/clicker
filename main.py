# main.py

import time
import random

import pyautogui as gui


width, height = gui.size()

x_center, y_center = width//2, height//2

x_min = x_center - x_center//2
x_max = x_center + x_center//2
y_min = y_center - y_center//2
y_max = y_center + y_center//2



if __name__ == '__main__':
    limit = input('얼마나? (분):')

    if limit == None:
        limit == 20
        print('기본값 20분으로 설정되었습니다.')

    else: 
        limit = int(limit)
        print(f'{limit}분으로 설정되었습니다.')

    time.sleep(3)
    
    # center로 init
    past = 0
    gui.moveTo(x_center, y_center, duration=.5)
    
    while past < limit :
        time.sleep(57.5)
        past += 1
        print(f'{past}분이 지났습니다.')

        for i in range(5):
            x_cor = random.randint(x_min, x_max)
            y_cor  = random.randint(y_min, y_max)
            gui.moveTo(x_cor, y_cor, duration=.5)
            gui.click()

    print('완료되었습니다.')