## 172. Factorial Trailing Zeroes
##### 2018-05-28 21:15:10
##### 数学很关键...
***
## 题目
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
```
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```
Example 2:
```
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```
Note: Your solution should be in logarithmic time complexity.
## 问题分析
计算给定数字阶乘末尾零的个数，如果正常的做法不仅复杂度较高，而且无法计算较大数字。  
这样来看，这道题考的数学的知识比较多，因为末尾的零只能由5和2构成，而一个五之前会有足够的偶数，所以算出阶乘中5的个数就是结果末尾零的个数。
## 示例代码
```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        int sum=0;
        while(n>4)
            sum += n/=5;
        return sum;
    }
};
```

