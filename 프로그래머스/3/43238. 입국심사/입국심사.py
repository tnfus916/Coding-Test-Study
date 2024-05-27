def solution(n, times):
    answer = 0

    srt = 1
    end = min(times) * n

    while srt < end:
        mid = (srt + end) // 2

        tmp = 0
        for time in times:
            tmp += mid // time

        if tmp < n:
            srt = mid + 1
        else:
            end = mid

    return srt
