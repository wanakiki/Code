## 48. Rotate Image
##### 2018-03-14
***
## 1.题目
>You are given an n x n 2D matrix representing an image.
>
>Rotate the image by 90 degrees (clockwise).
>
>Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.  
给你一个表示图像的n×n二维矩阵。 将图像旋转90度(顺时针方向)。   
注： 你必须把图像旋转到位，这意味着你必须直接修改输入的2D矩阵。不要分配另一个2D矩阵并执行旋转操作。

## 2.分析
其实由于是矩阵，函数的参数并不需要全部使用。  
我的做法是从横纵坐标相同的位置开始横向遍历，同时交换四个对应元素。交换的四个元素之间的关系很好确定，比较麻烦的是想出一个比较简单的循环判断条件。

如果边长是偶数，判断条件自然是<n/2，乍眼一看这个条件应该对边长奇数的情况不适用，但实际上，如果边长是奇数，最中间的元素是不需要变换的，所以这个判断条件是全面的。

起初我遇到奇数边长的做法是加一再除二，但是看到了别人的这个条件，发现自己又做了无用功😑
## 3.代码
```c
void rotate(int** matrix, int matrixRowSize, int *matrixColSizes) {
    for (int i=0; i<matrixRowSize/2; ++i){
        for (int j=i; j<matrixRowSize-1-i; ++j){
            int z = matrix[i][j];
            matrix[i][j] = matrix[matrixRowSize-j-1][i];
            matrix[matrixRowSize-j-1][i] = matrix[matrixRowSize-i-1][matrixRowSize-j-1];
            matrix[matrixRowSize-i-1][matrixRowSize-j-1] = matrix[j][matrixRowSize-i-1];
            matrix[j][matrixRowSize-i-1] = z;
        }
    }
}

```
