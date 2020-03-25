import os,shutil,collections


route = "C:\\Users\\sh.Jo\\Downloads\\aa"
ar_pa = []
ar_fe = []
ar = []
count = 0
sw = 0

for (path, dir, files) in os.walk(route):                   # 하위 디렉토리에 확장자 검색
    for filename in files:
        ext = os.path.splitext(filename)[-1]        
        if ext == ".jpg":
            ar_pa.insert(count,path+"/")       # 하나 씩 배열에 차곡차곡
            ar_fe.insert(count,filename)
        elif ext == '.JPG':
            ar_pa.insert(count,path+"/")       # 하나 씩 배열에 차곡차곡
            ar_fe.insert(count,filename)
        elif ext == '.PNG':
            ar_pa.insert(count,path+"/")       # 하나 씩 배열에 차곡차곡
            ar_fe.insert(count,filename)
        elif ext == '.png':
            ar_pa.insert(count,path+"/ ")       # 하나 씩 배열에 차곡차곡
            ar_fe.insert(count,filename)
    count = count + 1                                           # 하위 for문 돌때마다 카운트 증가
count_1 = count                                                 # 카운트값 동기화

while sw != 3:
    sw = int(input("1.find duplicates , 2.copy, 3. exit:     "))
    if sw == 1: 
        du_str = collections.Counter(ar_fe)          # 중복 뭐 있는지 값까지 나타냄
        print(du_str)
    elif sw == 2: 
        for img in ar_pa:                                               # 리스트 합치기
            count_1 = count_1 - 1   
            ar.insert(count_1,ar_pa[count_1]+ar_fe[count_1])
        for v in ar:                                                            #  복사 for 문
            count_1 = count_1 + 1
            if count >= count_1:
                shutil.copy(ar[count_1],'C:\\Users\\sh.Jo\\Downloads\\newfolder\\')  #이미지 복사
    elif sw == 3:
        break

    
