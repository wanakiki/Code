## 1765. 地图中的最高点

2022-01-29 11:17:35

### 题目

给你一个大小为 ``m x n`` 的整数矩阵 ``isWater`` ，它代表了一个由 **陆地** 和 **水域** 单元格组成的地图。


- 如果 ``isWater[i][j] == 0`` ，格子 ``(i, j)`` 是一个 **陆地** 格子。
- 如果 ``isWater[i][j] == 1`` ，格子 ``(i, j)`` 是一个 **水域** 格子。


你需要按照如下规则给每个单元格安排高度：


- 每个格子的高度都必须是非负的。
- 如果一个格子是是 **水域** ，那么它的高度必须为 ``0`` 。
- 任意相邻的格子高度差 **至多** 为 ``1`` 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）


找到一种安排高度的方案，使得矩阵中的最高高度值 **最大** 。

请你返回一个大小为 ``m x n`` 的整数矩阵 ``height`` ，其中 ``height[i][j]`` 是格子 ``(i, j)`` 的高度。如果有多种解法，请返回 **任意一个** 。

 

**示例 1：**

**<img alt="" src="https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82045-am.png" style="width: 220px; height: 219px;" />**

```
输入：isWater = [[0,1],[0,0]]
输出：[[1,0],[2,1]]
解释：上图展示了给各个格子安排的高度。
蓝色格子是水域格，绿色格子是陆地格。
```

**示例 2：**

**<img alt="" src="https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82050-am.png" style="width: 300px; height: 296px;" />**

```
输入：isWater = [[0,0,1],[1,0,0],[0,0,0]]
输出：[[1,1,0],[0,1,1],[1,2,2]]
解释：所有安排方案中，最高可行高度为 2 。
任意安排方案中，只要最高高度为 2 且符合上述规则的，都为可行方案。
```

 

**提示：**


- ``m == isWater.length``
- ``n == isWater[i].length``
- ``1 <= m, n <= 1000``
- ``isWater[i][j]`` 要么是 ``0`` ，要么是 ``1`` 。
- 至少有 **1** 个水域格子。



[LeetCode链接](https://leetcode-cn.com/problems/map-of-highest-peak/)

### 思路及代码

题目核心点在于，每个非水域格子的最大高度等于该格子到最近水域格子的最小距离。

超时做法：统计所有水域格子位置，再遍历地图计算非水域格子与所有水域格子的距离，保留最小值并更新。

```cpp
class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        vector<vector<int>> water_point;
        vector<vector<int>> res(isWater.size(), vector<int>(isWater[0].size(), 1));

        for(int i = 0; i < isWater.size(); i++){
            for(int j = 0; j < isWater[0].size(); j++){
                if(isWater[i][j] == 1){
                    res[i][j] == 0;
                    water_point.push_back({i, j});
                }
            }
        }

        for(int i = 0; i < isWater.size(); i++){
            for(int j = 0; j < isWater[0].size(); j++){
                if(res[i][j] == 0)  continue;

                int min_distance = INT_MAX;
                for(int k = 0; k < water_point.size(); k++){
                    int cur_distance = abs(i - water_point[k][0]) + abs(j - water_point[k][1]);
                    min_distance = min(min_distance, cur_distance);
                }
                res[i][j] = min_distance;
            }
        }
        return res;
    }
};
```

算法复杂度为O(mn·k)，k为水域格子的数目。在上述做法超时之后，无法找到有效做法缩短查找最小距离所需复杂度，如果轮流以水域节点开始搜索又会导致有大量搜索面积的重复。

不得以查看题解，发现这类问题是经典多源广度优先搜索题目，只要在第一轮同时把所有的水域格子入队，就能保证同时计算距离水域格子相同距离的情况，避免了搜索面积覆盖。

```cpp
class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        queue<pair<int, int>> q;
        vector<vector<int>> res(isWater.size(), vector<int>(isWater[0].size(), -1));
        vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for(int i = 0; i < isWater.size(); i++){
            for(int j = 0; j < isWater[0].size(); j++){
                if(isWater[i][j] == 1){
                    q.push(make_pair(i, j));
                }
            }
        }

        int cur_index = 0;
        while(!q.empty()){
            int count = q.size();
            while(count--){
                auto p = q.front();
                q.pop();

                int x = p.first;
                int y = p.second;

                if(x < 0 || x >= res.size() || y < 0 || y >= res[0].size() || res[x][y] != -1) continue;
                res[x][y] = cur_index;
                for(int i = 0; i < 4; i++){
                    q.push(make_pair(x + directions[i][0], y + directions[i][1]));
                }
            }
            cur_index++;
        }
        return res;
    }
};
```