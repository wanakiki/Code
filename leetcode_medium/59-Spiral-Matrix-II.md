## 59. Spiral Matrix II
##### 2018-03-13
***
## 1.题目
>Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
>
>For example,
Given n = 3,
You should return the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

## 2.分析及代码
回型填充，相对较熟悉的题目。
详细的分析可能需要睡醒了再补充了。
```c
int** generateMatrix(int n) {
    if (n == 0) {
        return NULL;
    }

    int** res = (int**)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; ++i) {
        res[i] = (int*)malloc(sizeof(int) * n);
    }

    int low = 0, high = n - 1, k = 1;
    for (; low < high; ++low, --high) {
        for (int i = low; i < high; ++i, ++k) {
            res[low][i] = k;
        }
        for (int i = low; i < high; ++i, ++k) {
            res[i][high] = k;
        }
        for (int i = high; i > low; --i, ++k) {
            res[high][i] = k;
        }
        for (int i = high; i > low; --i, ++k) {
            res[i][low] = k;
        }
    }
    if (low == high) {
        res[low][low] = k;
    }
    return res;
}
```
****
##### 2018-4-10  C++
```cpp
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n,vector<int>(n));
        int k = 1,i = 0,j=0;
        while(k<=n*n){
            j=i;
            while(j<n-i)
                res[i][j++]=k++;
            j=i+1;
            while(j<n-i)
                res[j++][n-1-i]=k++;
            j=n-2-i;
            while(j>i)
                res[n-1-i][j--]=k++;
            j=n-1-i;
            while(j>i)
                res[j--][i]=k++;
            i++;
        }
        return res;
    }
};
```
