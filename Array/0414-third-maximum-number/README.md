# 414. Third Maximum Number

| Difficulty | Topics |
|---|---|
| **Easy** | `Array` `Sorting` |

[View problem on LeetCode](https://leetcode.com/problems/third-maximum-number/)

---

## Problem Description

Given an integer array `nums`, return *the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number*.

**Example 1:**

```
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
```

**Example 2:**

```
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
```

**Example 3:**

```
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
```

**Constraints:**

- `1 <= nums.length <= 104`
- `-231 <= nums[i] <= 231 - 1`

**Follow up:** Can you find an `O(n)` solution?

---

## Approach

The accepted solution is available below. Add a short explanation of the technique used in the code.

---

## Algorithm

Review the accepted solution and describe its main processing steps.

---

## Complexity Analysis

- **Time Complexity:** Add after analysing the loops and operations used by the solution.
- **Space Complexity:** Add after checking the extra data structures used by the solution.

---

## Solution

### `0414-third-maximum-number.py`

```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num = set(nums)
        n = len(num)
        if n >= 3:
  return sorted(num, reverse = True)[2]
        else:
  return max(num)
```
