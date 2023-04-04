## 1000. 合并石头的最低成本

2023-04-04 11:04:20

### 题目

有 ``N`` 堆石头排成一排，第 ``i`` 堆中有 ``stones[i]`` 块石头。

每次<em>移动（move）</em>需要将**连续的** ``K`` 堆石头合并为一堆，而这个移动的成本为这 ``K`` 堆石头的总数。

找出把所有石头合并成一堆的最低成本。如果不可能，返回 ``-1`` 。

 

**示例 1：**

```
输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。
```

**示例 2：**

```
输入：stones = [3,2,4,1], K = 3
输出：-1
解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
```

**示例 3：**

```
输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。
```

 

**提示：**


- ``1 <= stones.length <= 30``
- ``2 <= K <= 30``
- ``1 <= stones[i] <= 100``



[LeetCode链接](https://leetcode-cn.com/problems/minimum-cost-to-merge-stones/)

### 思路及代码

比较经典的区间动态规划题目，花了一些时间想明白状态转移。

首先合成代价是固定的，可以使用前缀和在常数时间求出来。对于k等于2的情况，令 dp[l][r] 代表将区间合成为 1 堆的最小代价，容易想到将整个区间划分为两个部分，对每个部分递归求解后合并，即 $dp[l][r] = min\{dp[l][p] + dp[p + 1][r] + sum(l, r)\}$ 其中 $p$ 是所有可能的区间切分位置。

题目的难点在于 k 是不定的，导致上述状态转移关系变得复杂，个人目前的能力只停留在 k 为 2 的情况。查看官方题解之后，发现采用了一个比较巧妙的写法，采用三维dp，令 $$dp[l][r][1] = dp[l][r][k] + sum(l, r) \\ dp[l][r][t] = min\{dp[l][p][1] + dp[p+1][r][t-1]\}$$

其中 $dp[l][r][t]$ 代表了将当前区间合并为 t 堆需要的总代价：
- 仅在 t 为 1 时才会执行区间合并，需要计算出当前区间合并为 k 堆的代价和区间元素的总和。
- 如果 t 不为 1，则尝试将区间分片，这里将目标堆数分成了 1 堆和 t - 1 堆，伴随动态规划的深入，所有可能的堆数分配均会被访问到，是很巧妙的一步。
  > 假定 k 为 2，则需要把整个区间合并为 2 堆，对应 （1, 1)
  > 假定 k 为 3，则需要把整个区间合并为 3 堆，由于将整体切分为 (1, t-1) 伴随区间长度的变化，所有可能的区间分配均会被访问到

```cpp
class Solution {
   public:
    int helper(vector<int>& stones, vector<vector<vector<int>>>& dp, int l,
               int r, int t, int k) {
        if(dp[l][r][t] != -1)
            return dp[l][r][t];
        
        // t 始终小于等于 k
        int cur_len = r - l + 1;

        // 如果当前长度小于 t 不可能合并出 t 堆
        if(cur_len < t)
            return dp[l][r][t] = INT_MAX;
        
        if(t == 1){
            // 如果要合成一堆 则应该计算出当前区间合并出k堆的最小代价 + 合并区间k堆需要的代价
            int res = helper(stones, dp, l, r, k, k);
            if(res == INT_MAX)
                return dp[l][r][t] = INT_MAX;
            else    
                return dp[l][r][t] = res + getPre(l, r);
        }
        else{
            // 如果要合成多堆 则开始尝试分割点
            int res = INT_MAX;
            for(int i = l; i < r; i++){
                // 分割点在 i 处
                int left = helper(stones, dp, l, i, 1, k);
                int right = helper(stones, dp, i + 1, r, t - 1, k);
                if(left == INT_MAX || right == INT_MAX)
                    continue;
                res = min(res, left + right);
            }

            return dp[l][r][t] = res;
        }
    }
    vector<int> pre;
    int getPre(int l, int r) {
        if (l == 0)
            return pre[r];
        else
            return pre[r] - pre[l - 1];
    }
    int mergeStones(vector<int>& stones, int k) {
        int len = stones.size();
        vector<vector<vector<int>>> dp(len, vector<vector<int>>(len, vector<int>(k + 1, -1)));
        for (int i = 0; i < len; i++) {
            if (i == 0)
                pre.push_back(stones[i]);
            else {
                pre.push_back(stones[i] + pre[i - 1]);
            }
        }

        for(int i = 0; i < len; i++){
            dp[i][i][1] = 0;
        }
        int res = helper(stones, dp, 0, len - 1,1, k);
        return res == INT_MAX ? -1 : res;
    }
};
```

由于题目限定了合并的长度，上面的做法还可以进一步优化。