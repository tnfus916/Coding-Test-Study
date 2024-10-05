import math


def solution(fees, records):
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees

    def get_dif(srt, end):
        srt_hr, srt_min = map(int, srt.split(":"))
        end_hr, end_min = map(int, end.split(":"))

        minute = 0
        if srt_min > end_min:
            minute += end_min - srt_min + 60
            end_hr -= 1
        else:
            minute += end_min - srt_min

        minute += (end_hr - srt_hr) * 60

        return minute

    def get_fee(total_min):
        nonlocal base_fee
        nonlocal base_time
        nonlocal unit_fee
        nonlocal unit_time

        if total_min <= base_time:
            return base_fee
        else:
            return base_fee + math.ceil((total_min - base_time) / unit_time) * unit_fee

    parked = {}
    total_time = {}
    for record in records:
        time, car, inout = record.split()
        if inout == "IN":
            parked[car] = time
        else:
            if car in total_time:
                total_time[car] += get_dif(parked[car], time)
            else:
                total_time[car] = get_dif(parked[car], time)
            parked.pop(car)

    for car in parked:
        if car in total_time:
            total_time[car] += get_dif(parked[car], "23:59")
        else:
            total_time[car] = get_dif(parked[car], "23:59")

    total_fee = []
    for car in total_time:
        total_fee.append((car, get_fee(total_time[car])))

    total_fee.sort(key=lambda x: x[0])

    for i in total_fee:
        answer.append(i[1])

    return answer


print(
    solution(
        [180, 5000, 10, 600],
        [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ],
    )
)
