array=[]
count = 1
calorie = 0
calorie_set = 2600

print("입력 제한: 밥, 고기, 라면, 부대찌개, 김치")
print("총합은 0을 누르면 나옴")

while True:
    string = input("입력 ")
    if string == "밥":
        calorie = 300
        array.append(calorie)
        calorie = calorie + 1
    if string == "고기":
        calorie = 200
        array.append(calorie)
        calorie = calorie + 1
    if string == "라면":
        calorie = 450
        array.append(calorie)
        calorie = calorie + 1
    if string == "부대찌개":
        calorie = 340
        array.append(calorie)
        calorie = calorie + 1
    if string == "김치":
        calorie = 33
        array.append(calorie)
        calorie = calorie + 1
    elif string == "0":
        break


final_calorie = 2600 - sum(array, 0.0)
print("총량 : %dkcal" % final_calorie)
