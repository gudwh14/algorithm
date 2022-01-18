def solution(brown, yellow):
    _sum = brown + yellow
    for i in range(_sum, 0, -1):
        result = list(divmod(_sum, i))
        if result[1] == 0:
            x = i
            y = result[0]
            if (x * 2) + (y * 2) - 4 == brown:
                return [x, y]


print(solution(24, 24))
