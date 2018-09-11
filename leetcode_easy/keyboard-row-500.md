# 500. Keyboard Row

2018年9月11日

## 题目

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
![tupian](https://leetcode.com/static/images/problemset/keyboard.png)

Example 1:

```no
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
```

Note:
1. You may use one character in the keyboard more than once.
2. You may assume the input string will only contain letters of alphabet.

## 分析

解法很简单，制作一个哈希表，处在相同行的字母有相同的值，便利单词判断是否可以在一行内打出。

看了一个人的解答方式，对我的代码进行了整改，用一个字符串取消了哈希表，使用了``tolower``函数使大写字母转化为小写，整体简单了很多。

参考链接：https://leetcode.com/problems/keyboard-row/discuss/162287/shortest-C++-ac-code

## 示例代码

```cpp
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        string keybord = "12210111011122000010020202";
        vector<string> res;
        int temp = 0, i;
        for(auto str : words){
            temp = keybord[tolower(str[0]) - 'a'];
            for(i = 1; i < str.size() && temp == keybord[tolower(str[i]) - 'a']; i++){}
            if(i == str.size())
                res.push_back(str);
        }
        return res;
    }
};
```