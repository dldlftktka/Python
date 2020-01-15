import random


stop = 0
bab=[0]


while True : 
    bab.append(str(input("밥 선택지: ")))
    stop = stop+1
    if bab[stop] == "0" :
        stop =  random.randrange(0,stop-1)
        break
print("선택된 밥: %s" % bab[stop]) 
