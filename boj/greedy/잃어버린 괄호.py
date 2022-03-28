def solution(exps):
    new_exp = []

    for exp in exps:
        plus_exp = exp.split('+')
        temp = 0
        for num in plus_exp:
            temp += int(num)
        new_exp.append(temp)

    answer = new_exp[0]

    for i in range(1, len(new_exp)):
        answer -= new_exp[i]

    return answer


exps = input().split('-')
print(solution(exps))
