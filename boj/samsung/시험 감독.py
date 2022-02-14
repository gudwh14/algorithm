import sys
import collections


def solution(n, people, B, C):
    answer = 0
    counts = collections.Counter(people)

    for key, value in counts.items():
        count = 1
        key -= B
        if key > 0:
            div, mod = divmod(key, C)
            count += div
            if mod > 0:
                count += 1

        answer += count * value
    return answer


n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
tmp = list(map(int, sys.stdin.readline().split()))
B = tmp[0]
C = tmp[1]

print(solution(n, people, B, C))
