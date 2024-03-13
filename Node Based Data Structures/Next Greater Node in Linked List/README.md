# Next Greater Node In Linked List

You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.


### Example 1:
![image](https://github.com/Aishwariyaa-Anand/Competitive-Coding/assets/124241367/766ef8f4-2611-4226-9fe0-ab50a13d9754)

```
Input: head = [2,1,5]
Output: [5,5,0]
```


### Example 2:
![image](https://github.com/Aishwariyaa-Anand/Competitive-Coding/assets/124241367/d5c023dc-99b6-490f-95e9-188deb86331a)

```
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

**Constraints:**

The number of nodes in the list is n.
1 <= n <= 104
1 <= Node.val <= 109
