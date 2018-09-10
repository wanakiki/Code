# 415. Add Strings

2018年9月10日

## 题目

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

1. The length of both num1 and num2 is < 5100.
2. Both num1 and num2 contains only digits 0-9.
3. Both num1 and num2 does not contain any leading zero.
4. You **must not use any built-in BigInteger library or convert the inputs to integer** directly.

## 分析

刚开始学习C++时就已经遇到过的大整数加法问题，思路是这样的：从两个输入字符串的最后一位开始计算，计算出每一位的和并加到返回数组后。当某一为数大于9时需要考虑进位，使用``%``、``/``两个运算符可以相对容易的达到这个目的。另外因为输入字符串的最后一位相加得到的返回字符串的第一位，所以最终返回之前我们需要将其反转。

大致思路是这样，但是由于输入两个字符串的长度不定，如何设置循环条件才能达到最高效率是相对困难的点。

## 示例代码

C++

```cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        string res;
        int len1 = num1.size() - 1, len2 = num2.size() - 1;
        int temp = 0;
        while(1){
            if(len1 < 0 && len2 < 0){
                if(temp)
                    res += temp + '0';
                break;
            }
            if(len1 >= 0){
                temp += num1[len1] - '0';
                len1 --;
            }
            if(len2 >= 0){
                temp += num2[len2] - '0';
                len2 --;
            }
            res += temp % 10 + '0';
            temp /= 10;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

上面是我的代码，可以看出循环部分实现的不是很合理，下面是优化过的代码，效率提升了很多：

```cpp
class Solution {
public:
    string addStrings(const string& num1, const string &num2) {
        string result;
        int len1 = num1.length()-1;
        int len2 = num2.length()-1;
        int carry = 0;
        while(len1 >= 0 || len2 >= 0 || carry)
        {            
            int sum = carry + ((len1 >=0) ? num1[len1] - '0' : 0) +((len2 >= 0) ? num2[len2] - '0' : 0);
            result += (sum%10) + '0';
            carry = sum/10;

            --len1;
            --len2;
        }
        
        reverse(result.begin(), result.end());
        return result;
    }
};
```