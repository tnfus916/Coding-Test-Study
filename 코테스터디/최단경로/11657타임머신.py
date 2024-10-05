import sys

input = sys.stdin.readline

city, edge = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(edge)]

time = [10**9] * city
time[0] = 0
for _ in range(city - 1):
    for srt, end, t in edges:
        if time[srt - 1] != 10**9:
            if time[srt - 1] + t < time[end - 1]:
                time[end - 1] = time[srt - 1] + t

# 마지막에 갱신된다면 무한으로 마이너스
inf = 0
for srt, end, t in edges:
    if time[srt - 1] != 10**9:
        if time[srt - 1] + t < time[end - 1]:
            inf = 1
            break

if inf == 1:
    print(-1)
else:
    for i in range(1, city):
        if time[i] == 10**9:
            print(-1)
        else:
            print(time[i])
