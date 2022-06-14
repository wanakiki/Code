## 498. 对角线遍历

2022-06-14 09:06:28

### 题目

给你一个大小为 ``m x n`` 的矩阵 ``mat`` ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。



**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg" style="width: 334px; height: 334px;" />
```
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]
```

**示例 2：**

```
输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]
```



**提示：**


- ``m == mat.length``
- ``n == mat[i].length``
- ``1 <= m, n <= 10<sup>4</sup>``
- ``1 <= m * n <= 10<sup>4</sup>``
- ``-10<sup>5</sup> <= mat[i][j] <= 10<sup>5</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/diagonal-traverse/)

### 思路及代码

刚开始学编程时就做过的题目，思路比较简单，但是由比较多的边界判断，一卡一卡的写完了代码：

```cpp
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        vector<int> res;
        int m = mat.size();
        int n =mat[0].size();

        int x = 0;
        int y = 0;
        while(1){
            while(x >= 0 && y < n){
                res.push_back(mat[x][y]);
                x--;
                y++;
            }

            if(x < 0 && y < n){
                x++;
            }
            else{
                x += 2;
            }
            if(y >= n){
                y--;
            }
            if(x >= m || y < 0) break;

            while(x < m && y >= 0){
                res.push_back(mat[x][y]);
                x++;
                y--;
            }

            if(y < 0 && x < m){
                y++;
            }
            else{
                y+=2;
            }

            if(x >= m){
                x--;
            }
            if(x < 0 || y >= n) break;
        }
        return res;
    }
};
```

学习一下执行比较快的代码，总迭代次数等于对角线的个数，等于两边之和减一，如果当前迭代索引为偶数，则向右上，为奇数则向坐下。考虑到对角线元素满足累加和相等，可以只对一个坐标轴进行调整，使用总和计算另一个坐标轴。

下面代码中比较关键的点是计算x的初始位置和size。

```cpp
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int> >& mat) {
        vector<int> vec;
        int m = mat.size();
        int n = mat[0].size();

        for (int i = 0; i < (n+m-1); i++) {
            if (i%2 == 0) {
                int x = min(i, m-1);
                int size = max(0, i+1-n);       
                for (; x >= size; x--)
                    vec.push_back(mat[x][i-x]);
            }
            else {
                int x = max(0, i+1-n);
                int size = min(i, m-1);
                for (; x <= size; x++)
                    vec.push_back(mat[x][i-x]);
            }
        }

        return vec;
    }
};
```