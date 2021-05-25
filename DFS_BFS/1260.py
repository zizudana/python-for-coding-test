# DFS와 BFS https://www.acmicpc.net/problem/1260
from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for i in range(n+1)]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited1[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited2[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if not visited2[i] and graph[v][i] == 1:
                queue.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)
