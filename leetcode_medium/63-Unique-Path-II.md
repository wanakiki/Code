## 63. Unique Paths II
##### 2018-03-20
##### 继续了解动态规划.....
****
## 1.题目
>Follow up for "Unique Paths":
>
>Now consider if some obstacles are added to the grids. How many unique paths would there be?
>
>An obstacle and empty space is marked as 1 and 0 respectively in the grid.  
>题目沿袭独特的路，但是增加了无法经过的障碍物。现在给我们一个由零和一构成的二维数组，1代表障碍物，问从左上角到右下角方法的个数。

*for exmaple:*
```
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
```
在这个2x3的二维数组中，独特路径的个数为2。
## 2.分析
沿袭Unique Path的做法，继续使用动态规划，这次的难点在于如何避免障碍。  
开始打算直接对着原数组操作，把原数组中的1变成-1，当遇到-1的时候再把-1变为零，处理结束后返回右下角的值。此方法可行。

同学告诉了另一种方法，新建一个数组用于动态处理，遍历一个元素就去原数组查找是否为1，若为1，则该位置为零。最后仍是返回数组右下角的值。

## 3.代码
```c
int uniquePathsWithObstacles(int** Grid, int row, int col) {
    int **new;
    new=(int **)malloc(sizeof(int*)*row);
    for(int i=0;i<row;i++)
      new[i]=(int *)calloc(col,sizeof(int));  //动态分配的同时直接初始化，避免错误

    new[0][0]=1;
    int temp1,temp2;
    for(int i=0;i<row;i++){
      temp1=i-1;
    for(int j=0;j<col;j++){
      temp2=j-1;

      //判断障碍
      if(Grid[i][j]){
        new[i][j]=0;
        continue;
      }

      if(temp1>=0)
        new[i][j]+=new[temp1][j];
      if(temp2>=0)
        new[i][j]+=new[i][temp2];
    }
    }
    return new[row-1][col-1];
}
···
