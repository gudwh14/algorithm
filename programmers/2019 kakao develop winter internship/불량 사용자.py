import collections
import itertools


def solution(user_id, banned_id):
    banned = collections.defaultdict(list)
    n = len(banned_id)
    result = []

    for idx, ban in enumerate(banned_id):
        ban_count = collections.Counter(ban)
        for user in user_id:
            if len(user) == len(ban):
                user_count = collections.Counter(user)
                comp = ban_count - user_count
                if len(comp) == 1:
                    banned[idx].append(user)

    per = list(itertools.permutations(user_id, n))
    for item in per:
        count = 0
        for i in range(n):
            if item[i] not in banned[i]:
                break
            else:
                count += 1
        if count == n:
            result.append(sorted(list(item)))

    result = list(set(map(tuple, result)))
    return len(result)


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
# print(solution(["12345", "12453", "aaaaa"], ["*****", "*****"]))
print(solution(['12345', 'aaaaa'], ['**', '***']))
