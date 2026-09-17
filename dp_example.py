import sys

x = int(sys.stdin.readline().rstrip())

d = [0] * 30001

for i in range(2, x+1):

  # 현재에서 1을 빼는 경우
  d[i] = d[i-1] + 1

  # 현재가 2로 나눠지는 경우
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2] + 1)

  # 현재가 3으로 나눠지는 경우
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3] + 1)

  # 현재가 5로 나눠지는 경우
  if d % 5 == 0:
    d[i] = min(d[i], d[i//5] + 1)

print(d[x])