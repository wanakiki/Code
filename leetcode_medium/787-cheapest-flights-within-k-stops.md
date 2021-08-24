## 787. K 站中转内最便宜的航班

2021-08-24 21:53:19

### 题目

有 ``n`` 个城市通过一些航班连接。给你一个数组 ``flights`` ，其中 ``flights[i] = [from<sub>i</sub>, to<sub>i</sub>, price<sub>i</sub>]`` ，表示该航班都从城市 ``from<sub>i</sub>`` 开始，以价格 ``price<sub>i</sub>`` 抵达 ``to<sub>i</sub>``。      

现在给定所有的城市和航班，以及出发城市 ``src`` 和目的地 ``dst``，你的任务是找到出一条最多经过 ``k`` 站中转的路线，使得从 ``src`` 到 ``dst`` 的 **价格最便宜** ，并返回该价格。 如果不存在这样的路线，则输出 ``-1``。



**示例 1：**

```

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200
解释:
城市航班图如下
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 180px; width: 246px;" />
从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。```

**示例 2：**

```

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出: 500
解释:
城市航班图如下
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 180px; width: 246px;" />
从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。```



**提示：**


- ``1 <= n <= 100``
- ``0 <= flights.length <= (n * (n - 1) / 2)``
- ``flights[i].length == 3``
- ``0 <= from<sub>i</sub>, to<sub>i</sub> < n``
- ``from<sub>i</sub> != to<sub>i</sub>``
- ``1 <= price<sub>i</sub> <= 10<sup>4</sup>``
- 航班没有重复，且不存在自环
- ``0 <= src, dst, k < n``
- ``src != dst``



[LeetCode链接](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/)

### 思路及代码

动态规划，逐级推断中转次数为k时到达终点的距离。

```cpp
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<int>> dp(k + 2, vector<int>(n, 10000000));
        dp[0][src] = 0;
        for(int i = 1; i < dp.size(); i++){
            dp[i][src] = 0;
            for(int t = 0; t < flights.size(); t++){
                int from = flights[t][0];
                int to = flights[t][1];
                int w = flights[t][2];
                if(to == src)   continue;   // 避免再次回到起点
                dp[i][to] = min(dp[i][to], dp[i-1][from] + w);
            }
        }
        return dp[k+1][dst] == 10000000 ? -1 : dp[k+1][dst];
    }
};
```