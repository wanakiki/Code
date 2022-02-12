## 1020. 飞地的数量

2022-02-12 10:00:32

### 题目

给你一个大小为 ``m x n`` 的二进制矩阵 ``grid`` ，其中 ``0`` 表示一个海洋单元格、``1`` 表示一个陆地单元格。

一次 **移动** 是指从一个陆地单元格走到另一个相邻（**上、下、左、右**）的陆地单元格或跨过 ``grid`` 的边界。

返回网格中**无法**在任意次数的移动中离开网格边界的陆地单元格的数量。



**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg" style="height: 200px; width: 200px;" />
```
输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
```

**示例 2：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg" style="height: 200px; width: 200px;" />
```
输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。
```



**提示：**


- ``m == grid.length``
- ``n == grid[i].length``
- ``1 <= m, n <= 500``
- ``grid[i][j]`` 的值为 ``0`` 或 ``1``



[LeetCode链接](https://leetcode-cn.com/problems/number-of-enclaves/)

### 思路及代码

从边界为1的格子出发，搜索相邻数值为1的格子，并将其标记为零。在处理完四个边界之后，统计整个网格还有多少格子仍旧为1，对应题目答案。

```cpp
class Solution {
public:
    vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    void helper(vector<vector<int>>& grid, int x, int y){
        if(x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size() || grid[x][y] == 0) return ;
        grid[x][y] = 0;
        for(int i = 0; i < 4; i++){
            int next_x = x + directions[i][0];
            int next_y = y + directions[i][1];

            helper(grid, next_x, next_y);
        }
        return ;
    }
    int numEnclaves(vector<vector<int>>& grid) {
        // 寻找边界陆地单元格
        int tmp = grid.size() - 1;
        for(int i = 0; i < grid[0].size(); i++){
            if(grid[0][i] == 1) helper(grid, 0, i);
            if(grid[tmp][i] == 1)   helper(grid, tmp, i);
        }

        tmp = grid[0].size() - 1;
        for(int i = 0; i < grid.size(); i++){
            if(grid[i][0] == 1) helper(grid, i, 0);
            if(grid[i][tmp] == 1)   helper(grid, i, tmp);
        }

        // 计数未被处理单元格
        int res = 0;
        for(int i = 1; i < grid.size() - 1; i++){
            for(int j = 1; j < grid[0].size() - 1; j++){
                if(grid[i][j])  res++;
            }
        }
        return res;
    }
};
```