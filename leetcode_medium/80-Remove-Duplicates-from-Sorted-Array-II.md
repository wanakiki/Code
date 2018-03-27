## 80. Remove Duplicates from Sorted Array II
##### 2018-03-27
##### 数组处理方法
## 1.题目
> Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
>
>For example,
Given sorted array nums = [1,1,1,2,2,3],
>
>Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.   
>处理数组，最多允许两个重复元素出现，结束后返回数组长度，在元素组中进行操作。

## 2.分析
设置一个变量用来计算相同元素出现的个数，一个变量用来记录当前的长度，用循环遍历数组，当超过两个之后直接跳过该元素，在循环结束进行修改数组的操作。

**注意：这道题目数组是有序的**
## 3. 代码
```c
int removeDuplicates(int* nums, int numsSize) {
    int count=0,res=0;
    for(int i=0;i<numsSize;i++){
        if(i>0 && nums[i-1]==nums[i]){
            count++;
            if(count>=3)    //应该为大于等于3
                continue;
        }
        else
            count=1;
        nums[res++]=nums[i];
    }
    return res;
}
```
