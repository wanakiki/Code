## 1817. 查找用户活跃分钟数

2023-01-20 22:15:16

### 题目

给你用户在 LeetCode 的操作日志，和一个整数 ``k`` 。日志用一个二维整数数组 ``logs`` 表示，其中每个 ``logs[i] = [ID<sub>i</sub>, time<sub>i</sub>]`` 表示 ID 为 ``ID<sub>i</sub>`` 的用户在 ``time<sub>i</sub>`` 分钟时执行了某个操作。

**多个用户 **可以同时执行操作，单个用户可以在同一分钟内执行 **多个操作** 。

指定用户的** 用户活跃分钟数（user active minutes，UAM）** 定义为用户对 LeetCode 执行操作的 **唯一分钟数** 。 即使一分钟内执行多个操作，也只能按一分钟计数。

请你统计用户活跃分钟数的分布情况，统计结果是一个长度为 ``k`` 且 **下标从 1 开始计数** 的数组 ``answer`` ，对于每个 ``j``（``1 <= j <= k``），``answer[j]`` 表示 **用户活跃分钟数** 等于 ``j`` 的用户数。

返回上面描述的答案数组<i> </i>``answer``<i> </i>。

 

**示例 1：**

```

输入：logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
输出：[0,2,0,0,0]
解释：
ID=0 的用户执行操作的分钟分别是：5 、2 和 5 。因此，该用户的用户活跃分钟数为 2（分钟 5 只计数一次）
ID=1 的用户执行操作的分钟分别是：2 和 3 。因此，该用户的用户活跃分钟数为 2
2 个用户的用户活跃分钟数都是 2 ，answer[2] 为 2 ，其余 answer[j] 的值都是 0
```

**示例 2：**

```

输入：logs = [[1,1],[2,2],[2,3]], k = 4
输出：[1,1,0,0]
解释：
ID=1 的用户仅在分钟 1 执行单个操作。因此，该用户的用户活跃分钟数为 1
ID=2 的用户执行操作的分钟分别是：2 和 3 。因此，该用户的用户活跃分钟数为 2
1 个用户的用户活跃分钟数是 1 ，1 个用户的用户活跃分钟数是 2 
因此，answer[1] = 1 ，answer[2] = 1 ，其余的值都是 0
```

 

**提示：**


- ``1 <= logs.length <= 10<sup>4</sup>``
- ``0 <= ID<sub>i</sub> <= 10<sup>9</sup>``
- ``1 <= time<sub>i</sub> <= 10<sup>5</sup>``
- ``k`` 的取值范围是 ``[用户的最大用户活跃分钟数, 10<sup>5</sup>]``



[LeetCode链接](https://leetcode-cn.com/problems/finding-the-users-active-minutes/)

### 思路及代码

按照用户排序，之后统计每个用户的活跃时间。

```cpp
class Solution {
public:
    vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
        vector<int> res(k, 0);
        sort(logs.begin(), logs.end(), [&](vector<int>& a, vector<int>& b){
            if(a[0] == b[0])    return a[1] < b[1];
            return a[0] < b[0];
        });

        // 遍历数组查找活跃用户
        int index = 0;
        int last_id = -1;
        int time_count = 0;
        while(index < logs.size()){
            if(last_id != logs[index][0]){
                if(last_id != -1){
                    res[time_count-1]++;
                }
                last_id = logs[index][0];
                time_count = 1;
            }
            else{
                if(index != 0 && logs[index][1] != logs[index-1][1]){
                    time_count++;
                }
            }
            index++;
        }

        if(last_id != -1)   res[time_count-1]++;
        return res;
    }
};
```