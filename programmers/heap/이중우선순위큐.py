import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    _min = _max = 0

    for op in operations:
        op_list = op.split(' ')
        if op_list[0] == 'I':
            heapq.heappush(min_heap, int(op_list[1]))
            heapq.heappush(max_heap, -int(op_list[1]))

        elif op_list[0] == 'D':
            if op_list[1] == '-1' and min_heap and max_heap:
                min_heap.sort()
                min_heap.pop(0)
                max_heap.pop()
            elif op_list[1] == '1' and min_heap and max_heap:
                min_heap.pop()
                max_heap.pop(0)

    if min_heap and max_heap:
        _min = heapq.heappop(min_heap)
        _max = -heapq.heappop(max_heap)

    answer = [_max, _min]
    return answer


def solution(operations):
    Q = []
    _min = _max = 0

    for op in operations:
        op_list = op.split(' ')
        if op_list[0] == 'I':
            Q.append(int(op_list[1]))
            Q.sort()
        elif op_list[0] == 'D':
            if op_list[1] == '-1' and Q:
                Q.pop(0)
            elif op_list[1] == '1' and Q:
                Q.pop()

    if Q:
        _min = Q[0]
        _max = Q[-1]

    answer = [_max, _min]
    return answer


print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I 7", "I 5", "I -5", "D -1", "D 1"]))
print(solution(["I 16", "D 1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
