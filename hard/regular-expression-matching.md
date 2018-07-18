## 10. Regular Expression Matching
##### 2018年6月28日
##### 通配符匹配
***
## 题目
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```
The matching should cover the entire input string (not partial).

Note:

- s could be empty and contains only lowercase letters a-z.
- p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```
Example 2:
```
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```
Example 3:
```
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```
Example 4:
```
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
```
Example 5:
```
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```
## 分析
这道题看起来简单，实际上做起来还是很复杂的，我去网上看了别人的代码发现了用while循环实现类似递归的解决方式的代码，理解了思路提交发现这个问题的难度已经有了变化，原来的代码思路无法提交。（无法解决例四的问题）

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int len1=s.size(), len2=p.size();
        if(len1 == 0 && len2 ==0)
            return true;
        int si = 0, pi = 0;
        int last_p = -1, last_s = -1;

        while(si < len1){
            if(pi < len2 && (p[pi] == '*')){
                last_p = pi++;
                last_s = si;
            }
            else if(pi < len2 && (p[pi] == s[si] || p[pi] == '.')){
                pi++;
                si++;
            }
            else if(last_p > -1){
                pi = last_p + 1;
                si = ++last_s;
            }
            else{
                return false;
            }
        }

        while(pi < len2 && p[pi] == '*')
            pi++;
        return pi==len2;
    }
};
```
