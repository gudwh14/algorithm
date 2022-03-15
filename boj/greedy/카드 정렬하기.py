import heapq


def solution(N, cards):
    answer = 0
    heapq.heapify(cards)

    left = None
    right = None
    while cards:
        card = heapq.heappop(cards)
        if left == None:
            left = card
        elif right == None:
            right = card
        if left and right:
            answer += left + right
            heapq.heappush(cards, left + right)
            left = None
            right = None

    return answer


N = int(input())
cards = [int(input()) for _ in range(N)]
print(solution(N, cards))
