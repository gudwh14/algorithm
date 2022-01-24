import itertools


def solution(expression):
    answer = float('-inf')
    exp = []
    temp = ''
    for char in expression:
        if char in ['+', '-', '*']:
            exp.append(temp)
            exp.append(char)
            temp = ''
        else:
            temp += char

    if temp:
        exp.append(temp)

    operate = []
    for char in expression:
        if char in ['+', '-', '*'] and char not in operate:
            operate.append(char)

    len_op = len(operate)
    operate = list(itertools.permutations(operate, len(operate)))
    for _op in operate:
        temp = exp[::]
        op_index = 0
        while op_index != len_op:
            op = _op[op_index]
            try:
                idx = temp.index(op)
                result = eval(temp[idx - 1] + op + temp[idx + 1])
                del temp[idx - 1]
                del temp[idx - 1]
                del temp[idx - 1]
                temp.insert(idx - 1, str(result))
            except ValueError:
                op_index += 1
        answer = max(answer, abs(int(''.join(temp))))
    return answer


print(solution("100-200*300-500+20"))
