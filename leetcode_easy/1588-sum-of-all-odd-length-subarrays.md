## 1588. 所有奇数长度子数组的和

2021-08-29 10:33:47

### 题目

给你一个正整数数组 ``arr`` ，请你计算所有可能的奇数长度子数组的和。

**子数组** 定义为原数组中的一个连续子序列。

请你返回 ``arr`` 中 **所有奇数长度子数组的和** 。



**示例 1：**

```
输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```

**示例 2：**

```
输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
```

**示例 3：**

```
输入：arr = [10,11,12]
输出：66
```



**提示：**


- ``1 <= arr.length <= 100``
- ``1 <= arr[i] <= 1000``



[LeetCode链接](https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/)

### 思路及代码

前缀和配合暴力算法，考虑区间长度和区间起点的所有可能。

```cpp
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        vector<int> pre(arr);   // 前缀和数组
        for(int i = 1; i < pre.size(); i++){
            pre[i] += pre[i-1];
        }

        int res = 0;
        for(int len = 1; len <= arr.size(); len+=2){
            for(int i = 0; i < arr.size(); i++){
                int j = i + len - 1;
                if(j >= arr.size()){
                    break;
                }
                else{
                    if(i == j){
                        res += arr[i];
                    }
                    else{
                        if(i == 0){
                            res += pre[j];
                        }
                        else{
                            res += pre[j] - pre[i-1];
                        }
                    }
                }
            }
        }
        return res;
    }
};
```

读完题就感觉应该有利用数学规则直接求解的做法，但是自己没想到，看了别人的题解之后发现实现起来很简单。对于每个数字，可能使用的次数和该数字左右两侧数据长度有关，左右两侧同时连续取偶数个数字、奇数个数字的所有组合便是该数字使用的次数。

```cpp
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int res = 0;
        int len = arr.size();
        for(int i = 0; i < arr.size(); i++){
            int left_num = i;
            int right_num = len - i - 1;

            // 左右两侧分别取奇数、偶数个数字的可能性
            int left_even = left_num / 2 + 1;
            int right_even = right_num / 2 + 1;
            
            int left_odd = (left_num & 1) ? left_num / 2 + 1 : left_num / 2;
            int right_odd = (right_num & 1) ? right_num / 2 + 1 : right_num / 2;    // 此处可以利用整型除法的特点向上加一再除二，不需要判断
            res += (left_odd * right_odd + left_even * right_even) * arr[i];
        }
        return res;
    }
};
```