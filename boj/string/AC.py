import collections

T = int(input())


def solution(p, n, nums):
    if n == 0 and 'D' in p:
        return 'error'
    elif n == 0 and 'D' not in p:
        return '[]'
    else:
        nums = list(map(int, nums))
    nums = collections.deque(nums)
    pointer = 0

    for cmd in p:
        if cmd == 'R':
            if pointer == 0:
                pointer = 1
            elif pointer == 1:
                pointer = 0
        elif cmd == 'D':
            try:
                if pointer == 0:
                    nums.popleft()
                elif pointer == 1:
                    nums.pop()
            except IndexError:
                return 'error'
    nums = list(nums)
    if pointer == 1:
        nums.reverse()
    nums = str(nums).replace(' ', '')
    return nums


for _ in range(T):
    p = input()
    n = int(input())
    nums = input().lstrip('[').rstrip(']').split(',')
    print(solution(p, n, nums))
