import collections


def solution(str1, str2):
    A = []
    B = []

    for i in range(len(str1) - 1):
        temp = str1[i:i + 2]
        if temp.isalpha():
            A.append(temp.upper())
    for i in range(len(str2) - 1):
        temp = str2[i:i + 2]
        if temp.isalpha():
            B.append(temp.upper())

    count_a = collections.Counter(A)
    count_b = collections.Counter(B)
    inter = []
    union = []
    for key, value in count_a.items():
        if count_b[key]:
            for _ in range(0, min(value, count_b[key])):
                inter.append(key)

    for key, value in count_a.items():
        if count_b[key]:
            for _ in range(0, max(value, count_b[key])):
                union.append(key)
        else:
            for _ in range(0, value):
                union.append(key)
    for key, value in count_b.items():
        if key not in union:
            for _ in range(0, value):
                union.append(key)

    if len(A) == 0 and len(B) == 0:
        return 65536
    return int(float((len(inter) / len(union))) * 65536)


# print(solution("aa1+aa2", "AAAA12"))
print(solution("aa+aa+bb+bb", "AAAA+BBBB"))
print(solution("E=M*C^2", "e=m*c^2"))
