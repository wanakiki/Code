## 516. 最长回文子序列

2021-08-12 10:02:59

### 题目

给你一个字符串 ``s`` ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

**示例 1：**

```
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
```

**示例 2：**

```
输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
```

 

**提示：**


- ``1 <= s.length <= 1000``
- ``s`` 仅由小写英文字母组成



[LeetCode链接](https://leetcode-cn.com/problems/longest-palindromic-subsequence/)

### 思路及代码

核心在于意识到回文字符串在去掉两侧元素之后仍然是回文字符串，根据这点便可通过动态规划方法求解。

需要注意的是动态规划时应优先访问较短的区间，最后访问较长的区间。

```cpp
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int len = s.size();
        vector<vector<int>> dp(len, vector<int>(len, 0));

        // 对角线初始为1
        for(int i = 0; i < len; i++)    dp[i][i] = 1;

        // 从短区间向长区间遍历
        for(int j = 1; j < len; j++){
            int x = 0, y = j;
            while(y < len){
                if(s[x] == s[y]){
                    dp[x][y] = dp[x+1][y-1] + 2;
                }
                else{
                    dp[x][y] = max(dp[x+1][y], dp[x][y-1]);
                }
                x++;
                y++;
            }
        }
        return dp[0][len-1];
    }
};
```