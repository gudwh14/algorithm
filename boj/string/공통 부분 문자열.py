def solution(A, B):
    max_len = 0
    len_a = len(A)
    len_b = len(B)
    if len_b > len_b:
        for i in range(len_b):
            for j in range(i + 1, len_b + 1):
                if max_len < j - i:
                    word = B[i:j]
                    if word in A:
                        max_len = j - i
                    else:
                        break
    else:
        for i in range(len_a):
            for j in range(i + 1, len_a + 1):
                if max_len < j - i:
                    word = A[i:j]
                    if word in B:
                        max_len = j - i
                    else:
                        break
    return max_len


A = input()
B = input()
print(solution(A, B))
