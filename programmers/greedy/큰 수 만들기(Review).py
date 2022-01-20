def solution(number, k):
    answer = []  # Stack

    for num in number:
        # K (제거할 수 있는 횟수가 남아있고 push 할 값이 마지막원소보다 크다면, push 할 값보다 크거나 같값이 나올때까지 pop 해준다
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    # K 가 남아있을경우 마지막 K개만 제거
    return ''.join(answer[:len(answer) - k])


print(solution("1924", 2))
print(solution("1231234", 5))
print(solution("4177252841", 4))
print(solution("33322", 2))