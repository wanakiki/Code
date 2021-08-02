## 743. 网络延迟时间

2021-08-02 19:07:42

### 题目

有 ``n`` 个网络节点，标记为 ``1`` 到 ``n``。

给你一个列表 ``times``，表示信号经过 **有向** 边的传递时间。 times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>) 
，其中 u<sub>i</sub> 是源节点，v<sub>i</sub> 是目标节点， w<sub>i</sub> 是一个信号从源节点传递到目标节点的时间
。

现在，从某个节点 ``K`` 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 ``-1`` 。

 

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="height: 220px; width: 200px;" />

```
输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
```

**示例 2：**

```
输入：times = [[1,2,1]], n = 2, k = 1
输出：1
```

**示例 3：**

```
输入：times = [[1,2,1]], n = 2, k = 2
输出：-1
```

 

**提示：**


- ``1 <= k <= n <= 100``
- ``1 <= times.length <= 6000``
- ``times[i].length == 3``
- 1 <= u<sub>i</sub>, v<sub>i</sub> <= n
- u<sub>i</sub> != v<sub>i</sub>
- 0 <= w<sub>i</sub> <= 100
- 所有 (u<sub>i</sub>, v<sub>i</sub>) 对都 **互不相同**（即，不含重复边）



[LeetCode链接](https://leetcode-cn.com/problems/network-delay-time/)

### 思路及代码

最短路Dijkstra算法，在具体实现时通过遍历距离数组的方式找到距离最近的点。距离数组可以使用小顶堆替代，同一节点不同路径的添加对最终最小距离的查找结果不会产生影响。

针对于本题而言，节点数目小于边数，使用距离数组的代码执行速度应该会比使用小顶堆的代码执行速度快一些，因为小顶堆需要维护许多不需要的边。

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // 统计所有节点的出边 构成邻接表
        vector<vector<pair<int, int>>> nodes(n + 1);
        for(int i = 0; i < times.size(); i++){
            nodes[times[i][0]].push_back({times[i][1], times[i][2]});
        }

        int res = 0;
        vector<int> flag(n + 1, false);
        vector<int> distance(n + 1, INT_MAX);

        // 从节点k开始搜索
        int cur_node = k;
        distance[cur_node] = 0;
        int cur_distance = 0;
        while(1){
            flag[cur_node] = true;

            // 更新临边
            for(auto p : nodes[cur_node]){
                int v = p.first;
                int w = p.second;
                if(!flag[v]){
                    distance[v] = min(distance[v], cur_distance + w);
                }
            }

            // 获取下一个距离最小的节点
            int next_node = 0;
            for(int i = 1; i <= n; i++){
                if(!flag[i] && distance[i] < distance[next_node]){
                    next_node = i;
                }
            }
            if(next_node == 0)  break;  // 找不到下一个节点 跳出循环
            
            cur_node = next_node;
            cur_distance = distance[cur_node];
            res = max(res, cur_distance);

        }

        // 遍历数组判断是否存在未通知到的数据
        for(int i = 1; i <= n; i++){
            if(!flag[i])    return -1;
        }
        return res;
    }
};
```