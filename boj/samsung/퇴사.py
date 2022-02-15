import sys


# 로직
# n은 최대 15일경우 해당 상담을 하거나 안하거나 모든경우를 구하면 최대 2^15 개의 경우가 나온다 최대 32768 경우의수를 확인하면 된다
def solution(n, consults):
    answer = []

    def dfs(next, price):
        # 상담일이 출근날이 아닐경우 종료!
        if next >= n:
            answer.append(price)
            return

        t, p = consults[next]
        # 해당 상담을 하지 않을경우, 바로 다음 상담으로 이동
        dfs(next + 1, price)
        # 만약 해당 상담을 진행할경우, n일 까지 상담을 끝낼수있으면, 진행할수있는 다음 상담으로 이동
        if next + t > n:
            # 더이상 진행할수 없을경우 수익저장
            answer.append(price)
            return
        dfs(next + t, price + p)

    # 1번째 상담부터 시작, 수익은 0
    dfs(0, 0)
    # 오름차순으로 정렬
    answer.sort()
    # 최대값 출력
    return answer[-1]


n = int(sys.stdin.readline())
consults = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, consults))
