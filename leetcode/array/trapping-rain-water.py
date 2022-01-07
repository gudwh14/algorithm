from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        def calc_water(water: int, _height: List[int]) -> int:
            # 맨처음 높이를 시작높이로 지정
            start = _height[0]
            water_list = []

            for value in _height:
                # 다음 높이가 시작높이보다 작을경우 water_list 에 삽입
                if value < start:
                    water_list.append(value)
                # 다음 높이가 시작높이보다 크거나 같을경우 water_list 길이만큼 시작높이를 곱한다음 water_list 에 존재하는 높이만큼 빼준다
                else:
                    water = water + (start * len(water_list) - sum(water_list))
                    water_list = []
                    start = value

            # 시작 높이보다 크거나 같은 높이를 만나지 못했을 경우
            # 시작높이를 water_list 에 존재하는 가장 큰 값으로 설정후 , 함수를 다시 실행한다
            if len(water_list) > 0:
                start = min(start, max(water_list))
                water_list.insert(0, start)
                return calc_water(water, water_list)
            return water

        if len(height) == 1:
            return 0
        return calc_water(0, height)


s = Solution()
print(s.trap(height=[4, 2, 0, 3, 2, 5]))
print(s.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap(height=[4, 2, 3]))
print(s.trap(height=[4, 1, 2, 3]))
print(s.trap(height=[4, 0, 2, 0, 3]))
print(s.trap(height=[5, 4, 1, 2]))
