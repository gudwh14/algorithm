from typing import List


def solution(phone_book: List[str]):
    # 정렬을 함으로써 바로 다음 index 만 조사할수있게 된다.
    phone_book = sorted(phone_book)

    for i in range(0, len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
