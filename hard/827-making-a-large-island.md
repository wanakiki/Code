## 854. 最大人工岛

2022-09-18 10:30:33

### 题目

给你一个大小为 ``n x n`` 二进制矩阵 ``grid`` 。**最多** 只能将一格 ``0`` 变成 ``1`` 。

返回执行此操作后，``grid`` 中最大的岛屿面积是多少？

**岛屿** 由一组上、下、左、右四个方向相连的 ``1`` 形成。

 

**示例 1:**

```

输入: grid = [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
```

**示例 2:**

```

输入: grid = [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。
```

**示例 3:**

```
输入: grid = [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。
```

 

**提示：**


- ``n == grid.length``
- ``n == grid[i].length``
- ``1 <= n <= 500``
- ``grid[i][j]`` 为 ``0`` 或 ``1``



[LeetCode链接](https://leetcode-cn.com/problems/making-a-large-island/)

### 思路及代码

虽然是hard，但是思路较为简单。

遍历数组，使用并查集维护联通岛屿和岛屿的面积。二次遍历数组，对于每个数值为零的位置，查找四周的岛屿情况，并使用集合进行去重，去重后累加周围岛屿的面积，即在当前位置进行修改后得到的新岛屿面积。

由于题目数据中可能不包含零，需要在第一次遍历的时候维护所及的最大岛屿面积。需要注意的是，如果数据全为零，则对应最小最终结果1。

```cpp
class Solution {
public:
    vector<int> parent;
    int findx(int x){
        if(parent[x] != x){
            parent[x] = findx(parent[x]);
        }
        return parent[x];
    }
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        parent.resize(n * n);
        iota(parent.begin(), parent.end(), 0);
        vector<int> island_size(n * n, 1);  // 面积初始值为1

        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        int res = 1;    // 变化一次后最小面积为1

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j]){
                    int pa = findx(i * n + j);
                    for(int k = 0; k < 4; k++){
                        int next_i = i + directions[k][0];
                        int next_j = j + directions[k][1];

                        if(next_i >= 0 && next_j >= 0 && next_i < n && next_j < n && grid[next_i][next_j]){
                            int pb = findx(next_i * n + next_j);

                            if(pa != pb){
                                parent[pb] = pa;
                                island_size[pa] += island_size[pb];
                                res = max(res, island_size[pa]);
                            }
                        }
                    }
                }
            }
        }

        // 查找空岛附近的有效岛屿
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(!grid[i][j]){

                    unordered_set<int> uset;    // 对周围的岛屿进行去重

                    for(int k = 0; k < 4; k++){
                        int next_i = i + directions[k][0];
                        int next_j = j + directions[k][1];

                        if(next_i >= 0 && next_j >= 0 && next_i < n && next_j < n && grid[next_i][next_j]){
                            int pb = findx(next_i * n + next_j);
                            uset.emplace(pb);
                        }
                    }

                    // 计算去重后的岛屿总面积
                    int total_area = 0;
                    for(auto val : uset){
                        total_area += island_size[val];
                    }
                    res = max(res, 1 + total_area);
                }
            }
        }
        return res;
    }
};
```