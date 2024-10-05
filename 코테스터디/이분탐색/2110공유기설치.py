import sys

input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]

house.sort()

# 공유기 간 거리의 범위를 (1, house[n-1]-house[0]+1)로 설정
srt = 1
end = house[n - 1] - house[0]

# 가장 인접한 두 공유기 사이의 최대 거리에 대한 이분탐색
while srt <= end:

    # 설치할 공유기가 2개일 때는 최대값을 바로 반환
    if c == 2:
        ans = house[n - 1] - house[0]
        break

    dist = (srt + end) // 2
    cnt = 1
    h = house[0]

    # 각 공유기 간 거리가 해당거리보다 같거나 클 때 c개를 설치할 수 있는지 체크
    for i in range(1, n):
        if house[i] - h >= dist:
            h = house[i]
            cnt += 1

    if cnt >= c:
        srt = dist + 1
        ans = dist
    else:
        end = dist - 1

print(ans)
