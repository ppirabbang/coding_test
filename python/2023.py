import sys
from collections import deque
sys.setrecursionlimit(10**6)

N,M,K,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for i in range(M):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)

dist = [-1] * (N+1)
dist[X] = 0
q = deque([X])

while(q):
  now = q.popleft()
  for next in graph[now]:
    if dist[next] == -1:
      dist[next] = dist[now] + 1
      q.append(next)

check = False
for i in range(1,i+1):
  if (dist[i] == K):
    print(i)
    check = True

if check == False:
  print(-1)

  
