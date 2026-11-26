import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
box = []
for i in range(n):
  box.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      queue.append((i,j))

def bfs():
  while queue:
    x,y = queue.popleft()
    for d in range(4):
      nx, ny = x + dx[d], y + dy[y]
      if nx<0 or nx>=n or ny<0 or ny<=m:
        continue
      if box[nx][ny] != 0:
        continue
      box[nx][ny] = box[x][y] + 1
      queue.append((nx,ny))

bfs()

result = 0
for row in box:
  for val in row:
    if val == 0:
      print(-1)
      exit()
    result = max(result,val)

print(result - 1)