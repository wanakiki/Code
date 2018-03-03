## 16. 3Sum Closest
##### 2018-03-03 
##### 3SUM变式
***
## 1.题目
>Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.  
给定一个n个整数的数组S，在S中找到三个整数，使得总和最接近给定数量的目标。返回三个整数的总和。你可以假设每个输入都有一个解决方案。

## 2. 分析
由于之前坐过3SUM，有了之前定一移二的解法这道题也变得相对简单。  
花了相对较多的时间来寻找终止左右移动的办法，尽管是不必要的。  
我认为当两个可移动元素逐渐向中间靠近的时候，会出现差值一直大于零或者一直小于零的情况，在这种情况下，如果差值的绝对值也在变大我们就可以进行下一个元素的判断了。  

但实际测试之后发现并不需要上述判断，即使全部计算也不会出现超时的情况。

## 3.代码
```c
#include<limits.h>
#include<stdio.h>
#define ABS(x) (x<0 ? -x : x)
void sort(int *nums,int numsSize){
    for(int i=0;i<numsSize-1;i++)
    for(int j=i+1;j<numsSize;j++){
        if(nums[j]<nums[i]){
            int temp=nums[j];
            nums[j]=nums[i];
            nums[i]=temp;
        }
    }
}
int threeSumClosest(int* nums, int numsSize, int target) {
    int temp=0,differ=0,lastdiffer=INT_MAX,difference=INT_MAX;
    int sum=INT_MAX;

    sort(nums,numsSize);
    for(int i=0;i<numsSize-2;i++){
        int start=i+1;
        int end=numsSize-1;
        int flag=0;
        while(start<end){
            temp=nums[i]+nums[start]+nums[end];
            differ=temp-target;
		//lastdiffer用于记录上一次的差
            if(flag==0){
                lastdiffer=differ;
                flag=1;
            }
            else{
                if((differ*lastdiffer>0)&&(ABS(differ)>ABS(lastdiffer)))
                    break;
                lastdiffer=differ;
            }
            if(differ<0){
                differ=-differ;
                start++;
            }
            else if(differ>0){
                end--;
            }
            else if(differ==0)
                return target;

            if(differ<difference){
                difference=differ;
                sum=temp;
            }
        }
    }
    return sum;
}
```
