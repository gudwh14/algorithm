import collections


def solution(n_card, m_card):
    counts = collections.Counter(n_card)
    for find in m_card:
        print(counts[find], end=' ')


N = int(input())
n_card = list(map(int, input().split()))
M = int(input())
m_card = list(map(int, input().split()))

solution(n_card, m_card)
