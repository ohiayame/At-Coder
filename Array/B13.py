n, k = map(int, input().split())

a_list = list(map(int, input().split()))
re = [0]

sum = 0
for num in a_list:
    re.append(re[-1] + num)

for j in range(len(re)):
    # 1,len(re) -> j+1, len(re)
    for p in range(j+1, len(re)):
        s = re[p]-re[j]
        
        if 0 < s <= k:
            sum += 1
        elif k < s:
            break
print(sum)