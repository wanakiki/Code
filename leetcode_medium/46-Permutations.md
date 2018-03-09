## 46. Permutations
##### 2018-03-09
##### 全排列（递归实现）
***
## 1.题目
>Given a collection of distinct numbers, return all possible permutations.  
给定一组不同的数字，返回所有可能的排列
>
>For example,
[1,2,3] have the following permutations:
```
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## 2.分析
题目就是要求写出所给数组的全排列。因为之前接触过全排列的写法，用递归相对简单地达到了目的。  

提交后从别人代码发现全排列的返回数组可以直接直接计算出来大小再开辟，而不需要建立极大的空间。  

## 3.代码
```c
void swap_num(int *a, int *b){  
         int temp = *a;  
         *a = *b;  
         *b = temp;  
}  

void permut(int **result, int *nums, int end, int *rows, int beg)  
     {  
         int i;  
         if (beg == end) //最后一个元素递归返回
         {  
             (*rows)--;  
             for(i = 0; i != end; i++)  
                result[(*rows)][i] = nums[i];  
         }  
         else  
         {  
             for (i = beg; i != end; i++)  
             {  
                 swap_num(&nums[beg], &nums[i]);  
                 permut(result,nums, end, rows, beg+1);  
                 swap_num(&nums[beg], &nums[i]);  
             }  
         }  
}  

int** permute(int* nums, int numsSize, int* returnSize) {  
        int **result, i;  
        *returnSize = 1;  
        //计算全排列数   
        for(i = numsSize; i > 1; i--)  
        {  
            (*returnSize) *= i;  
        }  

        //开辟返回数组
        result = (int **)malloc((*returnSize)*sizeof(int *));
        for (i = 0; i != (*returnSize); i++)  
            *(result + i) = (int *)malloc(numsSize * sizeof(int));  

        int rows = *returnSize;  
        permut(result, nums, numsSize, &rows, 0);  
        return result;  
}  
```
