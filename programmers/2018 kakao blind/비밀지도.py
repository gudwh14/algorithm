def solution(n, arr1, arr2):
    def calc_binary(num):
        temp = []
        if num > 0:
            while num > 1:
                div, mod = divmod(num, 2)
                temp.insert(0, mod)
                num = div
            temp.insert(0, 1)

        if len(temp) < n:
            while len(temp) < n:
                temp.insert(0, 0)
        return temp

    result = []
    map_1 = [calc_binary(num) for num in arr1]
    map_2 = [calc_binary(num) for num in arr2]
    for i in range(n):
        temp = ""
        for j in range(n):
            if map_1[i][j] + map_2[i][j] == 0:
                temp += " "
            else:
                temp += "#"
        result.append(temp)

    return result


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(1, [0], [0]))
