## 1235. 规划兼职工作

2022-10-22 19:56:06

### 题目

你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 ``n`` 份兼职工作，每份工作预计从 ``startTime[i]`` 开始到 ``endTime[i]`` 结束，报酬为 ``profit[i]``。

给你一份兼职工作表，包含开始时间 ``startTime``，结束时间 ``endTime`` 和预计报酬 ``profit`` 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 ``X`` 结束，那么你可以立刻进行在时间 ``X`` 开始的下一份工作。



**示例 1：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/sample1_1584.png" style="width: 300px;">**

```
输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
输出：120
解释：
我们选出第 1 份和第 4 份工作，
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
```

**示例 2：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/sample22_1584.png" style="height: 112px; width: 600px;"> **

```
输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
输出：150
解释：
我们选择第 1，4，5 份工作。
共获得报酬 150 = 20 + 70 + 60。
```

**示例 3：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/sample3_1584.png" style="height: 112px; width: 400px;">**

```
输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
输出：6
```



**提示：**


- ``1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4``
- ``1 <= startTime[i] < endTime[i] <= 10^9``
- ``1 <= profit[i] <= 10^4``



[LeetCode链接](https://leetcode-cn.com/problems/maximum-profit-in-job-scheduling/)

### 思路及代码

比较经典的动态规划题目，将数组按照结束时间递增排序后，每个工作 i 对应开始时间 start_time，结束时间 end_time，其能够获得的最大报酬为 ``max(global_max, profit[i] + dp[s_time])`` 其中 s_time 为小于等于当前 start_time 的时间，可以通过二分查找得到。

下面的代码组合使用了 set 和 unordered_map，本意是使用 lower_bound 避免自己写二分查找，结果却需要处理更多的边界情况。

官方题解直接使用了数组进行动态规划，更简洁。

```cpp
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int len = startTime.size();
        int res = 0;    // 保存全局最大报酬
        vector<int> sorted_data(len, 0);
        iota(sorted_data.begin(), sorted_data.end(), 0);
        
        sort(sorted_data.begin(), sorted_data.end(), [&](int a, int b){
            if(endTime[a] == endTime[b]){
                return startTime[a] < startTime[b];
            }
            else{
                return endTime[a] < endTime[b];
            }
        });

        // for(auto n: sorted_data){
        //     cout << startTime[n] << ' ' << endTime[n] << ' ' << profit[n] << endl;
        // }
        unordered_map<int, int> hash;
        set<int> myset;

        for(auto n : sorted_data){
            int start_time = startTime[n];
            int end_time = endTime[n];

            int cur_max = profit[n];

            // 找到小于等于start_time的项
            auto it = myset.lower_bound(start_time);
            if(it == myset.end()){
                if(myset.size() == 0){
                    // 如果找不到小于等于开始时间的项 则不累加
                    cur_max = profit[n];
                }
                else{
                    it--;
                    cur_max += hash[*it];
                }
            }
            else{
                if(*it == start_time){
                    cur_max += hash[start_time];
                }
                else{
                    // 如果查找到的位置不是 start_time 则必然大于 start_time 需要找到更前一个元素
                    if(it == myset.begin()){
                        cur_max = profit[n];
                    }
                    else{
                        it--;
                        cur_max += hash[*it];
                    }
                }
            }

            res = max(res, cur_max);
            // 使用当前能够获得的最大报酬更新哈希表
            if(hash.find(end_time) == hash.end()){
                hash[end_time] = res;
            }
            else{
                hash[end_time] = max(hash[end_time], res);
            }

            res = max(res, hash[end_time]);
            myset.insert(end_time);

        }
        return res;
    }
};
```