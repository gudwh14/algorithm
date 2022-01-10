import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(elements: List[int]):
            # 리프 노드일경우 결과 추가
            if len(elements) == 0: # 통해서 원하는 순열의 조합 개수 설정 가능
                # prev_elemnets를 추가하게되면 prev_elements에 대한 참조가 추가되며, 이경우 참조된 값이 변경될 경우 같이 바뀌게 된다
                # 따라서 반드시 값을 복사하는 형태로 참조 관계를 갖기 않도록 처리해야 한다
                # [:], copy(), deepcopy()
                result.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                # print('ele : ', elements, 'prev : ', prev_elements, 'next : ', next_elements)
                dfs(next_elements)
                # 재귀가 끝나고 돌아왔을때 마지막 요소를 제거하고 새로운 e 를 추가하게 된다
                prev_elements.pop()

        result = []
        prev_elements = []
        dfs(nums)
        return result


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         # itertools 모듈을 사용하여 구현
#         return list(map(list, itertools.permutations(nums)))

s = Solution()
print(s.permute(nums=[1, 2, 3]))
