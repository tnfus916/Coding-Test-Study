from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([])
    trucks = len(truck_weights)

    sec, idx = 0, 0
    while idx < trucks:
        if len(bridge) > 0 and bridge[0][1] == sec:
            weight += bridge[0][0]
            bridge.popleft()

        if weight - truck_weights[idx] >= 0:
            bridge.append((truck_weights[idx], sec + bridge_length))
            weight -= truck_weights[idx]
            idx += 1
        sec += 1

    return bridge[-1][1] + 1