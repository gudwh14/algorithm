import collections


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = collections.deque()
    now_weight = 0

    while True:
        answer += 1
        for i in range(len(truck)):
            truck[i][1] += 1

        while truck and truck[0][1] >= bridge_length:
            now_weight -= truck[0][0]
            truck.popleft()

        if truck_weights and now_weight + truck_weights[0] <= weight and len(truck) < bridge_length:
            truck.append([truck_weights[0], 0])
            now_weight += truck_weights[0]
            truck_weights.pop(0)

        if not truck and not truck_weights:
            break
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
