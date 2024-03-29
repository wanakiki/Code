## 1037. 有效的回旋镖

2022-06-08 09:53:52  

### 题目

给定一个数组<meta charset="UTF-8" /> ``points`` ，其中<meta charset="UTF-8" /> ``points[i] = [x<sub>i</sub>, y<sub>i</sub>]`` 表示 **X-Y** 平面上的一个点，如果这些点构成一个***回旋镖** 则返回 ``true`` 。

**回旋镖** 定义为一组三个点，这些点 **各不相同** 且 **不在一条直线上** 。



**示例 1：**

```
输入：points = [[1,1],[2,3],[3,2]]
输出：true
```

**示例 2：**

```
输入：points = [[1,1],[2,2],[3,3]]
输出：false
```



**提示：**


- ``points.length == 3``
- ``points[i].length == 2``
- ``0 <= x<sub>i</sub>, y<sub>i</sub> <= 100``



[LeetCode链接](https://leetcode-cn.com/problems/valid-boomerang/)

### 思路及代码

判断三点是否位于同一条直线。

```cpp
class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
        return (points[2][1] - points[0][1]) * (points[1][0] - points[0][0]) != (points[1][1] - points[0][1]) * (points[2][0] - points[0][0]);
    }
};
```