from typing import List

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()
    # 공간복잡도가 O(1) 요구 하기 때문에 변수할당 처리에 제약이 있다. 따라서 s = s[::-1] 이 아닌 s[:] = s[::-1] 로 사용해야함!

