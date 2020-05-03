## Maximum Subarray
##### 2018年02月08日17:24:09
##### 这个题目深感无力.......Kadane算法
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

#### 2020年5月3日

数据结构课上又讲到了这个题目，很清楚地记住了一点：和为负数的子序列不能作为最大和连续子序列的头部，按照这个想法直接写出了O(n)代码。

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int tmp = 0, res = INT_MIN;
        bool flag = true;
        for(auto i : nums){
            if(flag){
                tmp = i;
                flag = false;
            }
            else{
                tmp += i;
            }
            res = max(res, tmp);
            if(tmp < 0){
                flag = true;
            }
        }
        return res;
    }
};
```

上面的代码能进一步简化，取消掉不必要的flag变量。

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int tmp = -1, res = INT_MIN;
        for(auto i : nums){
            if(tmp < 0){
                tmp = i;
            }
            else{
                tmp += i;
            }
            res = max(res, tmp);
        }
        return res;
    }
};
```

官方在题目上新增了要求，可以尝试用分治方法来求解，想了半天只和标准的解答有了一点点交集，自己考虑问题不是很全面。对于分治法，分的过程很简单，但是合并的过程却相对复杂，对于两个子序列进行合并的时候，具有最大和的连续子数组可能情况有多种：

- 左序列或右序列中间部分的最大值
- 左序列的右边界最大和与右序列的左边界最大和

这样可以定义出三个变量lSum、rSum、mSum，分别代表当前序列的左边界最大值、右边界最大值、序列中间最大值。

接下来研究这三个变量如何获取，当序列长为1时，三个变量自然相等，可以在这一基础上向上推导。对于lSum，它的值应该为合并前左序列的和，与右序列左边界最大和两者相加的结果与合并前左序列的左边界最大和两者中较大的一个。同理rSum的值应为合并前右序列的和与左序列右边界最大和两者相加的结果与合并前右序列右边界最大和两者中较大的一个。

分析到这里，就发现如果想要计算出lSum与rSum，需要第四个表示序列和的变量iSum，通过iSum可以方便地推算出lSum与rSum，而iSum本身的计算公式也很简单，等于左右两个序列的iSum相加。

到这里，就只剩一个mSum变量的计算方式没有明确，再回过头去看mSum的含义，其代表了整个序列中间部分的最大值，不难得到其实际上就是整个序列的最大和。它的计算方式就等于左序列中的最大和、右序列中的最大和、左序列的右边界最大和与右序列的左边界最大和三者中最大的一个，这一点与最开始的情况刚好对应起来。

复现了一遍官方的代码：

```cpp
class Solution {
public:
    struct Status{
        int lSum, rSum, mSum, iSum;
    };
    
    // 合并
    Status pushUp(Status left, Status right){
        int iSum = left.iSum + right.iSum;
        int lSum = max(left.iSum + right.lSum, left.lSum);
        int rSum = max(left.rSum + right.iSum, right.rSum);
        int mSum = max(max(left.mSum, right.mSum), left.rSum + right.lSum);
        return (Status){lSum, rSum, mSum, iSum};
    }

    Status get(vector<int>& nums, int left, int right){
        if(left == right)
            return (Status){nums[left], nums[left], nums[left], nums[left]};
        int mid = left + (right-left)/2;
        Status leftSub = get(nums, left, mid);
        Status rightSub = get(nums, mid+1, right);
        return pushUp(leftSub, rightSub);
    }

    int maxSubArray(vector<int>& nums) {
        return get(nums, 0, nums.size()-1).mSum;
    }
};
```