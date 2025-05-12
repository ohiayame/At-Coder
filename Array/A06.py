# 답 저장 배열
results = []

# N = 마지막 날 , Q = 질문의 개수
n, q = map(int, input().split())

# input N개의 입력받기  list넣기
peple = list(map(int, input().split()))

# Q번 반복
for _ in range(q):
    # input L과 R 받기
    l, r = map(int, input().split())
    
    # results에 p추가
    results.append(sum(peple[l-1:r]))

# 출력
print("\n".join(map(str, results)))



# 답 코드
n,q=map(int,input().split())
a=list(map(int,input().split()))
rs=[0]*(n+1)  # [0, 입력 값 들, ...n] 

for i in range(n):
    rs[i+1]=a[i]+rs[i] # 당일 인원수 + 전날까지의 인원수

for j in range(q):
    l,r=map(int,input().split())
    print(rs[r]-rs[l-1]) # r날까지의 인원수 - l보다 전의 인원수

