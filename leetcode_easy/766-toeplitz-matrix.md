## 777. 托普利茨矩阵

2021-02-22 10:29:55

### 题目

给你一个 ``m x n`` 的矩阵 ``matrix`` 。如果这个矩阵是托普利茨矩阵，返回 ``true`` ；否则，返回``false``。

如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是**托普利茨矩阵** 。

 
**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/ex1.jpg" style="width: 322px; height: 242px;" />

```
输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
输出：true
解释：
在上述矩阵中, 其对角线为:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
各条对角线上的所有元素均相同, 因此答案是 True 。
```

**示例 2：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/ex2.jpg" style="width: 162px; height: 162px;" />

```
输入：matrix = [[1,2],[2,2]]
输出：false
解释：
对角线 "[1, 2]" 上的元素不同。
```

 

**提示：**


- ``m == matrix.length``
- ``n == matrix[i].length``
- ``1 <= m, n <= 20``
- ``0 <= matrix[i][j] <= 99``


 

**进阶：**


- 如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？
- 如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？



[LeetCode链接](https://leetcode-cn.com/problems/toeplitz-matrix/)

### 思路及代码

不需要按线遍历，直接遍历每个元素判断是否与左上方元素相同即可。

```cpp
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int r = matrix.size(), c = matrix[0].size();
        // for(int i = 1; i < r; i++){
        //     for(int j = 1; j < c; j++){
        //         if(matrix[i][j] != matrix[i-1][j-1]){
        //             return false;
        //         }
        //     }
        // }
        for(int i = 0; i < r-1; i++){
            for(int j = 0; j < c-1; j++){
                if(matrix[i][j] != matrix[i+1][j+1]){
                    return false;
                }
            }
        }
        return true;
    }
};
```

针对于第一个进阶问题，容易想到先保存一行，在读取下一行时进行比较判断。对于第二个问题没有想到合适的解决方案，官方题解给出的做法是将矩阵进行切分，确保相邻矩阵之间有一行或者一列是重复的，对每个块进行判断（划分子问题）