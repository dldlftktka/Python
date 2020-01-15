wr = int(input())

def hansu(num):
    values = 0            # 한수 값
    for cw in range(1, num+1):            # 1부터 시작
        nums = list(map(int, str(cw)))                  # 매핑으로 자릿수 나눔
        if cw <= 99:
            values += 1
        elif nums[0] - nums[1] == nums[1] - nums[2]:          # 최대 1000자리라..
            values += 1
        elif cw > 1001:
            print("1000 이하의 숫자를 입력 바랍니다.")
                
    return values

print(hansu(wr))
