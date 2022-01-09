

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        jewels_dict = {}

        # 보석을 해쉬로 저장
        for jewel in jewels:
            jewels_dict[jewel] = True

        # 스톤들을 비교하여 key가 존재하면 카운팅
        for stone in stones:
            try:
                if jewels_dict[stone]:
                    result += 1
            except KeyError:
                continue

        return result


# python 다운 방식
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 리스트 컴프리헨션 이용!
        return sum(stone in jewels for stone in stones)



s = Solution()
print(s.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))