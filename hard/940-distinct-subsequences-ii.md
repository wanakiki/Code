## 940. 不同的子序列 II

2022-10-14 10:09:10

### 题目

给定一个字符串 ``s``，计算 ``s`` 的 **不同非空子序列** 的个数。因为结果可能很大，所以返回答案需要对** ****``10^9 + 7`` 取余** 。

字符串的 **子序列** 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。


- 例如，``"ace"`` 是 "<em>**a**</em>b<em>**c**</em>d<em>**e**</em>" 的一个子序列，但 ``"aec"`` 不是。




**示例 1：**

```
输入：s = "abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
```

**示例 2：**

```
输入：s = "aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
```

**示例 3：**

```
输入：s = "aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。
```



**提示：**


- ``1 <= s.length <= 2000``
- ``s`` 仅由小写英文字母组成





[LeetCode链接](https://leetcode-cn.com/problems/distinct-subsequences-ii/)

### 思路及代码

对于以相同字符结尾的子序列，结尾位置靠前的子序列集合必然是结尾靠后子序列集合的子集。采用动态规划做法，以新字符构成的子序列个数等于在这之前以26个字母结尾构成的子序列个数之和再加1。

```cpp
class Solution {
public:
    int getSum(vector<int>& last_pos, vector<int>& dp){
        long long res = 0;
        for(int i = 0; i < last_pos.size(); i++){
            if(last_pos[i] != -1){
                res += dp[last_pos[i]];
                res %= 1000000007;
            }
        }
        return res;
    }
    int distinctSubseqII(string s) {
        vector<int> last_pos(26, -1);
        vector<int> dp(s.size(), 0);

        for(int i = 0; i < s.size(); i++){
            dp[i] = 1 + getSum(last_pos, dp);

            last_pos[s[i] - 'a'] = i;
        }

        return getSum(last_pos, dp);
    }
};
```