n = int(input())

a_list = list(map(int, input().split()))

check_li = [0] * n
sum_value = 0
for i in range(len(a_list)-1):
    if i == 0:
        sum_value += a_list[i]-1
    elif a_list[i] != 1:
        sum_value += a_list[i]-1 - sum(check_li[:a_list[i]-1])
    check_li[a_list[i]-1] = 1



print(sum_value)


# 답
class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 2)

    def update(self, idx, value):
        while idx < len(self.tree):
            self.tree[idx] += value
            idx += idx & -idx

    def query(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result


n = int(input())
a_list = list(map(int, input().split()))

bit = BIT(n + 2)
sum_value = 0

for i in range(n - 1):
    val = a_list[i]
    count = bit.query(val - 1)  # val보다 작은 수 몇 번 나왔는지
    sum_value += val - 1 - count
    bit.update(val, 1)

print(sum_value)
