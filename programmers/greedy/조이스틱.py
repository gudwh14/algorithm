def solution(name):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                'Z']
    start = []
    index = 0
    answer = 0
    visit = []
    for _ in range(len(name)):
        start.append('A')

    while ''.join(start) != name:
        if start[index] == name[index]:
            right_find = left_find = 0
            for i in range(index + 1, len(name)):
                if name[i] != 'A':
                    right_find = i
                    break

            for i in range(len(name) - 1, 0, -1):
                if name[i] != 'A' and i not in visit:
                    left_find = i
                    break

            if right_find - index >= (len(name) - 1 - left_find) + (index + 1):
                index = right_find
                answer += right_find - index
            else:
                index = left_find
                answer += (len(name) - 1 - left_find) + (index + 1)
        else:
            _min = min(alphabet.index(name[index]), 26 - alphabet.index(name[index]))
            answer += _min
            start[index] = name[index]
            visit.append(index)
            print(start)
    return answer


print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JAZ"))
print(solution("ABAAB"))
# print(solution("AABAAAAABBB"))