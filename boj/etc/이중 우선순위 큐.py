import heapq

# 최대 힙, 최소 힙 두개를 사용하여
# 숫자를 제거할때 동기화가 필요함
# 저장할때 인덱스를 같이 저장하여
# 해당 인덱스가 삭제된 원소이면 먼저 제거하고 삭제 연산 진행
def solution(infos):
    maxQ = []
    minQ = []
    is_delete = [False] * len(infos)

    for idx in range(len(infos)):
        cmd, num = infos[idx]
        if cmd == 'I':
            heapq.heappush(minQ, (int(num), idx))
            heapq.heappush(maxQ, (-int(num), idx))
        elif cmd == 'D':
            if num == '-1' and minQ:
                while minQ and is_delete[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    value, id = heapq.heappop(minQ)
                    is_delete[id] = True
            elif num == '1' and maxQ:
                while maxQ and is_delete[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    value, id = heapq.heappop(maxQ)
                    is_delete[id] = True

    while minQ and is_delete[minQ[0][1]]:
        heapq.heappop(minQ)

    while maxQ and is_delete[maxQ[0][1]]:
        heapq.heappop(maxQ)

    if not minQ or not maxQ:
        print('EMPTY')
    else:
        print(-heapq.heappop(maxQ)[0], heapq.heappop(minQ)[0])


T = int(input())
for _ in range(T):
    N = int(input())
    infos = [list(input().split()) for _ in range(N)]
    solution(infos)
