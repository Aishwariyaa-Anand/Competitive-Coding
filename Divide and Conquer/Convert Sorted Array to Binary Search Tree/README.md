# Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
 

### Example 1:
![btree1](https://github.com/Aishwariyaa-Anand/Competitive-Coding/assets/124241367/10e3ef36-8ef4-427d-8961-a6a463da58f9)

![btree2](https://github.com/Aishwariyaa-Anand/Competitive-Coding/assets/124241367/a9803008-c6ea-4214-a699-6ff62046c438)

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
```
**Explanation:** [0,-10,5,null,-3,null,9] is also accepted:


### Example 2:


```
Input: nums = [1,3]
Output: [3,1]
```
**Explanation:** [1,null,3] and [3,1] are both height-balanced BSTs.


**Constraints:**

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
