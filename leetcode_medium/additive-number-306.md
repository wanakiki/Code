# 306. Additive Number

时间：2018年7月28日

## 题目

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

```no
Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```

Example 2:

```no
Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199
```

Follow up:
How would you handle overflow for very large input integers?

## 分析

题目要求我们判断以string形式给我们的一个数字是否满足所描述的条件（相邻两个数相加等于第三个数，数由几个数字构成没有限制，但是要保证能够加到末尾）。

需要注意一点，因为题目明确提出来数字的开头不能为零，所以我们可以针对这点减少不必要的循环。关于数字过长，我的解决方法是转化为``long long``型。

做法的主要思路是用``substr``截取不同长度的字符串，将其转化为数字，判断是否满足加和的条件。首先在要求书写的函数内用两个循环来截取不同对应长度的字符串，另外用了一个辅助函数来进行更深的递归判断（很难离开递归）。如果连第一个函数都不能截取到两个字符串，那么就直接判错。

>最近换用了vscode，按照提示的格式把自己的markdown语法矫正了一下，区别和之前稍微有点大😀

## 示例代码

C++:

```cpp
class Solution {
public:
    bool helper(long long num_l1, long long num_l2, string num, int len, int start){
        if(len == start)
            return true;
        for(int l3 = 1; l3 <= len -start; l3++){  
             //注意这里是小于等于
            string num3 = num.substr(start, l3);
            if(l3 > 1 && num3[0] == '0')
                break;
            long long num_l3 = atoi(num3.c_str());
            if(num_l1 + num_l2 == num_l3)
                if(helper(num_l2, num_l3, num, len, start+l3))
                    return true;
        }
        return false;
    }
    bool isAdditiveNumber(string num) {
        int len = num.size();
        //l1、l2为截取的长度
        for (int l1 = 1; l1 < len; l1++){
            string num1 = num.substr(0,l1);
            if(l1 > 1 && num1[0] == '0')
                break;      //长度大于一并且以零开始的数不满足题目要求
            long long num_l1 = atoi(num1.c_str());

            for(int l2 = 1; l2 < len - l1; l2++){
                string num2 = num.substr(l1, l2);   //起始位置应该为l1
                if(l2 > 1 && num2[0] == '0')
                    break;
                long long num_l2 = atoi(num2.c_str());

                if(helper(num_l1, num_l2, num, len, l1 + l2))
                    return true;
            }
        }
        return false;
    }
};
```

不知道为什么``stoll``函数在我的本地无法运行，本地测试的时候换用了``atoi``+``c_str()``的方法。