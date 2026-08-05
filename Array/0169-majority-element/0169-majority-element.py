class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = sorted(nums)
        add = 1
        count = 1
        maj = arr[0]

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                add += 1
            else:
                add = 1

            if add > count:
                count = add
                maj = arr[i]

        return maj