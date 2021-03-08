## 132. 分割回文串 II

2021-03-08 11:08:27

### 题目

给你一个字符串 ``s``，请你将 ``s`` 分割成一些子串，使每个子串都是回文。

返回符合要求的 **最少分割次数** 。


**示例 1：**

```
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
```

**示例 2：**

```
输入：s = "a"
输出：0
```

**示例 3：**

```
输入：s = "ab"
输出：1
```


**提示：**

- ``1 <= s.length <= 2000``
- ``s`` 仅由小写英文字母组成



[LeetCode链接](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)

### 思路及代码

受到[131题分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)影响首先想到的就是回溯方法，普通方法超时后又尝试了剪枝，结果又超时了，感觉问题主要出在递归过程中的大量开销。

```cpp
class Solution {
public:
    int res;
    void helper(string s, int start, int cur, vector<vector<int>>& dp){
        if(cur > res){return ;}
        
        if(start == s.size()){
            if(cur != 0){
                res = min(res, cur-1);
            }
            else{
                res = 0;
            }
        }
        else{
            for(int i = s.size()-1; i >= start; i--){
                if(dp[start][i]){
                    helper(s, i+1, cur+1, dp);
                }
            }
        }
    }
    int minCut(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 1));
        for(int i = n - 1; i >= 0; i--){
            for(int j = i + 1; j < n; j++){
                dp[i][j] = dp[i+1][j-1] && (s[i] == s[j]);
            }
        }

        res = n;
        helper(s, 0, 0, dp);
        return res;
    }
};
```

看了题解才发现想法偏离了方向，本题目没要求返回分割的具体可能情况，而是要求最少的分割次数，更适合用动态规划来做。

首先按照131题的方法预处理字符串，确保能够在O(1)时间内查找某个子串是否为回文。之后用动态规划来进行解题，假定$f[i]$代表到i位置的最少分割次数，则其应满足：

$$f[i] = min\{f[i]|-1\le j < i, s[j+1...i]\,is\, palindrome\}$$

考虑到$j=-1$时对应的判断为$s[0...i]$是否为回文，该情况分割次数必然最少，可以优先判断，一旦成立则不需要考虑剩余可能情况。

```cpp
class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 1));
        for(int i = n - 1; i >= 0; i--){
            for(int j = i + 1; j < n; j++){
                dp[i][j] = dp[i+1][j-1] && (s[i] == s[j]);
            }
        }

        vector<int> f(n, n);
        for(int i = 0; i < n; i++){
            if(dp[0][i]){
                f[i] = 0;
            }
            else{
                for(int j = 0; j < i; j++){
                    if(dp[j+1][i]){
                        f[i] = min(f[i], f[j] + 1);
                    }
                }
            }
        }
        return f[n-1];
    }
};
```