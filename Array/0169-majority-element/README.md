# 169. Majority Element

| Difficulty | Topics |
|---|---|
| **Easy** | `Array` `Hash Table` `Divide and Conquer` `Sorting` `Counting` `Boyer–Moore Majority Vote Algorithm` |

[View problem on LeetCode](https://leetcode.com/problems/majority-element/)

---

## Problem Description

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-109 <= nums[i] <= 109`
- The input is generated such that a majority element will exist in the array.

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

---

## Approach

The accepted solution is available below. Add a short explanation of the technique used in the code.

---

---

---

---

---

## Algorithm

Review the accepted solution and describe its main processing steps.

---

---

---

---

---

## Complexity Analysis

- **Time Complexity:** Add after analysing the loops and operations used by the solution.
- **Space Complexity:** Add after checking the extra data structures used by the solution.

---

---

---

---

---

## Solution

### `0169-majority-element.py`

```python
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         arr = sorted(nums)
#         add = 1
#         count = 1
#         maj = arr[0]

#         for i in range(1, len(arr)):
#             if arr[i] == arr[i - 1]:
#                 add += 1
#             else:
#                 add = 1

#             if add > count:
#                 count = add
#                 maj = arr[i]

#         return maj



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
```
