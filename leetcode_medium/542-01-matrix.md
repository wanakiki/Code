## 542. 01 矩阵

2020年4月15日

### 题目

给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
```no
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
```
示例 2:
```no
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
```
注意:

1. 给定矩阵的元素个数不超过 10000。
2. 给定矩阵中至少有一个元素是 0。
3. 矩阵中的元素只在四个方向上相邻: 上、下、左、右。

来源：力扣（LeetCode）  
链接：https://leetcode-cn.com/problems/01-matrix  

### 代码

两个解题思路，都很巧秒。

多起点广搜，能够解决矩阵中有多个零时进行广搜相互覆盖的问题，效率提升很多。

```cpp
class Solution {
public:
    int directions[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        vector<vector<int>> res;
        if(matrix.size() == 0)
            return res;
        int row = matrix.size(), col = matrix[0].size();
        res.resize(row, vector<int>(col));
        vector<vector<bool> > visit(row, vector<bool>(col, false));
        queue<pair<int,int>> myque;

        // 获取初始零点
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(matrix[i][j] == 0){
                    myque.emplace(i, j);
                    visit[i][j] = true;
                    res[i][j] = 0;
                }
            }
        }
        // 广搜
        while(!myque.empty()){
            auto [i, j] = myque.front();    // 方便的写法
            myque.pop();
            int tmp = res[i][j] + 1;
            for(int k = 0; k < 4; k++){
                int next_i = i + directions[k][0];
                int next_j = j + directions[k][1];
                if(next_i >=0 && next_j >= 0 && next_i < row && next_j < col && !visit[next_i][next_j]){
                    visit[next_i][next_j] = true;
                    res[next_i][next_j] = tmp;
                    myque.emplace(next_i, next_j);
                }
            }
        }
        return res;
    }
};
```

两个方向DP

```cpp
class Solution {
public:
    int directions[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        if(matrix.size() == 0)
            return vector<vector<int>> ();
        int row = matrix.size(), col = matrix[0].size();
        vector<vector<int>> res(row, vector<int>(col, 10000));  // 用INT_MAX会溢出
        
        // 找到所有零
        for(int i = 0; i < row; i++)
        for(int j = 0; j < col; j++){
            if(matrix[i][j] == 0)
                res[i][j] = 0;
        }

        // 向右下dp
        for(int i = 0; i < row; i++)
        for(int j = 0; j < col; j++){
            if(i-1 >= 0)
                res[i][j] = min(res[i-1][j]+1, res[i][j]);
            if(j-1 >= 0)
                res[i][j] = min(res[i][j-1]+1, res[i][j]);
        }

        // 向左上dp
        for(int i = row-1; i >= 0; i--)
        for(int j = col-1; j >= 0; j--){
            if(i+1 < row)
                res[i][j] = min(res[i+1][j]+1, res[i][j]);
            if(j+1 < col)
                res[i][j] = min(res[i][j+1]+1, res[i][j]);
        }

        return res;
    }
};
```