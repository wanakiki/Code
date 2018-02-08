## Maximum Subarray
##### 2018年02月08日17:24:09
##### 这个题目深感无力.......
***
### 题目
>Find the contiguous subarray within an array (containing at least one number) which has the largest sum.  
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],  
the contiguous subarray [4,-1,2,1] has the largest sum = 6.  
在一个数组中找到连续的子数组（至少包含一个数字），这个数组的总和最大。 例如，给定数组[-2,1，-3,4，-1,2,1，-5,4]， 连续的子数组[4，-1,2,1]具有最大的总和= 6。
 
### 分析
要求是找到最大总和的数组，在不考虑时间的情况下遍历一定能解决问题。但因为有时间要求，采取了两端同时比较的方法（leetcode11题），但是很遗憾，这个方法有自身的局限，不能在这个地方实现。  
看了看别人的想法，可以直接从头开始加，当和小于下一个元素时开始重新加和，返回最终的和。
  
我没有更好的办法。
### 代码
我的能实现部分数据的做法
```c
int maxSubArray(int * nums,int numsSize){
        int sum=0,sum2=0;
        for(int i=0;i<numsSize;i++)
                sum+=nums[i];
        sum2=sum;
        int i=0,j=numsSize-1;
        while(i!=j){
                if(nums[i]>nums[j]){
                        sum2-=nums[j];
                        j--;
                }
                else if(nums[i]<nums[j]){
                        sum2-=nums[i];
                        i++;
                }
                else if(nums[i]==nums[j]){
                        if(nums[i+1]>nums[j-1]){
                                sum2-=nums[j];
                                j--;
                        }
                        else{
                                sum2-=nums[i];
                                i++;
                        }
                }
                if(sum2>sum)
                        sum=sum2;
        }
        return sum;
}
```
不是我想出来的做法（很简单）
```c
int maxSubArray(int* nums, int size)
{
    int sum = 0;
    int max = INT_MIN;
    for(int i = 0; i < size; i++)
    {
        if(sum >= 0)
            sum += nums[i];
        else
            sum = nums[i];
        if(sum > max)
            max = sum;
    }
    return max;
}
```
