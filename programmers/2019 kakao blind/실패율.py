import collections


def solution(N, stages):
    count = collections.Counter(stages)
    # 1 스테이지 도달한 플레이어 수
    total = len(stages)
    result = []
    answer = []

    for i in range(1, N + 1):
        # 스테이지 도달한 플레이어 수가 0 아래 면 실패율을 0 으로 처리
        if total <= 0:
            result.append([i, 0])
        else:
            try:
                div = count[i] / total
                total -= count[i]
                result.append([i, div])
            # 해당 스테이지에 도달한 사람이 없을경우 IndexError 예외 처리
            except IndexError:
                result.append([i, 0])

    # 실패율을 기준으로 내림차순 정렬
    result.sort(key=lambda x: x[1], reverse=True)
    # 스테이지만 뽑아서 결과 출력
    for res in result:
        answer.append(res[0])
    return answer


print(solution(5, [1, 2, 3, 4, 4, 4]))
