## 1828. 统计一个圆中点的数目

2023-01-24 08:59:24

### 题目

给你一个数组 ``points`` ，其中 ``points[i] = [x<sub>i</sub>, y<sub>i</sub>]`` ，表示第 ``i`` 个点在二维平面上的坐标。多个点可能会有 **相同** 的坐标。

同时给你一个数组 ``queries`` ，其中 ``queries[j] = [x<sub>j</sub>, y<sub>j</sub>, r<sub>j</sub>]`` ，表示一个圆心在 ``(x<sub>j</sub>, y<sub>j</sub>)`` 且半径为 ``r<sub>j</sub>``<sub> </sub>的圆。

对于每一个查询 ``queries[j]`` ，计算在第 ``j`` 个圆 **内** 点的数目。如果一个点在圆的 **边界上** ，我们同样认为它在圆 **内** 。

请你返回一个数组``answer`` ，其中``answer[j]``是第 ``j`` 个查询的答案。

 

**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/chrome_2021-03-25_22-34-16.png" style="width: 500px; height: 418px;">
```
输入：points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
输出：[3,2,2]
解释：所有的点和圆如上图所示。
queries[0] 是绿色的圆，queries[1] 是红色的圆，queries[2] 是蓝色的圆。
```

**示例 2：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/chrome_2021-03-25_22-42-07.png" style="width: 500px; height: 390px;">
```
输入：points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
输出：[2,3,2,4]
解释：所有的点和圆如上图所示。
queries[0] 是绿色的圆，queries[1] 是红色的圆，queries[2] 是蓝色的圆，queries[3] 是紫色的圆。
```

 

**提示：**


- ``1 <= points.length <= 500``
- ``points[i].length == 2``
- ``0 <= x<sub>​​​​​​i</sub>, y<sub>​​​​​​i</sub> <= 500``
- ``1 <= queries.length <= 500``
- ``queries[j].length == 3``
- ``0 <= x<sub>j</sub>, y<sub>j</sub> <= 500``
- ``1 <= r<sub>j</sub> <= 500``
- 所有的坐标都是整数。



[LeetCode链接](https://leetcode-cn.com/problems/queries-on-number-of-points-inside-a-circle/)

### 思路及代码

对于每个查询，遍历所有点判断是否位于圆内。

```cpp
class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> res(queries.size(), 0);

        for(int i = 0; i < queries.size(); i++){
            int r = pow(queries[i][2], 2);
            for(int j = 0; j < points.size(); j++){
                if((pow(queries[i][0] - points[j][0], 2) + pow(queries[i][1] - points[j][1], 2) <= r)){
                    res[i]++;
                }
            }
        }
        return res;
    }
};
```