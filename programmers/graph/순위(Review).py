import collections


def solution(n, results):
    answer = 0
    # 승리, 패배 해쉬를 각각 두어서 해결
    win = collections.defaultdict(set)
    lose = collections.defaultdict(set)

    # 초기 set 세팅
    for winner, loser in results:
        win[loser].add(winner)
        lose[winner].add(loser)

    #
    print(win)
    print(lose)
    for i in range(1, n + 1):
        for winner in win[i]:  # i 에게 진 상대는 i 를 이긴 상대에게도 진다
            lose[winner].update(lose[i])

        for loser in lose[i]:  # i 를 이긴 상대는 i 에게 진 상대도 이긴다
            win[loser].update(win[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1: # 대진이 n - 1 개 만큼 만족하면 순위를 결정할 수 있다.
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
