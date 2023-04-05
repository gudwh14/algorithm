import collections


def solution(queue1, queue2):
    answer = 0
    queue1 = collections.deque(queue1)
    queue2 = collections.deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    n, m = len(queue1), len(queue2)

    while sum1 != sum2:
        if sum1 > sum2:
            item = queue1.popleft()
            queue2.append(item)
            sum1 -= item
            sum2 += item
        else:
            item = queue2.popleft()
            queue1.append(item)
            sum2 -= item
            sum1 += item
        answer += 1

        if answer > (n + m) * 3:
            return -1
    return answer