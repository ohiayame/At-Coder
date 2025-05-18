n = int(input())

a_list = list(map(int, input().split()))
# 누적 계산 저장 배열
re = [0]
# 답 저장 배열
result = []

# 누적 계산
for i in range(len(a_list)):
    if a_list[i] == 0:
        re.append(re[i] - 1)
    else:
        re.append(re[i] + 1)

q = int(input())
# 입력 값에 따라 결과 저장 
for _ in range(q):
    l, r = map(int, input().split())
    
    msg = 'loss'
    if re[r] - re[l-1] > 0:
        msg = 'win'
    elif re[r] - re[l-1] == 0:
        msg = 'drow'
    result.append(msg)
# 출력
for j in range(len(result)):
    print(result[j])