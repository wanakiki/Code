## 62. Unique Paths
##### 2018-03-19
##### 动态规划了解一下
***
## 1.题目
>A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
>
>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
>Note: m and n will be at most 100.

计算机器人走到右下角方法的个数（只能向右或者向下走）  
How many possible unique paths are there?

![sdaj](https://leetcode.com/static/images/problemset/robot_maze.png)
## 2.分析
开始认为是高中的数学题目，计算出C(m+n-2,n-1)就可以得到结果，但是因为大于10的数的阶乘实在有点大,long long之后还是会出现溢出的问题。如果用double型也会出现因为不能整除导致误差的情况。  

之后还是去看了别人的方法，不太习惯的动态规划方法，但是实现却非常简单。  
因为到达某个点的方法等于到达这个点上面的点和左边的点的和，动态规划就是利用了这个规律解决了这个题目。将第一行第一列赋值为1，从1，1元素开始遍历，返回最右下角的值。

**我还需要一个好的方法实现排列组合！！！！**
## 3.代码
```c
int uniquePaths(int m, int n) {
    int DP[100][100];

    for(int i = 0; i < n; ++i) DP[i][0] = 1;
    for(int j = 0; j < m; ++j) DP[0][j] = 1;

    for(int i = 1; i < n; ++i)
    {
        for(int j = 1; j < m; ++j)
        {
            DP[i][j] = DP[i - 1][j] + DP[i][j - 1];
        }
    }
    return DP[n - 1][m - 1];
}
```
