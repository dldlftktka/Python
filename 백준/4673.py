natural_number_set = set(range(1, 10001))       # set = 집합
generated_number_set= set()     

for i in range(1, 10001):
    for j in str(i):                                            # 문자로 받아들여서 각각 자리수 나옴
        i += int(j)
    generated_number_set.add(i)                 # 비어있는 집합에 추가


self_number_set = natural_number_set - generated_number_set     #set - set = 차집합

for i in sorted(self_number_set):
    print(i)

