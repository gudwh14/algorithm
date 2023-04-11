import collections
import itertools


def get_diff(apeach, lion):
    a, l = 0, 0

    for i in range(11):
        if apeach[i] or lion[i]:
            if apeach[i] >= lion[i]:
                a += 10 - i
            else:
                l += 10 - i

    return a, l


def solution(n, info):
    result = collections.defaultdict(list)
    score = [10 - n for n in range(11)]

    for case in itertools.combinations_with_replacement(score, n):
        lion = [0 for _ in range(11)]

        for shoot in case:
            lion[10 - shoot] += 1

        a, l = get_diff(info, lion)
        diff = l - a

        if diff > 0:
            result[diff].append(lion)
    if result:
        answer = sorted(result.items(), key=lambda x:-x[0])[0][1]

        if len(result) > 1:
            answer.sort(key=lambda x: int(''.join(map(str, x[::-1]))), reverse=True)

        return answer[0]
    return [-1]


solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
