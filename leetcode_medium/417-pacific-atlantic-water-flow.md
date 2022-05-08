## 417. 太平洋大西洋水流问题

2022-04-27 11:08:52

### 题目

有一个 ``m × n`` 的矩形岛屿，与 **太平洋** 和 **大西洋** 相邻。 **“太平洋”** 处于大陆的左边界和上边界，而 **“大西洋”** 处于大陆的右边界和下边界。

这个岛被分割成一个由若干方形单元格组成的网格。给定一个 ``m x n`` 的整数矩阵 ``heights`` ， ``heights[r][c]`` 表示坐标 ``(r, c)`` 上单元格 **高于海平面的高度** 。

岛上雨水较多，如果相邻单元格的高度 **小于或等于** 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。

返回网格坐标 ``result`` 的 **2D列表** ，其中 ``result[i] = [r<sub>i</sub>, c<sub>i</sub>]`` 表示雨水可以从单元格 ``(ri, ci)`` 流向 **太平洋和大西洋** 。



**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg" />

```

输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**示例 2：**

```

输入: heights = [[2,1],[1,2]]
输出: [[0,0],[0,1],[1,0],[1,1]]
```



**提示：**


- ``m == heights.length``
- ``n == heights[r].length``
- ``1 <= m, n <= 200``
- ``0 <= heights[r][c] <= 10<sup>5</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/)

### 思路及代码

题目可能是英文直接翻译过来的，一开始读完题目没有 get 到关键点，题目本意是要计算在雨水自由流动的情况下可能到达两个海洋的格子数量。

这样看下来题目的实现思路还是比较简单的，对于左上方的海洋，从最上方和最左方的单元格开始向四个方向搜索高度大于自己的单元格并将其标记。对于右下方的海洋，按照相同的规则进行搜索。最后汇总两次搜索结果并返回。


```cpp
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int  m = heights.size();
        int n = heights[0].size();
        vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        vector<vector<bool>> flag(m, vector<bool>(n, 0));
        queue<int> q;

        for(int i = 0; i < m; i++)  {q.emplace(i * 200);}
        for(int i = 0; i < n; i++)  {q.emplace(i);}
        while(!q.empty()){
            int size = q.size();
            while(size--){
                int cur = q.front();
                q.pop();
                int i = cur / 200;
                int j = cur % 200;

                if(flag[i][j])  continue;
                flag[i][j] = true;
                for(int k = 0; k < 4; k++){
                    int next_i = i + directions[k][0];
                    int next_j = j + directions[k][1];

                    if(next_i >= 0 && next_i < m && next_j >= 0 && next_j < n && !flag[next_i][next_j] && heights[next_i][next_j] >= heights[i][j]){
                        q.emplace(next_i * 200 + next_j);
                    }
                }
            }
        }

        vector<vector<bool>> flag2(m, vector<bool>(n, 0));
        for(int i = 0; i < m; i++)  {q.emplace(i * 200 + n -1);}
        for(int i = 0; i < n; i++)  {q.emplace((m-1)*200 + i);}
        while(!q.empty()){
            int size = q.size();
            while(size--){
                int cur = q.front();
                q.pop();
                int i = cur / 200;
                int j = cur % 200;

                if(flag2[i][j])  continue;
                flag2[i][j] = true;
                for(int k = 0; k < 4; k++){
                    int next_i = i + directions[k][0];
                    int next_j = j + directions[k][1];

                    if(next_i >= 0 && next_i < m && next_j >= 0 && next_j < n && !flag2[next_i][next_j] && heights[next_i][next_j] >= heights[i][j]){
                        q.emplace(next_i * 200 + next_j);
                    }
                }
            }
        }

        vector<vector<int>> res;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(flag[i][j] && flag2[i][j]){
                    res.push_back({i, j});
                }
            }
        }
        return res;
    }
};
```