import sys
import heapq

input = sys.stdin.readline

city, path, dist, srt = map(int, input().split())
graph = [[] for _ in range(city)]
for _ in range(path):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)

# 다익스트라: 시작점으로부터 모든 노드까지의 거리 구하기
dijk = [10**9] * city
dijk[srt - 1] = 0

queue = []
heapq.heappush(queue, (0, srt - 1))

while queue:
    cnt, node = heapq.heappop(queue)

    if dijk[node] < cnt:
        continue

    for neighbor in graph[node]:
        if dijk[node] + 1 < dijk[neighbor]:
            dijk[neighbor] = dijk[node] + 1
            heapq.heappush(queue, (cnt + 1, neighbor))


if dist in dijk:
    for i in range(city):
        if dijk[i] == dist:
            print(i + 1)
else:
    print(-1)
