# Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 
### Example 1:
![partition](https://github.com/Aishwariyaa-Anand/Competitive-Coding/assets/124241367/708a8b2f-e809-4a24-9716-4caef4a4109b)

```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

### Example 2:
```
Input: head = [2,1], x = 2
Output: [1,2]
```


**Constraints:**

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
