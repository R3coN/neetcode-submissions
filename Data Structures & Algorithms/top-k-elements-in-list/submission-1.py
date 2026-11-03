import sys
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        for i in nums:
            if i in dict_nums.keys():
                dict_nums[i] += 1
            else:
                dict_nums[i] = 1
        a = []
        for key, value in sorted(dict_nums.items(), key=lambda item: item[1], reverse=True):
            if k != 0:
                a.append(key)
                k -= 1
            else:
                break
        return a

        