# less than magic method
class compare(str):
    def __lt__(self, other):
        return self + other > other + self


def solution(numbers):
    str_numbers = []
    for number in numbers:
        str_numbers.append(str(number))

    str_numbers.sort(key=compare)

    return str(int(''.join(str_numbers)))


print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0]))
