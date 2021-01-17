## 1349. 缀点成线

2021-01-17 21:44:31

### 题目

在一个 XY 坐标系中有一些点，我们用数组 ``coordinates`` 来分别记录它们的坐标，其中 ``coordinates[i] = [x, y]`` 表示横坐标为 ``x``、纵坐标为 ``y`` 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 ``true``，否则请返回 ``false``。

 

**示例 1：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-2.jpg" style="height: 336px; width: 336px;">

```
输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true
```

**示例 2：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-1.jpg" style="height: 336px; width: 348px;">**

```
输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false
```

 

**提示：**


- ``2 <= coordinates.length <= 1000``
- ``coordinates[i].length == 2``
- ``-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4``
- ``coordinates`` 中不含重复的点



### 思路及代码

使用乘法形式两点式对直线进行表示，本题数据范围不会越界。

```cpp
class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int x1 = coordinates[0][0], y1 = coordinates[0][1];
        int x2 = coordinates[1][0], y2 = coordinates[1][1];
        for(int i = 2; i < coordinates.size(); i++){
            int x = coordinates[i][0], y = coordinates[i][1];
            int a = (x - x1) * (y2 - y1);
            int b = (x2 - x1) * (y - y1);
            if(a != b){
                return false;
            }
        }
        return true;
    }
};
```