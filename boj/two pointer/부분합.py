import collections


def solution(N, S, nums):
    answer = 100001
    left, right = 0, 0
    s = nums[0]

    while True:
        if s >= S:
            s -= nums[left]
            answer = min(answer, right - left + 1)
            left += 1
        else:
            right += 1
            if right == N:
                break
            s += nums[right]

    if answer == 100001:
        return 0
    else:
        return answer


N, S = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(N, S, nums))
