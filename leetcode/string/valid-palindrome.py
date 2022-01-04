import collections
from typing import Deque

# 슬라이스를 이용하여 역순시켜 팰린드롬 확인
def isPalindrome(self, s: str) -> bool:
    strs: list = []

    # 영문자와 숫자만 구분하여 리스트에 삽입
    for char in s:
        if char.isalnum():
            # 대소문자 구별하지 않기때문에 소문자로 통일
            strs.append(char.lower())

    # 리스트 를 역순하여 기존 리스트와 일치하는지 확인하여 팰린드롬 판단
    return ''.join(strs[::-1]) == ''.join(strs)


# Deque 를 이용한 팰린드롬 확인
def isPalindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()

    # 영문자와 숫자만 구분하여 리스트에 삽입
    for char in s:
        if char.isalnum():
            # 대소문자 구별하지 않기때문에 소문자로 통일
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

