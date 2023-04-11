def solution(price, money, count):
    answer = 0
    while count > 0:
        answer += price * count
        count -= 1
    answer = answer - money

    return answer if answer > 0 else 0