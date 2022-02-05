import collections


def solution(cacheSize, cities):
    answer = 0
    count = 0
    cache = collections.deque()
    for city in cities:
        if city.lower() in cache:
            answer += 1
            cache.remove(city.lower())
            cache.append(city.lower())
        else:
            answer += 5
            cache.append(city.lower())
            count += 1
            if count > cacheSize:
                cache.popleft()
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(5, ["a", "a", "a", "a", "a", "a"]))