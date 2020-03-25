import pyautogui as mouse
import os

try:
    while True:         # 연속 실행 x ,y 좌표와 rgb 반환
        x, y = mouse.position()
        RGB = mouse.screenshot().getpixel((x,y))
        print('RGB={}        '.format(RGB), end='\r')

except KeyboardInterrupt:           # 인터럽
    print('x: {}, y:{}, RGB={}     '.format(RGB))
    print("\b\bCtrl + C를 눌러서 프로그램을 종료")
    os.system('Pause')

    
