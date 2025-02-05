# A. Vanya and Fence
[Problem Link](https://codeforces.com/contest/677/problem/A)

**Problem Statement:**  
Vanya and his friends are walking along a fence of height `h`. If a friend's height exceeds `h`, they must bend down, taking more space on the road. Friends walking upright take 1 unit of space, while bent friends take 2 units. Determine the minimum total width required for all friends to walk.

**Input:**
3 7 4 5 14

**Output:**
4


**Solution Code:**

```python
n, h = map(int, input().split())
heights = list(map(int, input().split()))

width = sum(2 if height > h else 1 for height in heights)
print(width)
