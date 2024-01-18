import sys
input = sys.stdin.readline
city, bus = map(int, input().split())

graph = [[] for _ in range(city)]
for _ in range(bus):
    a, b, c = map(int, input().split())
    graph[a-1].append((c, b-1))  # (시간,도착도시#)

dist = [10**9]*city
dist[0] = 0
breakcheck = 0
for chk in range(city):
    for i in range(city):
        for value, to in graph[i]:
            if dist[i] != 10**9 and dist[to] > dist[i]+value:
                dist[to] = dist[i]+value
                if chk == city-1:
                    breakcheck = 1
                    break
        if breakcheck == 1:
            break

if breakcheck == 1:
    print(-1)
else:
    for i in range(1, city):
        if dist[i] == 10**9:
            print(-1)
        else:
            print(dist[i])

