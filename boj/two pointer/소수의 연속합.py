def solution(N):
    if N == 1:
        return 0
    answer = 0
    nums = [True for _ in range(N + 1)]
    prime = []
    for num in range(2, N + 1):
        if not nums[num]:
            continue
        gop = 2
        idx = num
        while idx * gop <= N:
            nums[idx * gop] = False
            gop += 1

    for num in range(2, N + 1):
        if nums[num]:
            prime.append(num)

    left, right = 0, 0
    n = len(prime)
    sum = prime[0]

    while True:
        if sum >= N:
            if sum == N:
                answer += 1
            sum -= prime[left]
            left += 1
        else:
            right += 1
            if right == n:
                break
            sum += prime[right]

    return answer


N = int(input())
print(solution(N))
