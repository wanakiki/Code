## 665. 非递减数列

2021-02-08 14:50:14

### 题目

给你一个长度为 ``n`` 的整数数组，请你判断在 **最多 **改变 ``1`` 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 ``i`` ``(0 <= i <= n-2)``，总满足 ``nums[i] <= nums[i + 1]``。

 

**示例 1:**

```
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
```

**示例 2:**

```
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
```

 

**说明：**


- ``1 <= n <= 10 ^ 4``
- ``- 10 ^ 5 <= nums[i] <= 10 ^ 5``



[LeetCode链接](https://leetcode-cn.com/problems/non-decreasing-array/)

### 思路及代码

虽然标签是简单题，但是这个题目实现起来会有一些细节。

首先遍历数组，当遇到递减情况时进行判断，假定当前数组为[a, b, c, d]，其中a到b满足非递减，``b > c``为当前处理的递减位置。

为使数组变成非递减数列，需要对b、c进行处理，为了不影响前后的变化，处理方式有两种：

1. 令b的值为c：若``c >= a``则该变化成立，否则不成立
2. 令c的值为b：若``d >= b``则该变化成立，否则不成立

若以上两种变化均不满足，则证明该位置不能通过一次变化得到非递减的特性，直接返回false，例如数列[3,4,2,3]。

```cpp
class Solution {
public:
    bool checkPossibility(vector<int> &nums) {
        int n = nums.size(), cnt = 0;
        for (int i = 0; i < n - 1; ++i) {
            if(nums[i] > nums[i+1]){
                if(cnt == 1){
                    return false;
                }
                bool flag1 = false, flag2 = false;
                if(i == 0 || nums[i+1] >= nums[i-1]){
                    flag1 = true;
                }
                if(i == n-2 || nums[i+2] >= nums[i]){
                    flag2 = true;
                }

                // 检查是否能够执行一种变化
                if(flag2 || flag1){
                    cnt++;
                }
                else{
                    return false;
                }
            }
        }
        return true;
    }
};
```