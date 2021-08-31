## 1109. 航班预订统计

2021-08-31 21:47:17

### 题目

这里有 ``n`` 个航班，它们分别从 ``1`` 到 ``n`` 进行编号。

有一份航班预订表 ``bookings`` ，表中第 ``i`` 条预订记录 ``bookings[i] = [first<sub>i</sub>, last<sub>i</sub>, seats<sub>i</sub>]`` 意味着在从 ``first<sub>i</sub>`` 到 ``last<sub>i</sub>`` （**包含** ``first<sub>i</sub>`` 和 ``last<sub>i</sub>`` ）的 **每个航班** 上预订了 ``seats<sub>i</sub>`` 个座位。

请你返回一个长度为 ``n`` 的数组 ``answer``，其中 ``answer[i]`` 是航班 ``i`` 上预订的座位总数。

 

**示例 1：**

```

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]
```

**示例 2：**

```

输入：bookings = [[1,2,10],[2,2,15]], n = 2
输出：[10,25]
解释：
航班编号        1   2
预订记录 1 ：   10  10
预订记录 2 ：       15
总座位数：      10  25
因此，answer = [10,25]
```

 

**提示：**


- ``1 <= n <= 2 * 10<sup>4</sup>``
- ``1 <= bookings.length <= 2 * 10<sup>4</sup>``
- ``bookings[i].length == 3``
- ``1 <= first<sub>i</sub> <= last<sub>i</sub> <= n``
- ``1 <= seats<sub>i</sub> <= 10<sup>4</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/corporate-flight-bookings/)

### 思路及代码

直接暴力统计超时，采取差分数组方法

```cpp
class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> res(n+1);
        for(auto booking : bookings){
            res[booking[0] - 1] += booking[2];
            res[booking[1]] -= booking[2];
        }
        for(int i = 1; i <= n; i++){
            res[i] += res[i-1];
        }
        res.resize(n);
        return res;
    }
};
```