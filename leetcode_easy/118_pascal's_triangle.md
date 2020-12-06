## 118. Pascal's Triangle
##### 2018年2月22日11:00:34
##### 动态开辟二维数组
***
### 题目
>Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return
```
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```
### 分析
首先要知道杨辉三角的递推规律，其次需要明白如何动态的开辟二维数组。  
有关于动态二维数组的开辟：
```c
char *p=(char*)malloc(sizeof(char)*col);
free(p);	//开辟一维数组并释放

char**p=(char**)malloc(sizeof(char *)*row);
for(int i=0;i<row;i++)
	p[i]=(char *)malloc(sizeof(char)*col);
for(int i=0;i<row;i++)
	free(p[i]);
free(p);	//开辟行列可变的二维数组，但是释放较为麻烦

char(*p)[col]=(char(*)[col])malloc(sizeof(char)*row*col);
free(p);	//开辟列不可变的二维数组，但释放简单

用malloc开辟时应注意判空，试用结束后要记得释放内存。
```
### 代码
应注意返回的size是``*columnSizes``
```c
/**
 * Return an array of arrays.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generate(int numRows, int** columnSizes) {
    int** psk;
    psk=(int **)malloc(sizeof(int *)*numRows);
    *columnSizes=(int *)malloc(sizeof(int)*numRows);
    for(int i=0;i<numRows;i++){
            psk[i]=(int *)malloc(sizeof(int)*(i+1));
            //columnSizes[i]=i+1;
            *(*columnSizes+i) = i+1;
            for(int j=0;j<i+1;j++){
                if(j==0||j==i){
                    psk[i][j]=1;
                    continue;
                }
                psk[i][j]=psk[i-1][j-1]+psk[i-1][j];
            }
    }
    return psk;
}
```

#### 2020年12月6日

cpp解法

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        int cur = 0;
        while(cur < numRows){
            vector<int> nums(cur + 1, 1);
            int last_level = cur - 1;
            for(int i = 1; i < cur; i++){
                nums[i] = res[last_level][i] + res[last_level][i-1];
            }
            res.push_back(nums);
            cur++;
        }
        return res;
    }
};
```


## 119. Pascal's Triangle II
##### 2018年2月22日11:19:23
##### 杨辉三角
***
### 题目
>Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?

### 分析
与118题相似，不过这次只需要得到某一行。因为杨辉三角的递推关系是`` C(n+1,i)=C(n,i)+C(n,i-1)``，如果我们按照正常的思路从零开始写，我们就需要保留上一层的数组，为了简化程序，我们可以采取从每行最后一位开始往前写的方法。  
还要注意，当输入为3时，输出的是第四行。
### 代码
```c
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getRow(int rowIndex, int* returnSize) {
int *result=(int *)malloc(sizeof(int)*(rowIndex+1));
for(int i=0;i<=rowIndex;i++)
for(int j=i;j>=0;j--){
    if(j==0||j==i){
        result[j]=1;
        continue;
    }
    result[j]=result[j]+result[j-1];
}
*returnSize=rowIndex+1;
return result;
}
```
