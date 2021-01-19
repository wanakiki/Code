## 1706. 连接所有点的最小费用

2021-01-19 21:05:20

### 题目

给你一个``points`` 数组，表示 2D 平面上的一些点，其中 ``points[i] = [x<sub>i</sub>, y<sub>i</sub>]`` 。

连接点 ``[x<sub>i</sub>, y<sub>i</sub>]`` 和点 ``[x<sub>j</sub>, y<sub>j</sub>]`` 的费用为它们之间的 **曼哈顿距离** ：``|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|`` ，其中 ``|val|`` 表示 ``val`` 的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 **有且仅有** 一条简单路径时，才认为所有点都已连接。

 

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/d.png" style="height:268px; width:214px" />

```
输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：
```

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/c.png" style="height:268px; width:214px" />

```
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。
```

**示例 2：**

```
输入：points = [[3,12],[-2,5],[-4,1]]
输出：18
```

**示例 3：**

```
输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4
```

**示例 4：**

```
输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000
```

**示例 5：**

```

输入：points = [[0,0]]
输出：0
```

 

**提示：**


- ``1 <= points.length <= 1000``
- ``-10<sup>6</sup> <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>6</sup>``
- 所有点 ``(x<sub>i</sub>, y<sub>i</sub>)`` 两两不同。

### 思路及代码

Prim算法得到最小生成树，核心原理是不断取连接最小生成树与外部节点中最小边对应节点添加到最小生成树对应点集中，添加点后更新各个节点在与最小生成树的距离。

```cpp
class Solution {
public:
    int helper(vector<int>& a, vector<int>& b){
        return abs(a[0] - b[0]) + abs(a[1] - b[1]);
    }
    int minCostConnectPoints(vector<vector<int>>& points) {
        int res = 0;
        int len = points.size();
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<bool> flag(len, false);   // 标记节点是否已经归入
        
        int n = len;
        pq.push({0, 0});
        while(!pq.empty() && n > 0){
            auto [dist, point] = pq.top();
            pq.pop();
            if(flag[point]){
                continue;
            }

            res += dist;
            flag[point] = true;
            n--;

            for(int i = 0; i < len; i++){
                if(flag[i]){
                    continue;
                }
                pq.push({helper(points[point], points[i]), i});
            }
        }
        return res;
    }
};
```