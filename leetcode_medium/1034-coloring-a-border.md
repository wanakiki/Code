## 1034. 边界着色

2021-12-07 09:14:37

### 题目

给你一个大小为 ``m x n`` 的整数矩阵 ``grid`` ，表示一个网格。另给你三个整数 ``row``、``col`` 和 ``color`` 。网格中的每个值表示该位置处的网格块的颜色。

当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一** 连通分量 **。

**连通分量的边界**** **是指连通分量中的所有与不在分量中的网格块相邻（四个方向上）的所有网格块，或者在网格的边界上（第一行/列或最后一行/列）的所有网格块。

请你使用指定颜色 ``color`` 为所有包含网格块 ``grid[row][col]`` 的 **连通分量的边界** 进行着色，并返回最终的网格 ``grid`` 。



**示例 1：**

```

输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
输出：[[3,3],[3,2]]
```

**示例 2：**

```

输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
输出：[[1,3,3],[2,3,3]]
```

**示例 3：**

```

输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
输出：[[2,2,2],[2,1,2],[2,2,2]]
```



**提示：**


- ``m == grid.length``
- ``n == grid[i].length``
- ``1 <= m, n <= 50``
- ``1 <= grid[i][j], color <= 1000``
- ``0 <= row < m``
- ``0 <= col < n``





[LeetCode链接](https://leetcode-cn.com/problems/coloring-a-border/)

### 思路及代码

深度优先搜索，需要额外使用一部分空间标记当前元素是否已经被访问过，如果节点满足四周存在边界或者其他颜色，则必定需要染色。

```cpp
class Solution {
public:
    vector<vector<int>> colorBorder(vector<vector<int>>& grid, int row, int col, int color) {
        int original_color = grid[row][col];
        vector<vector<int>> directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        stack<pair<int, int>> stk;
        vector<vector<bool>> flags(grid.size(), vector<bool>(grid[0].size(), false));       // 并不是所有访问过的点都需要染色，因此需要使用额外空间记录节点访问情况

        stk.push(make_pair(row, col));
        flags[row][col] = true;
        while(!stk.empty()){
            auto p = stk.top();
            stk.pop();

            int x = p.first, y = p.second;
            bool need_color = false;

            // 检查四个方向
            for(int i = 0; i < 4; i++){
                int cur_x = x + directions[i][0];
                int cur_y = y + directions[i][1];

                if(cur_x < 0 || cur_y < 0 || cur_x >= grid.size() || cur_y >= grid[0].size()){
                    need_color = true;
                }
                else{
                    // 先判断节点是否访问过 在判断节点颜色是否满足条件
                    // 先判断的原因是，连通区域内可能存在不需要改变颜色的节点
                    if(flags[cur_x][cur_y] == false){
                        if(grid[cur_x][cur_y] != original_color){
                            need_color = true;
                        }
                        else{
                            stk.push(make_pair(cur_x, cur_y));
                        flags[cur_x][cur_y] = true;
                        }
                    }
                }
            }

            if(need_color){
                grid[x][y] = color;
            }
        }
        return grid;
    }
};
```