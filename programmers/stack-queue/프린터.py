import collections


def solution(priorities, location):
    max_prior = max(priorities)
    priorities = collections.deque(enumerate(priorities))
    answer = 0

    while priorities:
        if priorities[0][1] == max_prior:
            answer += 1
            if location == priorities[0][0]:
                return answer
            priorities.popleft()
            if priorities:
                max_prior = max(priorities, key=lambda x: x[1])[1]
        else:
            priorities.append(priorities[0])
            priorities.popleft()
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
