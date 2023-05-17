## 2446. 判断两个事件是否存在冲突

2023-05-17 09:21:23

### 题目

给你两个字符串数组 ``event1`` 和 ``event2`` ，表示发生在同一天的两个闭区间时间段事件，其中：


- ``event1 = [startTime<sub>1</sub>, endTime<sub>1</sub>]`` 且
- ``event2 = [startTime<sub>2</sub>, endTime<sub>2</sub>]``


事件的时间为有效的 24 小时制且按 ``HH:MM`` 格式给出。

当两个事件存在某个非空的交集时（即，某些时刻是两个事件都包含的），则认为出现 **冲突** 。

如果两个事件之间存在冲突，返回 ``true``；否则，返回``false`` 。

 

<b>示例 1：</b>

```

输入：event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
输出：true
解释：两个事件在 2:00 出现交集。
```

<b>示例 2：</b>

```

输入：event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
输出：true
解释：两个事件的交集从 01:20 开始，到 02:00 结束。
```

**示例 3：**

```

输入：event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
输出：false
解释：两个事件不存在交集。
```

 

<b>提示：</b>


- ``evnet1.length == event2.length == 2.``
- ``event1[i].length == event2[i].length == 5``
- ``startTime<sub>1</sub> <= endTime<sub>1</sub>``
- ``startTime<sub>2</sub> <= endTime<sub>2</sub>``
- 所有事件的时间都按照 ``HH:MM`` 格式给出



[LeetCode链接](https://leetcode-cn.com/problems/determine-if-two-events-have-conflict/)

### 思路及代码

将时间转化为整数格式后判断区间是否相交，实际上也可以直接对字符串进行比较。

```cpp
class Solution {
public:
    int helper(string event){
        return stoi(event.substr(0,2)) * 60 + stoi(event.substr(3));
    }
    bool haveConflict(vector<string>& event1, vector<string>& event2) {
        return max(helper(event1[0]), helper(event2[0])) <= min(helper(event1[1]), helper(event2[1]));
    }
};
```


```cpp
class Solution {
public:
    int helper(string event){
        return stoi(event.substr(0,2)) * 60 + stoi(event.substr(3));
    }
    bool haveConflict(vector<string>& event1, vector<string>& event2) {
        /// return max(helper(event1[0]), helper(event2[0])) <= min(helper(event1[1]), helper(event2[1]));
        return max(event1[0], event2[0]) <= min(event1[1], event2[1]);
    }
};
```