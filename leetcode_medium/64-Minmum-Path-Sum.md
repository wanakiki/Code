## 64. Minimum Path Sum
##### 2018-03-21 
##### 动态分配继续了解
***
## 1.题目
>Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.    
>Note: You can only move either down or right at any point in time.
>在给定的mxn的网格中，找到一条路径使其到达右下角的总和最小。只能向右或向下走。  

*Example 1:*
```
[[1,3,1],
 [1,5,1],
 [4,2,1]]
 ```
 Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum. 

 ##  2.分析
 按照要求，首先想起了动态规划的解法。写完之后感觉如果出现个别的极限值计算就不会正确，但是由于遍历了整个数组，某条路径中间出现个别值也会被避免，无需考虑。  
 ## 3.代码
 ```c
 int minPathSum(int** grid, int row, int col) {
    for(int i=1;i<col;i++)
      grid[0][i]+=grid[0][i-1];
    for(int i=1;i<row;i++)
      grid[i][0]+=grid[i-1][0];

    for(int i=1;i<row;i++)
    for(int j=1;j<col;j++){
      if(grid[i-1][j]>grid[i][j-1])
        grid[i][j]+=grid[i][j-1];
      else
        grid[i][j]+=grid[i-1][j];
    }
    return grid[row-1][col-1];
}
```
