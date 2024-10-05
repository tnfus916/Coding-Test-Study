def solution(players, callings):
    seq = {}
    name = {}
    for i in range(len(players)):
        seq[players[i]] = i
        name[i] = players[i]

    for player in callings:
        moveto = seq[player] - 1
        loser = name[moveto]

        seq[player] = moveto
        seq[loser] = moveto + 1

        name[moveto] = player
        name[moveto + 1] = loser

    result = []
    for i in range(len(players)):
        result.append(name[i])

    return result
