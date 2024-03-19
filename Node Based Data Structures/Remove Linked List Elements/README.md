# Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 
### Example 1:
![removelinked-list](https://github.com/Aishwariyaa-Anand/Competitive-Coding/assets/124241367/e8db8e60-1887-40d6-b4d6-a827e6a6434b)

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

### Example 2:
```
Input: head = [], val = 1
Output: []
```

### Example 3:
```
Input: head = [7,7,7,7], val = 7
Output: []
```


**Constraints:**

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
