def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    counts = [0, 0, 0]
    answer = []

    for i in range(len(answers)):
        if answers[i] == a[i % 5]:
            counts[0] += 1
        if answers[i] == b[i % 8]:
            counts[1] += 1
        if answers[i] == c[i % 10]:
            counts[2] += 1

    result = max(counts)
    for i in range(len(counts)):
        if result == counts[i]:
            answer.append(i + 1)

    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))