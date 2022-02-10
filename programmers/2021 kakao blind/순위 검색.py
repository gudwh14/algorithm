import bisect
import collections


def solution(info, query):
    answer = []
    # 가능한 경우의 수로 배열 만들어 놓기
    lang = ['cpp', 'java', 'python', '-']
    job = ['frontend', 'backend', '-']
    career = ['junior', 'senior', '-']
    food = ['chicken', 'pizza', '-']
    cases = []
    sol = collections.defaultdict(list)

    # 조합 가능한 쿼리 만들기
    for l in lang:
        for j in job:
            for c in career:
                for f in food:
                    cases.append([l, j, c, f])

    # 해당 쿼리를 만족하는 점수만 넣어 놓기
    for case in cases:
        for i in range(len(info)):
            infos = info[i].split(' ')
            score = infos[-1]
            infos = infos[:-1]

            count = 0
            for j in range(4):
                if case[j] == '-':
                    count += 1
                else:
                    if case[j] == infos[j]:
                        count += 1
                    else:
                        break

            if count == 4:
                sol[''.join(case)].append(int(score))

    # 오름차순으로 정렬
    for key, value in sol.items():
        sol[key].sort()

    # 쿼리 비교
    for q in query:
        stmt = q.replace(' and ', ' ')
        stmt = stmt.split(' ')
        score = int(stmt[-1])
        stmt = ''.join(stmt[:-1])

        # 이미 구해놓은 경우의수에서 쿼리에 해당하는 값 뽑아오기
        find = sol[stmt]
        # 이진 탐색으로 해당 점수가 들어갈 인덱스 찾기
        # 전체 길이에서 빼주면, 해당 점수 보다 높은 점수의 개수를 반환
        answer.append(len(find) - bisect.bisect_left(find, score))

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
