## 205. Isomorphic Strings
##### 2018-06-08 22:04:52
##### 并非map
***
## 题目
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
```
Input: s = "egg", t = "add"
Output: true
```
Example 2:
```
Input: s = "foo", t = "bar"
Output: false
```
Example 3:
```
Input: s = "paper", t = "title"
Output: true
```
Note:
You may assume both s and t have the same length.

## 分析
面向对象节课的一道考试题，当时以为能够用map解决，遍历一个元素 map++，实际上并不需要这样（这样也会出错），只要记住上一个元素的位置，判断是否相等就可以解决，很简单。
## 示例代码
```cpp
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int m1[256] = {0}, m2[256] = {0}, n = s.size();
        for (int i = 0; i < n; ++i) {
            if (m1[s[i]] != m2[t[i]]) return false;
            m1[s[i]] = i + 1;
            m2[t[i]] = i + 1;
        }
        return true;
    }
};
```
