## 697. 数组的度

2021-02-20 12:23:54

### 题目

给定一个非空且只包含非负数的整数数组 ``nums``，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 ``nums`` 中找到与 ``nums`` 拥有相同大小的度的最短连续子数组，返回其长度。


**示例 1：**

```
输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
```

**示例 2：**

```
输入：[1,2,2,3,1,4,2]
输出：6
```

 

**提示：**

- ``nums.length`` 在1到 50,000 区间范围内。
- ``nums[i]`` 是一个在 0 到 49,999 范围内的整数。



[LeetCode链接](https://leetcode-cn.com/problems/degree-of-an-array/)

### 思路及代码

```cpp
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        // 用哈希表统计每个数出现的次数 起点和终点
        unordered_map<int, vector<int>> hash;
        for(int i = 0; i < nums.size(); i++){
            if(hash.find(nums[i]) == hash.end()){
                hash[nums[i]] = {1, i, i};
            }
            else{
                hash[nums[i]][0]++;
                hash[nums[i]][2] = i;
            }
        }

        int res = 0;
        int max_freq = 0;
        for(auto p : hash){
            if(p.second[0] > max_freq){
                max_freq = p.second[0];
                res = p.second[2] - p.second[1] + 1;
            }
            else if(p.second[0] == max_freq){
                res = min(res, p.second[2] - p.second[1] + 1);
            }
        }
        return res;
    }
};
```