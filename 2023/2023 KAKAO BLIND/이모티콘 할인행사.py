import itertools


def solution(users, emoticons):
    answer = [0, 0]
    n, m = len(users), len(emoticons)
    discounts = [10, 20, 30, 40]

    items = list(itertools.product(discounts, repeat=m))

    for item in items:
        emoticon_plus_cnt = 0
        total_price = 0

        for user in users:
            u_discount, u_price = user
            price = 0

            for idx in range(m):
                if item[idx] >= u_discount:
                    price += emoticons[idx] * (100 - item[idx]) * 0.01

            if price >= u_price:
                emoticon_plus_cnt += 1
            else:
                total_price += price
        answer = max(answer, [emoticon_plus_cnt, int(total_price)], key=lambda x: (x[0], x[1]))
    return answer
#         answer.append([emoticon_plus_cnt, int(total_price)])

#     answer.sort(key=lambda x: (x[0], x[1]))
#     return answer[-1]