import sys

N,M = map(int, sys.stdin.readline().split())
d_len = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 하는 변수가 말도 안되게 큰 수를 하는거임
start = 0
end = max(d_len)

result = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  for x in d_len:
    #떡 자르기
    if x > mid :
      total += x - mid

  if total < M :
    end = mid - 1
  else:
    result = mid
    start = mid + 1
print(result)
