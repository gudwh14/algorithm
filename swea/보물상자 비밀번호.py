def solution(N, K, nums):
    answer = []
    token = N // 4
    for _ in range(token):
        last = nums[N - 1]
        for i in range(N - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last
        for i in range(0, N, token):
            answer.append(int(''.join(nums[i: i + token]), 16))
    answer = set(answer)
    answer = list(answer)
    answer.sort(reverse=True)
    idx = K % len(answer)
    return answer[idx - 1]


T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(input())
    value = solution(N, K, nums)
    print('#%d' % test_case, end=" ")
    print(value)
