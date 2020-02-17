import random as rd

z = 1 # 기본 최솟값
y = 46 # 기본 최댓값
j = 0 # 랜덤 변수
n = 0 # 출력 값의 길이
count = 0 # 카운터
k = 0 # 중복 확인 변수
m = 45 # 중복 확인 변수 2

arr = [] # 1~45까지 넣은 배열 값
arr1 = [] # 카피 버전
arr2 = []  # 랜덤 값
arr3 = []  # 출력 값

for i in range(z,y):
    arr.append(i)

arr1 = arr

while count < 5:
    while (True):
        j = rd.randrange(z,y)
        arr2.append(j)
        arr2 = list(set(arr2))

        arr1 = list(set(arr1) - set(arr2))
        k = len(arr1)

        if m != k:
            arr3.append(arr2)
            m =  m-1
        else:
            pass

        n = len(arr3)
        arr2 = []
        
        if n == 5:
            break
        
    print(arr3)
    arr3 = []
    count = count + 1

