from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))

op_count = list(map(int, input().split()))  # +, - , x, ÷

op_list = []
for i in range(4):
    for j in range(op_count[i]):
        op_list.append(i)


def dfs(op_cnt, num_idx, result):
    global mini
    global maxi
    if op_cnt == n - 1:
        mini = min(mini, result)
        maxi = max(maxi, result)
        return

    for i in range(n - 1):
        if visit[i] == 0:
            visit[i] = 1

            if op_list[i] == 0:
                # print("+", num_list[num_idx], "=", result + num_list[num_idx])
                dfs(op_cnt + 1, num_idx + 1, result + num_list[num_idx])
            elif op_list[i] == 1:
                # print("-", num_list[num_idx], "=", result - num_list[num_idx])
                dfs(op_cnt + 1, num_idx + 1, result - num_list[num_idx])
            elif op_list[i] == 2:
                # print("*", num_list[num_idx], "=", result * num_list[num_idx])
                dfs(op_cnt + 1, num_idx + 1, result * num_list[num_idx])
            else:
                # print("//", num_list[num_idx], "=", result // num_list[num_idx])
                if result < 0:
                    dfs(op_cnt + 1, num_idx + 1, -(-result // num_list[num_idx]))
                else:
                    dfs(op_cnt + 1, num_idx + 1, result // num_list[num_idx])

            visit[i] = 0


mini = 10**9
maxi = -(10**9)
visit = [0] * (n - 1)
dfs(0, 1, num_list[0])

print(maxi)
print(mini)
