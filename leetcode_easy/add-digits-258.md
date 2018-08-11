# 258. Add Digits

2018年8月11日

## 题目

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

```no
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
```

Follow up:

Could you do it without any loop/recursion in O(1) runtime?

## 分析

采取了最直接的办法，首先用一个while循环判断数字的位数是否大于二，若满足，再次使用一个while循环，将各个数都加到临时变量temp中，之后更新Num。

## 示例代码

C++:

```cpp
class Solution {
public:
    int addDigits(int num) {
        while(num/10){
            int temp = 0;
            while(num){
                temp += num%10;
                num/=10;
            }
            num = temp;
        }
        return num;
    }
};
```

最快的方法，还是考察的数学...

```cpp
class Solution {
public:
    int addDigits(int num) {
        --num;
        return num % 9 + 1;

    }
};
```