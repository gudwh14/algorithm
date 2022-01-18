import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        answer += 1
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        heapq.heappush(scoville, one + two * 2)
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2], 4))
