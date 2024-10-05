import sys
import heapq

input = sys.stdin.readline


def prim():
    global ans
    cnt = 0
    while heap:
        if cnt == v:
            break
        weight, node = heapq.heappop(heap)
        if visit[node] == 0:
            visit[node] = 1
            ans += weight
            cnt += 1
            for w, near in graph[node]:
                if visit[near] == 0:
                    heapq.heappush(heap, (w, near))


def kruskal():
    print()


v, e = map(int, input().split())

graph = [[] for _ in range(v)]
visit = [0] * v
heap = [(0, 0)]  # (가중치, 1번 노드)

for _ in range(e):
    srt, end, weight = map(int, input().split())
    graph[srt - 1].append((weight, end - 1))
    graph[end - 1].append((weight, srt - 1))

# 최소 스패닝 트리 찾기
ans = 0
prim()
print(ans)
