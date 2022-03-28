## 689. 三个无重叠子数组的最大和

2021-12-08 10:51:08

### 题目

给你一个整数数组 ``nums`` 和一个整数 ``k`` ，找出三个长度为 ``k`` 、互不重叠、且 ``3 * k`` 项的和最大的子数组，并返回这三个子数组。

以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 **0** 开始）。如果有多个结果，返回字典序最小的一个。



**示例 1：**

```
输入：nums = [1,2,1,2,6,7,5,1], k = 2
输出：[0,3,5]
解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
```

**示例 2：**

```
输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
输出：[0,2,4]
```



**提示：**


- ``1 <= nums.length <= 2 * 10<sup>4</sup>``
- ``1 <= nums[i] < 2<sup>16</sup>``
- ``1 <= k <= floor(nums.length / 3)``



[LeetCode链接](https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays/)

### 思路及代码

首先采用滑动窗口计算所有可能子数组的最大和，之后进行三次动态规划，记录在子数组个数为1 2 3的情况下记录到当前位置的最大子数组和。没有对代码逻辑进行优化，实现起来较为复杂。题目的难度相对简单。

```cpp
class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        // 滑动窗统计子数组的和
        vector<int> subarray;

        int cur_sum = 0;
        for(int i = 0; i < k; i++){
            cur_sum += nums[i];
        }

        subarray.push_back(cur_sum);
        int left = 0;
        int right = k;
        while(right < nums.size()){
            cur_sum -= nums[left];
            cur_sum += nums[right];

            left++;
            right++;

            subarray.push_back(cur_sum);
        }

        // 开始对和数组进行动态规划
        // 动态规划需要三轮 第一轮获取单个数组的最大和

        vector<int> dp_1(subarray.size(), 0);
        vector<int> dp_1_pos(subarray.size(), 0);
        
        dp_1[0] = subarray[0];
        dp_1_pos[0] = 0;
        for(int i = 1; i< subarray.size(); i++){
            if(subarray[i] > dp_1[i-1]){
                dp_1[i] = subarray[i];
                dp_1_pos[i] = i;
            }
            else{
                dp_1[i] = dp_1[i-1];
                dp_1_pos[i] = dp_1_pos[i-1];
            }
        }

        vector<int> dp_2(subarray.size(), 0);
        vector<vector<int>> dp_2_pos(subarray.size(), vector<int>(2, 0));
        dp_2[k] = subarray[k] + dp_1[0];
        dp_2_pos[k] = {k, dp_1_pos[0]};

        for(int i = k + 1; i < subarray.size(); i++){
            int val = subarray[i] + dp_1[i - k];
            if(val > dp_2[i-1]){
                dp_2[i] = val;
                dp_2_pos[i] = {i, dp_1_pos[i-k]};
            }
            else{
                dp_2[i] = dp_2[i-1];
                dp_2_pos[i] = dp_2_pos[i-1];
            }
        }

        vector<int> dp_3(subarray.size(), 0);
        vector<vector<int>> dp_3_pos(subarray.size(), vector<int>(3, 0));
        dp_3[2 * k] = subarray[2 * k] + dp_2[k];
        dp_3_pos[2 * k] = {2 * k, dp_2_pos[k][0], dp_2_pos[k][1]};

        for(int i = 2 * k + 1; i < subarray.size(); i++){
            int val = subarray[i] + dp_2[i - k];
            if(val > dp_3[i-1]){
                dp_3[i] = val;
                dp_3_pos[i] = {i, dp_2_pos[i-k][0], dp_2_pos[i-k][1]};
            }
            else{
                dp_3[i] = dp_3[i-1];
                dp_3_pos[i] = dp_3_pos[i-1];
            }
        }

        vector<int> res = dp_3_pos[subarray.size() - 1];
        swap(res[0], res[2]);
        return res;
    }
};
```