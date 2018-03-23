## 73. Set Matrix Zeroes
##### 2018-03-23 
##### 先求实现，再求简练
***
## 1.题目
>Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
>
>Follow up:
>
>Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?  
>给定一个数组，如果这个数组有元素为零，则将该元素所在的行和列全部变为零。  
然后，给出的follow up先不看。

## 2.分析
题目相对简单，看到的时候首先想到了大一上学期做过的流感传染的题目，与这道题目不同，流感传染需要计算天数。但是当时采用的设置一个新变量表示第二天病发的方法很实用。  

对于这道题目，如果还是按照当时第一种想法，遍历到这个元素之后直接对其所在的行和列操作，那么遍历到最后的下场就是全部元素都变成了零。  

为了避免上面的问题，我的解决方法是新建一个数组用于存储为零元素的坐标，（这种做法多用了很多空间）在遍历结束之后再依照存放坐标的数组进行操作。

## 3.代码
```c
void setZeroes(int** matrix, int row, int col) {
      int store[row*col][2];
      int index=0;
      for(int i=0;i<row;i++)
      for(int j=0;j<col;j++){
        if(matrix[i][j]==0){
          store[index][0]=i;
          store[index][1]=j;
          index++;
        }
      }
      for(int i=0;i<index;i++){
        for(int j=0;j<col;j++){
          matrix[store[i][0]][j]=0;
        }
        for(int k=0;k<row;k++){
          matrix[k][store[i][1]]=0;
        }
      }
}
```

## 4.新想法
这是看到的想法，用第一行第一列来记录需要变成零的行和列。
  1. 首先遍历第一行第一列，看其是否含有零，设置两个布尔变量进行存储
  2. 对其他元素进行遍历，如果matix[i][j]为零，则(0,j)为零，(i,0)为零
  3. 按照上述方法遍历结束之后，对第一行第一列再次遍历，发现零就将其对应的行、则将该元素所在的行和列全部变为零
  3. 接着根据开始设置的布尔变量考录是否设置第一行第一列为零
