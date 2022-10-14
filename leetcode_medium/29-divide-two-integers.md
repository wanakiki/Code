## 29. 两数相除

2022-10-14 12:07:15

### 题目

给定两个整数，被除数 ``dividend`` 和除数 ``divisor``。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 ``dividend`` 除以除数 ``divisor`` 得到的商。

整数除法的结果应当截去（``truncate``）其小数部分，例如：``truncate(8.345) = 8`` 以及 ``truncate(-2.7335) = -2``



**示例 1:**

```
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
```

**示例 2:**

```
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
```



**提示：**


- 被除数和除数均为 32 位有符号整数。
- 除数不为 0。
- 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [&minus;2<sup>31</sup>,  2<sup>31 </sup>&minus; 1]。本题中，如果除法结果溢出，则返回 2<sup>31 </sup>&minus; 1。



[LeetCode链接](https://leetcode-cn.com/problems/divide-two-integers/)

### 思路及代码


溢出的情况只包含除法的最终结果是 2^32，为避免额外判断，将关键变量转化为 long long 后处理。

```cpp
class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend == 0)   return 0;
        
        bool flag = false;  // 标记最后是否需要负号
        if((long long)(dividend) * divisor < 0) flag = true; 

        long long dividend_l = abs(dividend);
        divisor = abs(divisor);

        vector<long long> vals;
        vector<long long> times;
        long long cur_val = divisor;
        long long cur_times = 1;

        while(cur_val <= dividend_l){
            vals.push_back(cur_val);
            times.push_back(cur_times);
            cur_val += cur_val;
            cur_times += cur_times;
        }

        long long res = 0;
        
        for(int i = vals.size() - 1; i >= 0; i--){
            while(dividend_l >= vals[i]){
                dividend_l -= vals[i];
                res += times[i];
            }
        }
        
        if(flag)    res = -res;
        if(res > INT_MAX)   return INT_MAX;
        else    return res;

        
    }
};
```