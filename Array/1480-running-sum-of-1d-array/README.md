# 1480. Running Sum of 1d Array

| Difficulty | Topics |
|---|---|
| **Easy** | `Array` `Prefix Sum` |

[View problem on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/)

---

## Problem Description

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

**Example 2:**

```
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

**Example 3:**

```
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

---

## Approach

Use the **prefix-sum technique**.

Start from index `1`. Add the previous running sum to the current element. After each update, `nums[i]` contains the sum of all elements from index `0` through index `i`.

The input array is updated directly, so an additional result array is not required.

---

---

---

---

---

---

---

---

## Algorithm

1. Start iterating from index `1`.
2. Add `nums[i - 1]` to `nums[i]`.
3. Repeat until the final element.
4. Return the updated array.

---

---

---

---

---

---

---

---

## Complexity Analysis

- **Time Complexity:** `O(n)` because every array element is processed once.
- **Space Complexity:** `O(1)` because the input array is updated in place.

---

---

---

---

---

---

---

---

## Solution

### `1480-running-sum-of-1d-array.py`

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
  nums[i] += nums[i - 1]
        return nums
```
