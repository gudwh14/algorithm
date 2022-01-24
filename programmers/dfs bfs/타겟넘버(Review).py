import collections


def solution(numbers, target):
    answer = 0
    Q = collections.deque()
    Q.append([numbers[0], 0])
    Q.append([-1 * numbers[0], 0])

    while Q:
        number, index = Q.popleft()
        index += 1
        if index < len(numbers):
            Q.append([number + numbers[index], index])
            Q.append([number - numbers[index], index])
        else:
            if number == target:
                answer += 1

    return answer
