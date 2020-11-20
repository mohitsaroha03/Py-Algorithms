# Link - https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/oliver-and-the-game-3/description/

import sys

sys.setrecursionlimit(10 ** 8)
time = 0
n = int(input())
graph = [[] for i in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [False for i in range(n + 1)]
starttime = [0 for i in range(n + 1)]
endtime = [0 for i in range(n + 1)]
time = 0


def DFS(u, visited, starttime, endtime, time):
    visited[u] = True
    time = time + 1
    starttime[u] = time
    for v in graph[u]:
        time = DFS(v, visited, starttime, endtime, time)

    time += 1
    endtime[u] = time
    return time


def Check(type_move, x, y):
    if type_move == 0:
        if starttime[x] < starttime[y] and endtime[y] < endtime[x]:
            return True

        return False

    if type_move == 1:
        if starttime[y] < starttime[x] and endtime[x] < endtime[y]:
            return True
        return False


DFS(1, visited, starttime, endtime, 0)
m = int(input())
# print(starttime)
# print(endtime)
for _ in range(m):
    tmp_1, tmp_2, tmp_3 = map(int, input().split())
    if Check(tmp_1, tmp_2, tmp_3):
        print("YES")
    else:
        print("NO")
