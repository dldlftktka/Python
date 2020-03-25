import random
import os


stop = 0
bab=[0]
print("0 입력하면 결과 출력 및 종료")

while True : 
    bab.append(str(input("밥 선택지: ")))
    stop = stop+1
    if bab[stop] == "0" :
        stop =  random.randrange(0,stop-1)
        break
print("선택된 밥: %s" % bab[stop]) 
os.system("Pause")
