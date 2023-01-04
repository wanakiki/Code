## 1620. 网络信号最好的坐标

2022-11-02 20:29:16

### 题目

给你一个数组 ``towers`` 和一个整数 ``radius`` 。

数组  ``towers``  中包含一些网络信号塔，其中 ``towers[i] = [x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub>]`` 表示第 ``i`` 个网络信号塔的坐标是 ``(x<sub>i</sub>, y<sub>i</sub>)`` 且信号强度参数为 ``q<sub>i</sub>``<sub> </sub>。所有坐标都是在  X-Y 坐标系内的 **整数** 坐标。两个坐标之间的距离用 **欧几里得距离** 计算。

整数 ``radius`` 表示一个塔 **能到达 **的 **最远距离** 。如果一个坐标跟塔的距离在 ``radius`` 以内，那么该塔的信号可以到达该坐标。在这个范围以外信号会很微弱，所以 ``radius`` 以外的距离该塔是 **不能到达的** 。

如果第 ``i`` 个塔能到达 ``(x, y)`` ，那么该塔在此处的信号为 ``⌊q<sub>i</sub> / (1 + d)⌋`` ，其中 ``d`` 是塔跟此坐标的距离。一个坐标的 <b>信号强度</b> 是所有 **能到达 **该坐标的塔的信号强度之和。

请你返回数组 ``[c<sub>x</sub>, c<sub>y</sub>]`` ，表示 **信号强度** 最大的 **整数** 坐标点 ``(c<sub>x</sub>, c<sub>y</sub>)`` 。如果有多个坐标网络信号一样大，请你返回字典序最小的 **非负** 坐标。

**注意：**


- 坐标 ``(x1, y1)`` 字典序比另一个坐标 ``(x2, y2)`` 小，需满足以下条件之一：


- 要么 ``x1 < x2`` ，
- 要么 ``x1 == x2`` 且 ``y1 < y2`` 。


- ``⌊val⌋`` 表示小于等于 ``val`` 的最大整数（向下取整函数）。


 

**示例 1：**
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/17/untitled-diagram.png" style="width: 176px; height: 176px;" />
```

输入：towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
输出：[2,1]
解释：
坐标 (2, 1) 信号强度之和为 13
- 塔 (2, 1) 强度参数为 7 ，在该点强度为 ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
- 塔 (1, 2) 强度参数为 5 ，在该点强度为 ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
- 塔 (3, 1) 强度参数为 9 ，在该点强度为 ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
没有别的坐标有更大的信号强度。
```

**示例 2：**

```
输入：towers = [[23,11,21]], radius = 9
输出：[23,11]
解释：由于仅存在一座信号塔，所以塔的位置信号强度最大。
```

**示例 3：**

```
输入：towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
输出：[1,2]
解释：坐标 (1, 2) 的信号强度最大。
```

 

**提示：**


- ``1 <= towers.length <= 50``
- ``towers[i].length == 3``
- ``0 <= x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub> <= 50``
- ``1 <= radius <= 50``



[LeetCode链接](https://leetcode-cn.com/problems/coordinate-with-maximum-network-quality/)

### 思路及代码

相对来讲比较没意思的题目，因为题目给定的数据范围较小，可以直接枚举出每个灯塔辐射的信号量，最后遍历一次进行比较。

```cpp
class Solution {
public:
    vector<int> bestCoordinate(vector<vector<int>>& towers, int radius) {
        vector<vector<int>> signal(51, vector<int>(51, 0));
        int old_radius = radius;
        radius *= radius;   // 避免开方
        for(auto t : towers){
            for(int i = 0; i < 51; i++){
                for(int j = 0; j < 51; j++){
                    int x = abs(i - t[0]);
                    int y = abs(j - t[1]);
                    if(x > old_radius || y > old_radius){
                        continue;
                    }
                    int tmp = x* x + y * y;
                    if(tmp <= radius){
                        float distance = sqrt(tmp);
                        signal[i][j] += (float)t[2] / ( 1 + distance);
                    }
                }
            }
        }

        int max_val = 0;
        vector<int> res ={0, 0};

        for(int i = 0; i < 51; i++){
            for(int j = 0; j < 51; j++){
                if(signal[i][j] > max_val){
                    res = {i, j};
                    max_val = signal[i][j];
                }
            }
        }
        return res;
    }
};
```