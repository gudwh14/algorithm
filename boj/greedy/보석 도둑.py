import heapq


def solution(N, K, jewels, bags):
    answer = 0

    jewels.sort()
    # 가방 무게가 작은 것부터 넣어야함
    bags.sort()

    temp_jew = []

    for bag in bags:
        # 가방에 넣을 수 있는 보석들을 가치를 기준으로 최대힙으로 만들어주기
        while jewels and bag >= jewels[0][0]:
            heapq.heappush(temp_jew, -heapq.heappop(jewels)[1])

        # 넣을 수 있는 보석이 있으면 가방에 넣기
        # 여러개의 보석중 가치가 제일 큰 보석을 넣는다.
        # 1의 무게를 견딜수 있는 가방에 넣을 수 있는 보석은 2의 무게를 견디는 가방에도 넣을 수 있다
        # 가방을 오름차순으로 정렬했기 때문에 temp_jew 에 존재하는 보석들은 모두 현재 가방에도 넣을 수 있는 보석 들이다.
        if temp_jew:
            value = -heapq.heappop(temp_jew)
            answer += value

        # 남아 있는 보석이 없으면 종료
        elif not jewels:
            break

    return answer


N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
print(solution(N, K, jewels, bags))
