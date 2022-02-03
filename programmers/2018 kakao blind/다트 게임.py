def solution(dartResult):
    score = []
    star = False
    index = 0

    while index < len(dartResult):
        dart = dartResult[index]
        if dart.isdigit():
            if dartResult[index + 1].isdigit():
                score.append(10)
                index += 1
            else:
                score.append(int(dart))
            star = False
        elif dart == 'D':
            score[-1] = pow(score[-1], 2)
        elif dart == 'T':
            score[-1] = pow(score[-1], 3)
        elif dart == '*':
            if star:
                score[-1] = score[-1] * 2
            else:
                if len(score) == 1:
                    score[-1] = score[-1] * 2
                else:
                    score[-1] = score[-1] * 2
                    score[-2] = score[-2] * 2
            star = True
        elif dart == '#':
            score[-1] = -score[-1]
        index += 1

    return sum(score)


# print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
