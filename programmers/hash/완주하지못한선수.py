import collections


def solution(participant, completion):
    part = collections.Counter(participant)
    comp = collections.Counter(completion)

    for key, value in part.items():
        if comp[key] < value:
            return key


print(solution(["leo", "kiki", "eden"], ["kiki", "eden"]))
