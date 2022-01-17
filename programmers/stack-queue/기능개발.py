import collections


def solution(progresses, speeds):
    answer = []
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        count = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1

        if count != 0:
            answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
