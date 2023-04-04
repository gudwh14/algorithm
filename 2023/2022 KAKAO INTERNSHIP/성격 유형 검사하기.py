import collections


def solution(survey, choices):
    answer = ''
    n = len(survey)
    scores = collections.defaultdict(int)
    types = ['RT', 'CF', 'JM', 'AN']

    for i in range(n):
        l, r = survey[i][0], survey[i][1]
        choice = choices[i]

        if 4 - choice > 0:
            scores[l] += abs(4 - choice)
        else:
            scores[r] += abs(4 - choice)

    for type in types:
        l, r = type[0], type[1]

        if scores[l] < scores[r]:
            answer += r
        else:
            answer += l

    return answer