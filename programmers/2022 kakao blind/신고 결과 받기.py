import collections


def solution(id_list, report, k):
    reports = collections.defaultdict(set)
    counts = collections.defaultdict(int)
    answer = [0 for _ in range(len(id_list))]

    for rep in report:
        users = rep.split(' ')
        if users[1] not in reports[users[0]]:
            counts[users[1]] += 1
        reports[users[0]].add(users[1])

    for i in range(len(id_list)):
        for report_user in reports[id_list[i]]:
            if counts[report_user] >= k:
                answer[i] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))