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
