import itertools

# 우선순위 없이 왼쪽 식부터 계산하기
def calc(exps):
    # 표현식의 길이가 1일 경우 그대로 반환
    if N == 1:
        return int(exps[0])

    left = None
    op = None
    # 들어오는 순서대로 계산하기
    for exp in exps:
        if left == None:
            left = exp
        elif left != None and op == None:
            op = exp
        elif left != None and op != None:
            left = eval(str(left) + op + str(exp))
            op = None
    return left


def solution(exps):
    answer = float('-inf')
    count = N // 2

    # 피연선자가 0 ~ 9까지 한자리 수이므로 괄호를 넣을 수 있는 인덱스값은 2의 배수 이다
    hubos = [idx * 2 for idx in range(count)]

    for i in range(0, count + 1):
        # 괄호를 넣을 조합 구하기
        combs = list(itertools.combinations(hubos, i))

        # 조합 반복
        for comb in combs:
            # 새로운 표현식
            new_exps = []
            # 인덱스
            idx = 0
            while idx < N:
                # 만약 괄호를 넣을 경우
                if idx in comb:
                    # 미리 계산해서 계산값을 new_exps 에 추가
                    value = eval(''.join(exps[idx:idx + 3]))
                    new_exps.append(value)
                    # 인덱스는 3 증가 -> 괄호를 열고 닫았을때 인덱스를 3만큼 증가해야 다음 표현식을 접근할 수 있음!
                    idx += 3
                # 괄호를 넣지 않을 경우 그대로 추가
                else:
                    new_exps.append(exps[idx])
                    idx += 1
            # 최대값 구하기
            answer = max(answer, calc(new_exps))

    return answer


N = int(input())
exps = list(input())
print(solution(exps))
