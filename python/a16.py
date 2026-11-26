import sys

n,m = map(int,sys.stdin.readline().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽 설치한 뒤의 맵 리스트

for i in range(n):
  data.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0

def virus(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and nx < n or ny >= 0 or ny < m:  #바이러스가 퍼질 수 있는 경우
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx,ny)

def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1

def dfs(count):
  global result

  if count == 3:  # 종료 조건
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]

    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i,j)
  result = max(result,get_score())

  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        count -=1
        data[i][j] = 0

dfs(0)
print(result)     