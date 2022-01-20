def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    while people:
        if len(people) == 1:
            people.pop()
            answer += 1
            break
        if people[-1] + people[0] > limit:
            people.pop(0)
            answer += 1
        else:
            for i in range(1, len(people)):
                if people[0] + people[i] <= limit:
                    people.pop(i)
                    people.pop(0)
                    answer += 1
                    break
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([40, 100], 240))