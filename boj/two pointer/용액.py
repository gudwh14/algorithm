# Two Pointer

N = int(input())
li = list(map(int, input().split()))

def solution():
    if li[0] >= 0:
        return li[0], li[1]
    elif li[-1] <= 0:
        return li[-2], li[-1]

    answer = float('+inf')
    index = ('+inf', '+inf')
    left = 0
    right = N - 1

    while left < right:
        if answer >= abs(li[left] + li[right]):
            answer = abs(li[left] + li[right])
            index = (left, right)

        if li[left] + li[right] <= 0:
            left += 1
        else:
            right -= 1
    return li[index[0]], li[index[1]]

# Delete Bracket
print(*solution())
