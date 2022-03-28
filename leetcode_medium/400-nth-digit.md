## 400. 第 N 位数字

2021-11-30 17:31:50

### 题目

给你一个整数 ``n`` ，请你在无限的整数序列 ``[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]`` 中找出并返回第 ``n``位数字。



**示例 1：**

```
输入：n = 3
输出：3
```

**示例 2：**

```
输入：n = 11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
```



**提示：**


- ``1 <= n <= 2<sup>31</sup> - 1``



[LeetCode链接](https://leetcode-cn.com/problems/nth-digit/)

### 思路及代码

可以根据数字的宽度将所有数字分为不同区间，初始区间长度为9，观察易知数字宽度每增加1，区间长度变为原来的十倍。按此关系，结合区间中数字的宽度，可以计算出第n个字符所处的区间，和对应数字位于区间的索引，进一步可得到最终的字符。需要注意的是，在计算数字索引时，应将n减一后进行常见的除宽度、模宽度操作。

```cpp
class Solution {
public:
    int findNthDigit(long long int n) {

        long long int mask = 9;
        long long int width = 1;
        int base = 1;
        while(n > mask * width){
            n -= mask * width;
            mask *= 10;
            width++;
            base *= 10;
        }

        // 剩余宽度在当前区间的索引 和数字位数
        int index = (n-1) / width;
        int num_index = (n-1) % width;

        int real_num = base + index;
        return to_string(real_num)[num_index] - '0';
    }
};
```