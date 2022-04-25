import itertools


def solution(infos):
    answer = 0
    # 0번 선수는 항상 4번째 순서로 고정
    players = [1, 2, 3, 4, 5, 6, 7, 8]
    # 1 ~ 8 번 선수로 만들수 있는 순열 구하기
    pers = list(itertools.permutations(players))

    # 각 순서 마다 반복
    for per in pers:
        per = list(per)
        # 0번 선수 4번째 순서로 만들기
        per.insert(3, 0)

        # 시작 인덱스
        start = 0
        # 얻은 점수
        score = 0

        # 각 이닝 실행
        for idx in range(N):
            # 아웃 카운트, 주자 초기화
            out = 0
            juja = [0, 0, 0]
            while True:
                # 순서에 맞는 타자가 치는 value 가져오기
                val = infos[idx][per[start]]

                # 아웃
                if val == 0:
                    out += 1
                    if out == 3:
                        out = 0
                        # 다음 타자
                        start = (start + 1) % 9
                        break
                # 1루타
                elif val == 1:
                    score += juja[2]
                    juja[2] = juja[1]
                    juja[1] = juja[0]
                    juja[0] = 1
                # 2루타
                elif val == 2:
                    score += juja[2] + juja[1]
                    juja[2] = juja[0]
                    juja[1] = 1
                    juja[0] = 0
                # 3루타
                elif val == 3:
                    score += juja[2] + juja[1] + juja[0]
                    juja[2] = 1
                    juja[1] = 0
                    juja[0] = 0
                # 홈런
                elif val == 4:
                    score += juja[2] + juja[1] + juja[0] + 1
                    juja[2] = 0
                    juja[1] = 0
                    juja[0] = 0
                # 다음 타자
                start = (start + 1) % 9
        # 스코어 최대값 저장
        answer = max(answer, score)
    return answer


N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]
print(solution(infos))
