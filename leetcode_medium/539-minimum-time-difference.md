## 539. 最小时间差

2022-01-18 11:43:22

### 题目

给定一个 24 小时制（小时:分钟 **"HH:MM"**）的时间列表，找出列表中任意两个时间的最小时间差并以
分钟数表示。

 

**示例 1：**

```
输入：timePoints = ["23:59","00:00"]
输出：1
```

**示例 2：**

```
输入：timePoints = ["00:00","23:59","00:00"]
输出：0
```

 

**提示：**


- ``2 <= timePoints <= 2 * 10<sup>4</sup>``
- ``timePoints[i]`` 格式为 **"HH:MM"**



[LeetCode链接](https://leetcode-cn.com/problems/minimum-time-difference/)

### 思路及代码

对时间列表进行排序，计算相邻元素的时间差，同时计算最后一个元素和第一个元素的时间差。在计算时间差时，如果值大于12小时，则应用24小时对应分钟数减去原有值。

```cpp
class Solution {
public:
    int helper(string& a, string& b){
        int res = ((b[0] - a[0]) * 10 + b[1] - a[1]) * 60 + (b[3] - a[3]) * 10 + b[4] - a[4];
        int mid = 12 * 60;
        if(res > mid){
            return 24 * 60 - res;
        }
        else{
            return res;
        }
    }
    int findMinDifference(vector<string>& timePoints) {
        sort(timePoints.begin(), timePoints.end());
        int res = INT_MAX;

        for(int i = 0; i < timePoints.size() - 1; i++){
            res = min(res, helper(timePoints[i], timePoints[i+1]));
        }
        res = min(res, helper(timePoints[0],  timePoints[timePoints.size() - 1]));
        return res;
    }
};
```

上述做法执行速度较慢，参考官方题解，发现可以用雀巢算法提升执行效率。题目给定的输入范围是2*10^4，但实际上最多有1440个时间表示，当输入长度大于1440时，必然存在相同时间，可直接返回0。