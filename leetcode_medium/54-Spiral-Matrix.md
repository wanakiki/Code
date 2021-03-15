## 54. Spiral Matrix
##### 2018-03-17 
***
## 1.题目
>Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.  
>给定m×n个元素（m行，n列）的矩阵，以螺旋顺序返回矩阵的所有元素。  

For example,
Given the following matrix: 
```c
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
You should return [1,2,3,6,9,8,7,4,5]. 

## 2.分析
题目的本质是顺时针螺旋遍历一个二维数组，属于相对常见的题目。
因为之前做过类似的题目，很容易就想到了设置变量flag用于记录当前遍历的层数的办法，尽管相对麻烦，但是可行。  

对于这类问题，最大的难点个人感觉是层数的标志，以及如何避免重复遍历。  
上课的时候学到了一个非常好的办法，将数组分成了四块来遍历：  
1. 设置上下左右四个变量来标记四个方向的层数(u、d、l、r)
2. 开始循环，按照顺序逐层处理。以上侧为例，从l遍历到r,然后u++，和d相比较，如果大于d则跳出循环。其他类似。

道理很简单，个人表达能力较差，但是代码原理很简单。
## 3.代码
```c
int* spiralOrder(int** matrix, int matrixRowSize, int matrixColSize) {
  int n=matrixRowSize*matrixColSize;
  int *res;
  res=(int *)mallco(sizeof(int)*n);
  int u=0,d=matrixRowSize-1,l=0,r=matrixColSize-1;  //分别定义上下左右的标志
  int index=0;  //计数

  while(1){
    for(int col=l;col<=r;col++)
      res[index++]=matrix[u][col];
    if(++u>d) break;

    for(int row=u;row<=d;row++)
      res[index++]=matrix[row][r];
    if(--r<l) break;

    for(int col=r;col>=l;col--)
      res[index++]=matrix[d][col];
    if(--d<u) break;

    for(int row=d;row>=u;row--)
      resn[index++]=matrix[row][l];
    if(++l>r) break;
  }
  return res;
}
```
然后，这是别人的部分代码：
```c
 while (true) {
            // up
            for (int col = l; col <= r; col++) spiral[k++] = matrix[u][col];
            if (++u > d) break;
            // right
            for (int row = u; row <= d; row++) spiral[k++] = matrix[row][r];
            if (--r < l) break;
            // down
            for (int col = r; col >= l; col--) spiral[k++] = matrix[d][col];
            if (--d < u) break;
            // left
            for (int row = d; row >= u; row--) spiral[k++] = matrix[row][l];
            if (++l > r) break;
        }
 ```
emmmmm,可以通过加空格使自己的代码变得很清楚。🙄


```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int cur_loop = 1;
        int m = matrix.size(), n = matrix[0].size();
        int count = m * n;
        vector<int> res(count, 0);
        int cur_index = 0;

        int i = 0, j = 0;
        while(count){
            // 向右
            while(count && j <= n - cur_loop){
                res[cur_index++] = matrix[i][j++];
                count--;
            }
            i++;j--;

            // 向下
            while(count && i <= m - cur_loop){
                res[cur_index++] = matrix[i++][j];
                count--;
            }
            i--;j--;


            // 向左 边界稍微不同
            while(count && j >= cur_loop){
                res[cur_index++] = matrix[i][j--];
                count--;
            }

            // 向上
            while(count && i > cur_loop){
                res[cur_index++] = matrix[i--][j];
                count--;
            }

            cur_loop++;
        }
        return res;
    }
};
```
