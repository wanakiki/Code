## 898. 转置矩阵

2021-02-25 12:02:20

### 题目

给你一个二维整数数组 ``matrix``， 返回 ``matrix`` 的 **转置矩阵** 。

矩阵的 **转置** 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png" style="width: 600px; height: 197px;" />

 

**示例 1：**

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
```

**示例 2：**

```
输入：matrix = [[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
```

 

**提示：**


- ``m == matrix.length``
- ``n == matrix[i].length``
- ``1 <= m, n <= 1000``
- ``1 <= m * n <= 10<sup>5</sup>``
- ``-10<sup>9</sup> <= matrix[i][j] <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/transpose-matrix/)

### 思路及代码

```cpp
class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> res(n, vector<int>(m));     // 考虑矩阵长宽不等 创建结果数组时需要注意维度
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                res[j][i] = matrix[i][j];
            }
        }
        return res;
    }
};
```