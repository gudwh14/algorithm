# BruteForce로 해결

def solution(N, M, broken):
    answer = abs(int(N) - 100)
    for num in range(1000001):
        for n in str(num):
            if int(n) in broken:
                break
        else:
            answer = min(answer, len(str(num)) + abs(num - int(N)))

    return answer


N = input()
M = int(input())
if M == 0:
    broken = []
else:
    broken = list(map(int, input().split()))
print(solution(N, M, broken))
