import math


def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def convert_to_k(n, k):
    numbers = []

    while n >= k:
        mod = n % k
        n = n // k
        numbers.insert(0, mod)
    numbers.insert(0, n)
    return numbers


def solution(n, k):
    answer = 0
    numbers = convert_to_k(n, k)
    check = []
    visit = {}

    for num in numbers:
        if num != 0:
            check.append(num)
        elif num == 0:
            if check:
                check_num = int(''.join(map(str, check)))
                if check_num in visit:
                    if visit[check_num]:
                        answer += 1
                else:
                    flag = is_prime_number(check_num)
                    if flag:
                        answer += 1
                    visit[check_num] = flag

            check = []

    if check:
        check_num = int(''.join(map(str, check)))
        if is_prime_number(check_num):
            answer += 1
    return answer


print(solution(437674, 3))
