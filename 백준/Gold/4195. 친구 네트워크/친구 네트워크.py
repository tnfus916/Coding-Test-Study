import sys

input = sys.stdin.readline


def union(name1, name2):
    # 루트 네임 찾기
    root1 = find(name1)
    root2 = find(name2)
    if root1 != root2:  # 루트가 다르다면 root2의 루트를 root1으로 설정
        parent[root2] = root1

        # root1 네트워크에 root2 네트워크의 인원을 add
        count[root1] += count[root2]


def find(name):
    if parent[name] == name:  # name의 루트 노드가 자기 자신을 가리킨다면 name이 루트 노드! 바로 return
        return name

    parent[name] = find(parent[name])  # 루드 노드를 찾을 때까지 찾기

    return parent[name]


test_case = int(input())

for _ in range(test_case):
    relations = int(input())

    parent = {}
    count = {}
    idx = 0
    for _ in range(relations):
        friend1, friend2 = map(str, input().split())

        # 연결 전, 본인의 루트노드를 본인으로 저장
        if friend1 not in parent:
            parent[friend1] = friend1
            count[friend1] = 1

        if friend2 not in parent:
            parent[friend2] = friend2
            count[friend2] = 1

        # 연결하기, 루트 노드가 다르다면 같도록 설정
        union(friend1, friend2)

        print(count[find(friend1)])
