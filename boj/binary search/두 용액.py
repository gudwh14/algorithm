def solution(N, nums):
    answer = (-1, -1, float('+inf'))
    nums.sort()

    left = 0
    right = N - 1
    while left < right:
        sum = nums[left] + nums[right]
        if abs(0 - answer[2]) > abs(0 - sum):
            answer = (left, right, sum)

        if sum == 0:
            break
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1

    print(nums[answer[0]], nums[answer[1]])


N = int(input())
nums = list(map(int, input().split()))
print(solution(N, nums))
