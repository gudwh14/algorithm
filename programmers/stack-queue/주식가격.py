def solution(prices):
    price = []
    answer = [-1 for i in range(len(prices))]
    up_index = []

    for i in range(0, len(prices)):
        while price and price[-1] > prices[i]:
            answer[up_index[-1]] += 1
            price.pop()
            up_index.pop()
        price.append(prices[i])
        up_index.append(i)

        for index in up_index:
            answer[index] += 1

    return answer


print(solution([1, 2, 3, 2, 3]))
