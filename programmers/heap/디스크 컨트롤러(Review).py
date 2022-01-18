import heapq


def solution(jobs):
    answer = 0
    now = index = 0
    start = -1
    heap = []

    while index < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for job in jobs:
            if start < job[0] <= now:
                # 작업 요소 시간 기준으로 최소힙 을 만들어야 함으로 요소를 앞뒤로 바꿔서 push
                heapq.heappush(heap, [job[1], job[0]])

        # 처리할 작업이 있는경우
        if len(heap) > 0:
            current = heapq.heappop(heap)
            # start :  바로 이전에 완료한 작업의 총 시간
            start = now
            # now : 현재 시점
            now += current[0]
            # 시간 계산
            answer += (now - current[1])
            # 인덱스 증가
            index += 1
        # 작업이 없을경우 now만 1 증가
        else:
            now += 1

    return answer // len(jobs)


# print(solution([[0, 3], [102, 2], [1, 9], [100, 3], [5, 3], [4, 7], [2, 6]]))
# print(solution([[0, 3]]))
print(solution([[0, 3], [1, 9], [2, 6]]))
