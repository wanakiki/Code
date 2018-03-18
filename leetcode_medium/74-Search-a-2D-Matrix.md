## 74. Search a 2D Matrix
##### 2018-3-18
*****
## 1.题目

> Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
>
> * Integers in each row are sorted from left to right.
>* The first integer of each row is greater than the last integer of the previous row.
>
>写一个函数判断二维数组中是否具有给定的值。二维数组有如下特点：每行整数按照从小到大的顺序排序，
下一行最左端的数大于上一行最右边的数。

For example,

Consider the following matrix:
```
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
```
Given target = 3, return true.

## 2.分析
根据数组的规律，很容易写出来题目，判断每行最后一个是否大于等于目标值，如果大于则开始循环，从最后一个开始判断是否相同，当检测到了小于目标值的元素直接判假。遍历行的循环结束之后同样判假。
## 3.代码
```c
bool searchMatrix(int** matrix, int row, int col, int target) {
    for(int i=0;i<row;i++){
        if(matrix[i][col-1]>=target){
            for(int j=col-1;j>=0;j--){
                if(matrix[i][j]==target)
                    return true;
                if(matrix[i][j]<target)
                    return false;
            }
        }
    }
    return false;
}
```
