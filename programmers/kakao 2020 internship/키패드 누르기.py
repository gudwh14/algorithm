def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for number in numbers:
        if number in [1, 4, 7]:
            left = number
            answer += 'L'
        elif number in [3, 6, 9]:
            right = number
            answer += 'R'
        else:
            if number == 0:
                number = 11
            num_y, num_x = divmod(number - 1, 3)
            left_y, left_x = divmod(left - 1, 3)
            right_y, right_x = divmod(right - 1, 3)

            diff = (abs(num_y - left_y) + abs(num_x - left_x)) - (abs(num_y - right_y) + abs(num_x - right_x))
            if diff == 0:
                if hand == 'left':
                    left = number
                    answer += 'L'
                else:
                    right = number
                    answer += 'R'
            elif diff > 0:
                right = number
                answer += 'R'
            elif diff < 0:
                left = number
                answer += 'L'
    return answer


# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))