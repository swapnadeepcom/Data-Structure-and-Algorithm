class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num = set(nums)
        n = len(num)
        if n >= 3:
            return sorted(num, reverse = True)[2]
        else:
            return max(num)
