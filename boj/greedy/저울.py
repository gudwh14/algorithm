def solution(N, nums):
    nums.sort()
    answer = 1

    # answer = 1 을 넣고
    # answer >= num[0] 이면 answer += num
    # 아니면 만들수 없는 수
    # 여태까지의 추의 합이 다음 배열의 요소보다 작으면, 여태까지의 추의 합 + 1이 만들 수 없는 최솟값의 양수 이다.
    for num in nums:
        if answer >= num:
            answer += num
        else:
            break
    return answer


N = int(input())
nums = list(map(int, input().split()))
print(solution(N, nums))
