## 242. Valid Anagram
##### 2018年7月15日
***
### 题目
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```
Example 2:
```
Input: s = "rat", t = "car"
Output: false
```
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
### 分析
简单的题目，排序之后判断就可以了，不过这样做不是很快...
### 示例代码
C++：
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size())
            return false;
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};
```

用哈希表统计并判断。

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> myhash;
        for(int i = 0; i < s.size(); i++){
            myhash[s[i]]++;
        }
        unordered_map<char, int> myhash_t;
        for(int i = 0; i < t.size(); i++){
            myhash_t[t[i]]++;
        }
        return myhash_t == myhash;
    }
};
```