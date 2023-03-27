def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        print('pivot:', pivot, arr, low, high)
        while low <= high:
            # pivot 보다 작은 원소 찾기
            while arr[low] < pivot:
                low += 1
            # pivot 보다 큰 원소 찾기
            while arr[high] > pivot:
                high -= 1
            # 올바른 인덱스이면, swap
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
                print(arr)
        return low

    sort(0, len(arr) - 1)


print(quick_sort([9, 5, 3, 1, 4, 2]))
