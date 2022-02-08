import heapq


# 우선순위 큐를 이용하여 풀이
# 효율성 테스트에서 K 가 2 x 10^13, 완전 탐색으로 해결 불가
def solution(food_times, k):
    answer = -1
    Q = []
    food_len = len(food_times)
    prev_food_time = 0

    # food_times 를 몇번째 음식인지와 함께 우선순위큐에 저장
    for i in range(food_len):
        heapq.heappush(Q, (food_times[i], i + 1))

    # 큐가 존재할때 까지 반복
    while Q:
        # food_time 이 짧은 음식부터 , 음식을 먹는데 걸리는 시간을 계산
        # 음식을 먹는데 걸리는 시간 = 남은음식 양 * 남은음식 개수
        total_time = (Q[0][0] - prev_food_time) * food_len

        # K 가 현재 음식을 먹는 시간보다 크다면, 현재 음식을 다먹을 수 있다는 뜻!
        # 그경우 현재 음식을 제거
        if k >= total_time:
            # 남은 시간에서, 현재 음식을 먹는 시간을 제거
            k -= total_time
            # 현재 음식양을 prev_food_time 에 저장
            prev_food_time, _ = heapq.heappop(Q)
            # 남은 음식 개수 - 1
            food_len -= 1
        # 다 먹을수 없는 경우
        else:
            # K 가 남아 있는 개수보다 클수 있으므로 남은 음식개수로 나눈 나머지를 인덱스로 사용해야함!
            idx = k % food_len
            # 인덱스 순으로 다시 정렬
            Q.sort(key=lambda x: x[1])
            # 다음에 먹어야할 인덱스를 가져오기
            answer = Q[idx][1]
            break

    return answer


print(solution([3, 1, 2], 5))
