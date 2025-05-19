n, m = map(int, input().split())
loss_li = list(map(int, input().split()))

std_li = [m] * n

for los_std in loss_li:
    std_li[los_std-1] -= 1

print("\n".join(map(str,std_li)))