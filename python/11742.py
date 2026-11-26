import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  u,v = map(int,sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (n+1)

def bfs(start):
  q = deque([start])
  visited[start] = True
  while q:
    now = q.popleft()
    for next in graph[now]:
      if not visited[next]:
        visited[next] = True
        q.append(next)

count = 0
for i in range(1,n+1):
  if not visited[i]:
    bfs(i)
    count += 1

print(count)