## 764. 最大加号标志

2022-11-09 09:15:15

### 题目

在一个 ``n x n`` 的矩阵 ``grid`` 中，除了在数组 ``mines`` 中给出的元素为 ``0``，其他每个元素都为 ``1``。``mines[i] = [x<sub>i</sub>, y<sub>i</sub>]``表示 ``grid[x<sub>i</sub>][y<sub>i</sub>] == 0``

返回**``grid``<em> 中包含 ``1`` 的最大的 **轴对齐** 加号标志的阶数</em> 。如果未找到加号标志，则返回 ``0`` 。

一个 ``k`` 阶由*``1``</em> 组成的 **“轴对称”加号标志** 具有中心网格 ``grid[r][c] == 1`` ，以及4个从中心向上、向下、向左、向右延伸，长度为 ``k-1``，由 ``1`` 组成的臂。注意，只有加号标志的所有网格要求为 ``1`` ，别的网格可能为 ``0`` 也可能为 ``1`` 。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/06/13/plus1-grid.jpg" />

```
输入: n = 5, mines = [[4, 2]]
输出: 2
解释: 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/06/13/plus2-grid.jpg" />

```
输入: n = 1, mines = [[0, 0]]
输出: 0
解释: 没有加号标志，返回 0 。
```

 

**提示：**


- ``1 <= n <= 500``
- ``1 <= mines.length <= 5000``
- ``0 <= x<sub>i</sub>, y<sub>i</sub> < n``
- 每一对 ``(x<sub>i</sub>, y<sub>i</sub>)`` 都 **不重复**​​​​​​​



[LeetCode链接](https://leetcode-cn.com/problems/largest-plus-sign/)

### 思路及代码

根据 mines 数组进行挖洞，之后四个方向做动态规划找到最大连续1的个数。

```cpp
class Solution {
public:
    int orderOfLargestPlusSign(int n, vector<vector<int>>& mines) {
        // 四个方向进行遍历 保存最小连续1的个数
        vector<vector<int>> count(n, vector<int>(n, INT_MAX));
        vector<vector<int>> map(n, vector<int>(n, 1));

        // 初始化地图
        for(auto p : mines){
            map[p[0]][p[1]] = 0;
        }

        for(int i = 0; i < n; i++){
            int tmp = 0;
            for(int j = 0; j < n; j++){
                if(map[i][j]){
                    tmp++;
                }
                else{
                    tmp = 0;
                }

                if(tmp){
                    count[i][j] = min(count[i][j], tmp);
                }
            }
        }

        for(int j = 0; j < n; j++){
            int tmp = 0;
            for(int i = 0; i < n; i++){
                if(map[i][j]){
                    tmp++;
                }
                else{
                    tmp = 0;
                }

                if(tmp){
                    count[i][j] = min(count[i][j], tmp);
                }
            }
        }

        for(int i = n - 1; i >= 0; i--){
            int tmp = 0;
            for(int j = n - 1; j >= 0; j--){
                if(map[i][j]){
                    tmp++;
                }
                else{
                    tmp = 0;
                }

                if(tmp){
                    count[i][j] = min(count[i][j], tmp);
                }
            }
        }


        int res = 0;    // 找到最大值
        for(int j = n - 1; j >= 0; j--){
            int tmp = 0;
            for(int i = n - 1; i >=0; i--){
                if(map[i][j]){
                    tmp++;
                }
                else{
                    tmp = 0;
                }

                if(tmp){
                    count[i][j] = min(count[i][j], tmp);
                    res = max(res, count[i][j]);
                }
            }
        }
        return res;
    }
};
```