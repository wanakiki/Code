## 1873. 最长的美好子字符串

2022-02-01 10:49:59

### 题目

当一个字符串 ``s`` 包含的每一种字母的大写和小写形式 **同时** 出现在 ``s`` 中，就称这个字符串 ``s`` 是 
**美好** 字符串。比方说，``"abABB"`` 是美好字符串，因为 ``'A'`` 和 ``'a'`` 同时出现了，且 ``'B'`` 和 ``'b'`` 也同时出现了。然而，``"abA"`` 不是美好字符串因为 ``'b'`` 出现了，而 ``'B'`` 没有出现。

给你一个字符串 ``s`` ，请你返回 ``s`` 最长的 **美好子字符串** 。如果有多个答案，请你返回 **最早** 出现
的一个。如果不存在美好子字符串，请你返回一个空字符串。

 

**示例 1：**

```
输入：s = "YazaAay"
输出："aAa"
解释："aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
"aAa" 是最长的美好子字符串。
```

**示例 2：**

```
输入：s = "Bb"
输出："Bb"
解释："Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。
```

**示例 3：**

```
输入：s = "c"
输出：""
解释：没有美好子字符串。
```

**示例 4：**

```
输入：s = "dDzeE"
输出："dD"
解释："dD" 和 "eE" 都是最长美好子字符串。
由于有多个美好子字符串，返回 "dD" ，因为它出现得最早。
```

 

**提示：**


- ``1 <= s.length <= 100``
- ``s`` 只包含大写和小写英文字母。



[LeetCode链接](https://leetcode-cn.com/problems/longest-nice-substring/)

### 思路及代码

新年的第一道题目，虽然标记是简单题但也有一些能深度挖掘的点👍。

看到题目第一眼想到的做法是滑动窗口，脑子里面简单推导之后发现窗长改变函数有点难写，即使当前长度不满足，对其进行延长之后可能会满足。按这个想法继续下去，就变成了暴力做法。

```cpp
class Solution {
public:
    bool helper(vector<int>& a, vector<int>& b){
        for(int i = 0; i < 26; i++){
            if(a[i] != b[i])    return false;
        }
        return true;
    }
    string longestNiceSubstring(string s) {
        int max_len = -1;
        int max_index = -1;

        for(int i = 0; i < s.size(); i++){
            vector<int> upper(26, 0);
            vector<int> lower(26, 0);

            for(int j = i; j < s.size(); j++){
                if(s[j] >= 'a'){
                    lower[s[j] - 'a'] = 1;
                }
                else{
                    upper[s[j] - 'A'] = 1;
                }

                if(helper(lower, upper) && j - i + 1 > max_len){
                    max_len = j - i + 1;
                    max_index = i;
                }
            }
        }
        if(max_index == -1) return "";
        return s.substr(max_index, max_len);
    }
};
```

本以为上面的暴力做法会超时，但题目总数据量不是很大，时间卡的不严格，最终还是通过了。

查看题解之后，发现上面的暴力做法可以用状态压缩优化，将数组用两个整数进行替代，每一位标志是否有对应字母，直接判断是否相等即可。

```cpp
class Solution {
public:
    string longestNiceSubstring(string s) {
        int max_len = -1;
        int max_index = -1;

        for(int i = 0; i < s.size(); i++){
            int upper = 0;
            int lower = 0;
            for(int j = i; j < s.size(); j++){
                if(s[j] >= 'a'){
                    lower |= 1 << (s[j] - 'a');
                }
                else{
                    upper |= 1 << (s[j] - 'A');
                }

                if(lower == upper && j - i + 1 > max_len){
                    max_len = j - i + 1;
                    max_index = i;
                }
            }
        }
        if(max_index == -1) return "";
        return s.substr(max_index, max_len);
    }
};
```

除此之外，官方题解还给出了使用分治和滑动窗口的解题方案，以后有时间需要继续研究下。