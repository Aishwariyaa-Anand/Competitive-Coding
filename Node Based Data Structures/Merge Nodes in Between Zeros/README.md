# Merge Nodes in Between Zeros

You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
Return the head of the modified linked list.


### Example 1:
![image](https://github.com/Aishwariyaa-Anand/Competitive-Coding/assets/124241367/eae41d1e-9f80-4092-8260-ec7c16d783a9)

```
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
```
**Explanation:**
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.


### Example 2:
![image](https://github.com/Aishwariyaa-Anand/Competitive-Coding/assets/124241367/c181f995-bdc2-4c2a-8df6-1721721b34d9)

```
Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
```
**Explanation:**
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
