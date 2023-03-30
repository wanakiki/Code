## 1637. 两点之间不包含任何点的最宽垂直区域

2023-03-30 08:43:35

### 题目

给你 ``n`` 个二维平面上的点 ``points`` ，其中 ``points[i] = [x<sub>i</sub>, y<sub>i</sub>]`` ，请你返回两点之间内部不包含任何点的 **最宽垂直区域** 的宽度。

**垂直区域** 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 **最宽垂直区域** 为宽度最大的一个垂直区域。

请注意，垂直区域 **边上** 的点 **不在** 区域内。

 

**示例 1：**
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/31/points3.png" style="width: 276px; height: 371px;" />​
```

输入：points = [[8,7],[9,9],[7,4],[9,7]]
输出：1
解释：红色区域和蓝色区域都是最优区域。
```

**示例 2：**

```

输入：points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
输出：3
```

 

**提示：**


- ``n == points.length``
- ``2 <= n <= 10<sup>5</sup>``
- ``points[i].length == 2``
- ``0 <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/widest-vertical-area-between-two-points-containing-no-points/)

### 思路及代码

简单题，对宽度排序，找到相邻两个坐标的最大间隔。看题解，有人用了桶排序，n个元素准备n+1个桶，每个桶的容量是2，对应区间长度为 $(max-min)/n$。

```cpp
class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> width;
        for(auto p : points){
            width.push_back(p[0]);
        }
        sort(width.begin(), width.end());

        int res = 0;
        for(int i = 1; i < width.size(); i++){
            res = max(res, width[i] - width[i-1]);
        }
        return res;
    }
};
```