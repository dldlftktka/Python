import random,os

rotto = []

for cc in range(1,8,1):
    rotto.insert(cc,random.randint(1,99))

print(rotto)

os.system('Pause')
