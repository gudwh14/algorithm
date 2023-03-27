import bisect


def solution(k, room_number):
    answer = []
    rooms = [0 for _ in range(k + 1)]
    q = [i for i in range(1, k + 1)]

    for number in room_number:
        if rooms[number] == 0:
            rooms[number] = 1
            answer.append(number)
            q.remove(number)
        else:
            idx = bisect.bisect_left(q, number)
            rooms[q[idx]] = 1
            answer.append(q[idx])
            q.pop(idx)

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
print(solution(1, [1]))
