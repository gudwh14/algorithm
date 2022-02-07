from itertools import combinations


def solution(relation):
    # key의 개수
    N = len(relation[0])
    # key_idx = [0,1,2,3]
    key_idx = list(range(N))
    # key 목록
    candidate_keys = []

    for i in range(1, N + 1):
        # 각각의 조합 만들기 ( 1 ~ 4개 뽑기 )
        for comb in combinations(key_idx, i):
            # 중복되는지 확인하는 배열
            hist = []
            for rel in relation:
                # 각 조합만큼 key 뽑기 comb = [0, 1], cuurent_key = [rel[0], rel[1]]
                current_key = [rel[c] for c in comb]
                # 하나라도 중복되는 경우: 식별 불가능
                if current_key in hist:
                    break
                else:
                    hist.append(current_key)
            # 하나도 중복 안 된 경우: 식별 가능
            else:
                for ck in candidate_keys:
                    # issubset을 이용하여 최소성 확인
                    if set(ck).issubset(set(comb)):
                        break
                else:
                    # 최소성을 지키면 candi_key 에 등록
                    candidate_keys.append(comb)

    return len(candidate_keys)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
