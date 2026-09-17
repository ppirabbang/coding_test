import sys

N = int(sys.stdin.readline().rstrip())
list_ = list(map(int, sys.stdin.readline().split()))

d = [0] * 100

d[0] = list_[0]
d[1] = max(list_[0], list_[1])
for i in range(2, N):
  d[i] = max(d[i-1], d[i-2] + list_[i])

print(d[N-1])

# dp는 횟수를 저장하는 느낌으로 생각, 여기서는 내가 있는 곳을 i 라 하면 i-1을 선택하면 i는 선택하지 못함 한 칸 띄워야 하니까, 그래서 d[i-1] 와 d[i-2] + list_[i] 중 max 값으로 설정