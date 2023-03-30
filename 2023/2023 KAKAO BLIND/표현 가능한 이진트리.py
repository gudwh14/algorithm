import math


def to_binary(number):
    binary = ""
    while (number):
        mod = number % 2
        number = number // 2
        binary += str(mod)

    return binary[::-1]


# leaf가 1일때 parent가 1인지 체크
def check(binary, parent):
    mid = len(binary) // 2
    if binary:
        if binary[mid] == '1':
            child = True
        else:
            child = False
    else:
        return True

    if child and not parent:
        return False
    else:
        left = binary[:mid]
        right = binary[mid + 1:]
        return check(left, child) and check(right, child)


def solution(numbers):
    answer = []

    for number in numbers:
        if number == 1:
            answer.append(1)
            continue

        binary = to_binary(number)
        n = len(binary)

        total_len = 2 ** (int(math.log(n, 2)) + 1) - 1
        need_len = total_len - n
        binary = '0' * need_len + binary
        n = len(binary)

        # root가 존재 해야함
        if binary[n // 2] == '1':
            if check(binary, True):
                answer.append(1)
            else:
                answer.append(0)
        else:
            answer.append(0)

    return answer