# DFS와 BFS https://www.acmicpc.net/problem/1260
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    print(v, end=' ')
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
