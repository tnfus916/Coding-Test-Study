import math


def solution(enroll, referral, seller, amount):
    answer = []

    total = {name: 0 for idx, name in enumerate(enroll)}

    refer_set = {}
    for i in range(len(enroll)):
        refer_set[enroll[i]] = referral[i]

    for i in range(len(seller)):
        refer = seller[i]
        price = amount[i] * 100

        while True:
            if refer == "-" or price == 0:
                break

            take = math.ceil(price * 0.9)
            total[refer] += take
            price -= take
            refer = refer_set[refer]
    print(total)
    answer = [total[name] for idx, name in enumerate(total)]

    return answer


print(
    solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["sam", "emily", "jaimie", "edward"],
        [2, 3, 5, 4],
    )
)
