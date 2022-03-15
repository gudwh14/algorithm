import collections


# 풀이법
# 가장 큰 수로 만들기 위해서는 자리수가 큰 알파벳을 가장 큰값으로 만들어 주면된다.
# 맨 앞자리부터 큰자리를 부여하게 되면 예외가 발생함
# EX) AB
#     BB
# 따라서, 각 알파벳에 자리수에 대한 가중치를 만든다
# 가중치가 가장큰 알파벳에게 큰 숫자를 부여!
def solution(N, words):
    answer = 0
    value = 9
    alphabet = collections.defaultdict(int)

    # 자리숫에대한 가중치 구하기
    for word in words:
        n = len(word)
        for i in range(n):
            alphabet[word[i]] += 10 ** (n - i - 1)

    # 가중치를 기준으로 알파벳 정렬
    a = sorted(list(alphabet.items()), key=lambda x: x[1], reverse=True)
    alphabet = {}

    # 수 매핑하기
    for char, weight in a:
        alphabet[char] = value
        value -= 1

    # 수 더하기
    for word in words:
        temp = []
        for char in word:
            temp.append(str(alphabet[char]))
        answer += int(''.join(temp))

    return answer


N = int(input())
words = [input() for _ in range(N)]
print(solution(N, words))
