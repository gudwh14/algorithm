def solution(N, A, M, nums):
    A.sort()
    for num in nums:
        answer = False
        left = 0
        right = N - 1

        while left <= right:
            mid = (left + right) // 2

            if A[mid] == num:
                answer = True
                break

            if A[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        if answer:
            print(1)
        else:
            print(0)


N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

solution(N, A, M, nums)
