import pyautogui as op
import random, time, pyperclip  

def click():            # 2초 쉬고 클릭
    time.sleep(2)
    op.click()
def double_click():
    time.sleep(2)
    op.doubleClick()
def keyboard(w):    # 오늘 몇개 했는지..?
    time.sleep(1)
    pyperclip.copy('상시 진행중 / 총 ')
    hk_v()
    op.typewrite(w)
    pyperclip.copy('개 답변')
    hk_v()
def move(x, y):         # 정해진 좌표값으로 이동
    op.moveTo(x,y, duration = 0.5)
def mv_drive():
    move(25,25)         # 드라이브
    click()
def hk_c():
    op.hotkey("ctrl","c")       # 복사
def hk_v():
    op.hotkey("ctrl","v")       # 붙여넣기
def today():                        # 오늘 날짜
    td = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    pyperclip.copy(td)


td_w = input("오늘 한 갯수: ")
mv_drive()         # 드라이브 이동

move(350,539)       # 사본
double_click()

move(200,190)       # 확대 축소율
time.sleep(4)
click()


move(183,254)       # 75%
click()

move(665,360)       # 글 넣는 곳
click()

op.press('backspace')        # 삭제
double_click()
keyboard(td_w)          # 타이핑
move(145,295)           # 드래그 상단
click()
op.keyDown('shift')     # 쉬프트 꾹 누르기
move(725,600)           # 드래그 하단
click()
op.keyUp('shift')           # 쉬프트 뗌
hk_c()                         # 복사

mv_drive()         # 드라이브 이동

move(812,127)   # 구글 앱
click()

move(820,217)  # 지메일
click()

move(53,207)  # 새 메일
click()
time.sleep(10)
move(478,749)  # 메일
click()
hk_v()

move(529,314)  # 메일
click()
pyperclip.copy('전직원')
hk_v()

move(580,358)       # 받는 사람 클
click()

move(475,350)
click()
pyperclip.copy('업무보고 ')
hk_v()
today()
hk_v()







