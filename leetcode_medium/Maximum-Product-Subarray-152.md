## 152. Maximum Product Subarray
##### 2018-05-11 23:19:19
##### 动态规划
***
## 题目
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```
Example 2:
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
## 分析
先解决简单的动态规划问题，求出数组中连续数字的最大和：
需要保留两个变量，处理局部最大与全局最大。
```
local[i + 1] = Max(local[i] + A[i], A[i]);

global[i + 1] = Max(local[i + 1], global[i]);
```
代码
```cpp
int maxSubArray(int A[], int n)
{
    assert(n > 0);
    if (n <= 0)
        return 0;
    int global = A[0];
    int local = A[0];

    for(int i = 1; i != n; ++ i) {
        local = MAX(A[i], local + A[i]);
        global = MAX(local, global);
    }
    return global;
}
```
