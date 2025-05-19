from collections import Counter

n = int(input())

nums = [int(input()) for _ in range(n)]
# dictionary {값:개수, ...}
count = Counter(nums)

sum_num = 0
for c in count.values():
    sum_num += c * (c - 1) // 2
print(sum_num)