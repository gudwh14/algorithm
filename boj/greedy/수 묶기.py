import collections


def solution(N, nums):
    num_dict = collections.defaultdict(bool)
    neg = []
    pos = []
    nums.sort()
    for num in nums:
        num_dict[num] = True
        if num > 0:
            pos.append(num)
        elif num < 0:
            neg.append(num)

    pos.reverse()
    # print(neg)
    # print(pos)
    new_nums = []
    # 음수 계산: 작은 음수끼리 곱하면 큰 양수, 곱할 음수가 없으면 0이랑 곱하거나 0 이없으면 그대로
    i = 0
    while i < len(neg):
        if i + 1 < len(neg):
            new_nums.append(neg[i] * neg[i + 1])
            i += 1
        else:
            if num_dict[0]:
                new_nums.append(0)
            else:
                new_nums.append(neg[i])
        i += 1

    # print(new_nums)
    # 양수 계산: 1은 그대로, 큰수 끼리 곱하면 더 큰 값이 나타남
    i = 0
    while i < len(pos):
        if pos[i] == 1:
            new_nums.append(1)
        else:
            if i + 1 < len(pos):
                if pos[i + 1] == 1:
                    new_nums.append(pos[i])
                else:
                    new_nums.append(pos[i] * pos[i + 1])
                    i += 1
            else:
                new_nums.append(pos[i])
        i += 1
    # print(new_nums)
    return sum(new_nums)


N = int(input())
nums = [int(input()) for _ in range(N)]
print(solution(N, nums))
