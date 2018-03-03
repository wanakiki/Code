## 31. Next Permutation
##### 2018-03-03
##### 全排列
***
## 1. 题目
>Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.  
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).  
The replacement must be in-place, do not allocate extra memory.  
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.  
实施下一个排列，将数字重新排列成按字母顺序排列的下一个更大的数字排列。  
如果这种安排不可行，则必须将其重新排列为尽可能最低的顺序（即按升序排序）。  
替换必须在原地，不要分配额外的内存。  
这里有些例子。输入位于左侧列，其相应输出位于右侧列。

## 2.分析
题目的问题是要给出当前排列的下一个排列，如果是最后一个则变成第一个。由于不能开辟空间，所以需要交换需要变化的元素。  
开始不清楚全排列的规则，查找了网上的分析:
- 找出最大的索引k，使a [k] <a [k + 1]。  
- 如果不存在这样的索引，则排列是最后的排列。  
- 找出大于k的最大索引l，使得a [k] <a [1]。  
- 将[k]的值与[l]的值交换。  
- 反转从[k + 1]直到并包括最后一个元素a [n]的序列。

重点在于理解规则，有了规则之后代码就很容易写出来了。  
另外多用指针😑
## 3. 代码
```c
#include<stdio.h>
//自定义交换函数
void swap(int *p,int *q)
{
    int t=*p;
    *p=*q;
    *q=t;
}

//区域交换函数
void reverse(int *nums,int start,int end)
{
    for(int i=start;i<(start+end+1)/2;i++)
        swap(nums+i,nums+end+start-i);
}

void nextPermutation(int* nums, int numsSize) {
    int i=numsSize-1,j=numsSize-1;
    while(i>0&&nums[i]<=nums[i-1])
        i--;
    if(i==0){
        reverse(nums,0,numsSize-1);
        return ;
    }
    while(nums[j]<=nums[i-1]) j--;
    swap(nums+j,nums+i-1);
    reverse(nums,i,numsSize-1);
}
```
