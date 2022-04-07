def solution(A, B, C):
    def power(a, b):
        if b == 1:
            return a % C
        else:
            temp = power(a, b // 2)
            if b % 2 == 0:
                return temp * temp % C
            else:
                return temp * temp * a % C

    return power(A, B)


A, B, C = map(int, input().split())
print(solution(A, B, C))
