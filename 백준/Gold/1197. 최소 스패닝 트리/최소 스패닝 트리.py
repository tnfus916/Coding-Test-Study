import sys
input = sys.stdin.readline


def findroot(node):
    if parent[node] != node:
        parent[node] = findroot(parent[node])
    return parent[node]


v, e = map(int, input().split())

parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i] = i

edge = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))
edge.sort()

ans = 0
for value, v1, v2 in edge:
    root1 = findroot(v1)
    root2 = findroot(v2)
    if root1 != root2:
        if root1 < root2:
            parent[root2] = root1
        else:
            parent[root1] = root2
        ans += value
print(ans)