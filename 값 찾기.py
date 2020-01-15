'''
def find_2(lst, key):
    found = "검색 실패"
    count = 0
    for value in lst:
        if key in lst:
            found = "검색 성공"
            return found,count+1
    return found,count
'''
lst = []
for i in range(0,10):
    lst.append(input("입력: "))
'''
add()
key=input("검색: ")
print("목록: " , lst)
print(find(lst,key))
'''
def find_1(lst,key):
    found = "검색 실패"
    count = 0
    for value in lst:
        if key in lst:
            place = lst.index(key)
            found = "검색 성공"
            return found,place+1
    return found,place+1

key=input("검색: ")
print("목록: " , lst)
print(find_1(lst,key))


