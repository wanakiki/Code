## 304. 二维区域和检索 - 矩阵不可变

2021-03-02 11:19:49

### 题目

给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 ``(row1, col1)`` ，右下角为 ``(row2, col2)`` 。   

<img alt="Range Sum Query 2D" src="https://assets.leetcode-cn.com/aliyun-lc-upload/images/304.png" style="width: 130px;" />

<small>上图子矩阵左上角 (row1, col1) = **(2, 1)** ，右下角(row2, col2) = **(4, 3)**，该子矩形内元素的总和为 8。</small>

 

**示例：**

```
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
```

 

**提示：**


- 你可以假设矩阵不可变。
- 会多次调用 ``sumRegion``<em>*方法<em>。</em>
- 你可以假设 ``row1 ≤ row2`` 且 ``col1 ≤ col2`` 。



[LeetCode链接](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/)

### 思路及代码

二维前缀和。

```cpp
class NumMatrix {
public:
    vector<vector<int>> sum;
    NumMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if(m){
            int n = matrix[0].size();
            sum.resize(m+1, vector<int>(n+1));

            for(int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    sum[i+1][j+1] = sum[i][j+1] + sum[i+1][j] - sum[i][j] + matrix[i][j];
                }
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return sum[row2+1][col2+1] + sum[row1][col1] - sum[row2+1][col1] - sum[row1][col2+1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
```