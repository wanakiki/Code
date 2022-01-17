## 1332. 统计元音字母序列的数目

2022-01-17 11:09:24

### 题目

给你一个整数 ``n``，请你帮忙统计一下我们可以按下述规则形成多少个长度为 ``n`` 的字符串：


- 字符串中的每个字符都应当是小写元音字母（``'a'``, ``'e'``, ``'i'``, ``'o'``, ``'u'``）
- 每个元音 ``'a'`` 后面都只能跟着 ``'e'``
- 每个元音 ``'e'`` 后面只能跟着 ``'a'`` 或者是 ``'i'``
- 每个元音 ``'i'`` 后面 **不能** 再跟着另一个 ``'i'``
- 每个元音 ``'o'`` 后面只能跟着 ``'i'`` 或者是 ``'u'``
- 每个元音 ``'u'`` 后面只能跟着 ``'a'``


由于答案可能会很大，所以请你返回 模 ``10^9 + 7`` 之后的结果。



**示例 1：**

```
输入：n = 1
输出：5
解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
```

**示例 2：**

```
输入：n = 2
输出：10
解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。  
```

**示例 3：**

```
输入：n = 5
输出：68
```



**提示：**


- ``1 <= n <= 2 * 10^4``



[LeetCode链接](https://leetcode-cn.com/problems/count-vowels-permutation/)

### 思路及代码

采用动态规划做法，求解长度为n时以各个字母为末尾的字符串的个数。设当前长度为i，则当前长度的所有可能仅与长度为i-1时的数据相关，可优化空间。

另外也可以直接通过矩阵快速幂实现。

```cpp
class Solution {
public:
    int countVowelPermutation(int n) {
        vector<int> old = {1, 1, 1, 1, 1};
        vector<int> new_dp(5, 0);
        int cur = 1;
        int mask = 1000000007;
        while(cur < n){
            cur++;

            new_dp[0] = ((old[1] + old[2]) % mask + old[4]) % mask;
            new_dp[1] = (old[0] + old[2]) % mask;
            new_dp[2] = (old[1] + old[3]) % mask;
            new_dp[3] = (old[2]);
            new_dp[4] = (old[2] + old[3]) % mask;
            old = new_dp;
        }

        int res = 0;
        for(auto num : old){
            res += num;
            res %= mask;
        }
        return res;
    }
};
```