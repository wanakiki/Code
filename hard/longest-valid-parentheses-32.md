# 32. Longest Valid Parentheses

2019年3月29日

思维

## 题目描述

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

```
Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

## 分析

考验思维的一个题目，花了一定的时间折磨自己却没有解决，暴力解决方法如下（超时）：

```cpp
class Solution {
public:
    bool valid(string s){
        stack<char> S;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '(')
                S.push(s[i]);
            else{
                if(!S.empty() && S.top() == '(')
                    S.pop();
                else
                    return false;
            }
        }
        return S.empty();
    }
    int longestValidParentheses(string s) {
        int res = 0;
        for(int i = 0; i < s.size(); i++)
            for(int j = 2; i + j <= s.size(); j+=2){
                if(valid(s.substr(i,j))){
                    res = res > j ? res: j;
                }
            }
        return res;
    }
};
```