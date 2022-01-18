import collections


def solution(citations):
    counts = sorted(collections.Counter(citations).items(), reverse=True)
    for i in range(len(citations), 0, -1):
        _sum = 0
        for count in counts:
            if count[0] >= i:
                _sum += count[1]

        if _sum >= i:
            return i
    return 0


print(solution([3, 0, 6, 1, 5]))
print(solution([0]))
