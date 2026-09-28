# 217. Contains Duplicate

| Difficulty | Topics |
|---|---|
| **Easy** | `Array` `Hash Table` `Sorting` |

[View problem on LeetCode](https://leetcode.com/problems/contains-duplicate/)

---

## Problem Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** true

**Explanation:**

The element 1 occurs at the indices 0 and 3.

**Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** false

**Explanation:**

All elements are distinct.

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]

**Output:** true

**Constraints:**

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

---

## Approach

The accepted solution is available below. Add a short explanation of the technique used in the code.

---

---

## Algorithm

Review the accepted solution and describe its main processing steps.

---

---

## Complexity Analysis

- **Time Complexity:** Add after analysing the loops and operations used by the solution.
- **Space Complexity:** Add after checking the extra data structures used by the solution.

---

---

## Solution

### `0217-contains-duplicate.java`

```java
import java.util.HashSet;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int arr:nums) {
  if (seen.contains(arr)) {
      return true;
  }
  seen.add(arr);
        }
        return false;
    }
}
```
