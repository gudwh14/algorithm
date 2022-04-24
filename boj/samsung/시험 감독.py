import sys
import collections


def solution(n, people, B, C):
    answer = 0
    counts = collections.Counter(people)

    # key : 시험장에 응시한 응시자의 수,  value: 해당 시험장 개수
    for key, value in counts.items():
        # 최소 총감독관은 1명 이상 들어가야 함으로 count = 1 부터 시작
        count = 1
        # 응시자 수 - 총감독관이 감독할수 있는 수
        key -= B

        # 해당 값이 0 보다 크면 부 감독관이 필요함!
        if key > 0:
            # 남은 응시자의 수를 부 감독관이 감독하려면 필요한 감독관의 수 구하기
            div, mod = divmod(key, C)
            count += div
            # 나머지가 있으면 감독관이 1명 더 필요함!
            if mod > 0:
                count += 1
        # 총 필요한 감독관 수는, 1개의 시험장의 감독관수 * 해당 시험장의 개수!
        answer += count * value
    return answer


n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
B, C = map(int, input().split())
print(solution(n, people, B, C))
