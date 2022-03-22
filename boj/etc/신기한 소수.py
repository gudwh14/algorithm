import math


def is_prime_number(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(N):
    def make_special_prime(num, n):
        if n == N:
            print(num)
        for i in range(1, 10):
            new_num = int(num + str(i))
            if is_prime_number(new_num):
                make_special_prime(str(new_num), n + 1)

    make_special_prime('', 0)


N = int(input())
solution(N)
