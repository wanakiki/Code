# 344. Reverse String

2018年8月13日

## 题目

Write a function that takes a string as input and returns the string reversed.

Example 1:

```no
Input: "hello"
Output: "olleh"
```

Example 2:

```no
Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
```

## 分析

挺简单的题目，有很多实现方式。

## 示例代码

C++

```cpp
class Solution {
public:
    string reverseString(string s) {
        string res;
        for(int i = s.size() -1; i >= 0; i--){
            res += s[i];
        }
        return res;
    }
};
```

```cpp
class Solution {
public:
    string reverseString(string s) {
        reverse(s.begin(),s.end());
        return s;
    }
};
```