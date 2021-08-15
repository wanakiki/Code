## 576. 出界的路径数

2021-08-15 11:46:43

### 题目

给你一个大小为 ``m x n`` 的网格和一个球。球的起始坐标为 ``[startRow, startColumn]`` 。你可以将球移到在四个方向上相邻的单元
格内（可以穿过网格边界到达网格之外）。你 **最多** 可以移动 ``maxMove`` 次球。

给你五个整数 ``m``、``n``、``maxMove``、``startRow`` 以及 ``startColumn`` ，找出并返回可以将球移出边界的路径数量。因为答案
可能非常大，返回对 10<sup>9</sup> + 7 **取余** 后的结果。



**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png" style="width: 500px; height: 
296px;" />

```
输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
输出：6
```

**示例 2：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png" style="width: 500px; height: 
293px;" />

```
输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
输出：12
```



**提示：**


- ``1 <= m, n <= 50``
- ``0 <= maxMove <= 50``
- ``0 <= startRow < m``
- ``0 <= startColumn < n``



[LeetCode链接](https://leetcode-cn.com/problems/out-of-boundary-paths/)

### 思路及代码

动态规划

```cpp
class Solution {
public:
    int directions[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        vector<vector<int>> old_status(m, vector<int>(n, 0));
        int res = 0;

        // 初始化位置
        old_status[startRow][startColumn] = 1;

        for(int k = 0; k < maxMove; k++){
            // 检测老状态有多少可以直接出界
            for(int i = 0; i < n; i++){
                if(old_status[0][i]){
                    res += old_status[0][i];
                    res %= 1000000007;    
                }
                if(old_status[m-1][i]){
                    res += old_status[m-1][i];
                    res %= 1000000007;
                }
            }

            for(int i = 0; i < m; i++){
                if(old_status[i][0]){
                    res += old_status[i][0];
                    res %= 1000000007;
                }
                if(old_status[i][n-1]){
                    res += old_status[i][n-1];
                    res %= 1000000007;
                }
            }

            // 最后一次循环不需要计算新状态
            if(k == maxMove - 1)    break;

            // 计算新状态
            vector<vector<int>> new_status(m, vector<int>(n, 0));
            for(int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    if(old_status[i][j]){
                        // 增加相邻网格值
                        for(int t = 0; t < 4; t++){
                            int next_i = i + directions[t][0];
                            int next_j = j + directions[t][1];
                            if(next_i < 0 || next_j < 0 || next_i >= m || next_j >= n){
                                continue;
                            }

                            new_status[next_i][next_j] += old_status[i][j];
                            new_status[next_i][next_j] %= 1000000007;
                        }
                    }
                }
            }

            // 状态转移
            for(int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    old_status[i][j] = new_status[i][j];
                }
            }
        }
        return res;
    }
};
```