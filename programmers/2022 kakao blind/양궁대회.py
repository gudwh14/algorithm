import itertools
import collections


# 어피치, 라이언의 과녁점수를 계산해주는 함수
def calc_score(apeach, lion):
    a_score = 0
    l_score = 0
    for i in range(11):
        if apeach[i] >= lion[i]:
            if apeach[i] > 0:
                a_score += 10 - i
        else:
            l_score += 10 - i
    return a_score, l_score


def solution(n, info):
    # 과녁 점수 배열
    score = [10 - n for n in range(11)]
    # 결과를 담을 해쉬
    result = collections.defaultdict(list)

    # 중복 조합으로 슛 개수 만큼 경우의수를 만든다
    for case in itertools.combinations_with_replacement(score, n):
        # 라이언 과녁 초기화
        lion = [0 for _ in range(11)]
        # 라이언 과녁 할당하기
        for shoot in case:
            lion[10 - shoot] += 1
        # 점수계산
        a_score, l_score = calc_score(info, lion)
        # 라이언의 점수가 어피치 점수보다 크면 점수차를 계산하여, 점수차이를 키로, 라이언의 과녁을 저장한다
        if l_score > a_score:
            diff = l_score - a_score
            result[diff].append(lion)

    # 결과가 없으면 라이언이 이길수있는 방법이 없으므로 [-1] 리턴
    if result:
        # 가장 점수차가 큰 값들을 가져온다
        answer = sorted(result.items(), reverse=True)[0][1]
        # 점수차이가 같은 과녁들이 여러개일때, 낮은 점수대를 많이 맞춘 순으로 정렬해주기
        answer.sort(key=lambda x: int(''.join(map(str, x[::-1]))), reverse=True)
        # 1번째 값 리턴
        return answer[0]
    else:
        return [-1]


print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
