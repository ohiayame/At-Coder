n, q = map(int, input().split())

s_list = list(input())

result = []

for i in range(q):
    l, r = map(int, input().split())
    re = True
    for j in range((r-l + 1) // 2):
        if s_list[l-1 + j] != s_list[r-1 - j] :
            re = False
            break
    result.append('Yes' if re else 'No')

print("\n".join(result))