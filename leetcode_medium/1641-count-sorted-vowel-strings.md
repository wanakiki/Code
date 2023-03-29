## 1641. 统计字典序元音字符串的数目

2023-03-29 10:45:58

### 题目

给你一个整数 ``n``，请返回长度为 ``n`` 、仅由元音 (``a``, ``e``, ``i``, ``o``, ``u``) 组成且按 **字典序排列** 的字符串数量。

字符串 ``s`` 按 **字典序排列** 需要满足：对于所有有效的 ``i``，``s[i]`` 在字母表中的位置总是与 ``s[i+1]`` 相同或在 ``s[i+1]`` 之前。

 

**示例 1：**

```

输入：n = 1
输出：5
解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]
```

**示例 2：**

```

输入：n = 2
输出：15
解释：仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
```

**示例 3：**

```

输入：n = 33
输出：66045
```

 

**提示：**


- ``1 <= n <= 50`` 



[LeetCode链接](https://leetcode-cn.com/problems/count-sorted-vowel-strings/)

### 思路及代码

简单的动态规划题目，dp[i][j]代表以 i 结尾，总长度为 j 的可能组合数。在空间上还能进一步优化，只使用五个变量存储数值。

```cpp
class Solution {
public:
    int countVowelStrings(int n) {
        vector<vector<int>> dp(5, vector<int>(n, 0));
        for(int i = 0; i < 5; i++){
            dp[i][0] = 1;
        }

        for(int i = 1; i < n; i++){
            for(int j = 0; j < 5; j++){
                if(j == 0){
                    dp[j][i] = dp[j][i-1];
                }
                else{
                    dp[j][i] = dp[j-1][i] + dp[j][i-1];
                }
            }
        }

        int res = 0;
        for(int i = 0; i < 5; i++){
            res += dp[i][n-1];
        }
        return res;
    }
};
```