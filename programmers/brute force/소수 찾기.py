import itertools

# itertools 를 이용해서 순열을 만듬
# 라이브러리 사용불가면 순열을 직접 만들어야함
def solution(numbers):
    def is_prime_number(number):
        if number <= 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    answer = 0
    visit = []
    numbers = [i for i in numbers]
    for i in range(1, len(numbers) + 1):
        per = list(itertools.permutations(numbers, i))
        for item in per:
            number = int(''.join(list(item)))
            if number not in visit:
                visit.append(number)
                if is_prime_number(number):
                    answer += 1

    return answer


print(solution("011"))
print(solution("17"))
