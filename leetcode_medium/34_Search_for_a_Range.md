## 34. Search for a Range
##### 2018-03-04 
***
## 1.题目
>Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.  
Your algorithm's runtime complexity must be in the order of O(log n).  
If the target is not found in the array, return [-1, -1].   
给定按升序排序的整数数组，找到给定目标值的开始和结束位置。 算法的运行时复杂度必须按照O（log n）的顺序。 如果在数组中找不到目标，则返回[-1，-1]。
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

## 2.过程
因为数组是排好顺序的，我的做法是直接遍历一遍，同时记录target开始出现的位置，不停更新消失的位置。  
因为记录消失位置的方法是 ``nums[i-1]==target``，所以当最后一个元素是target时会出现错误。  

解决办法是在循环之前直接判断最后一个元素是否为target。
## 3.代码
```c
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize=2;
    int *res=(int *)malloc(sizeof(int)*2);
    res[0]=-1;
    res[1]=-1;
    if(nums[numsSize-1]==target)
        res[1]=numsSize-1;
    for(int i=0;i<numsSize;i++){
        if(res[0]==-1&&nums[i]==target)
            res[0]=i;
        if(nums[i-1]==target&&res[1]!=numsSize-1)
            res[1]=i-1;
    }
    return res;
}
```

