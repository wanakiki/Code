## 820. 找到最终的安全状态

2021-01-27 19:20:42

### 题目

在有向图中, 我们从某个节点和每个转向处开始, 沿着图的有向边走。 如果我们到达的节点是终点 (即它没有连出的有向边), 我们停止。

现在, 如果我们最后能走到终点，那么我们的起始节点是*最终安全*的。 更具体地说, 存在一个自然数 ``K``,  无论选择从哪里开始行走, 我们走了不到 ``K`` 步后必能停止在一个终点。

哪些节点最终是安全的？ 结果返回一个有序的数组。

该有向图有 ``N`` 个节点，标签为 ``0, 1, ..., N-1``, 其中 ``N`` 是 ``graph`` 的节点数.  图以以下的形式给出: ``graph[i]`` 是节点 ``j`` 的一个列表，满足 ``(i, j)`` 是图的一条有向边。

```

示例：
输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
输出：[2,4,5,6]
这里是上图的示意图。

```

<img alt="Illustration of graph" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png" style="height:86px; width:300px" />

**提示：**


- ``graph`` 节点数不超过 ``10000``.
- 图的边数不会超过 ``32000``.
- 每个 ``graph[i]`` 被排序为不同的整数列表， 在区间 ``[0, graph.length - 1]`` 中选取。

[题目连接](https://leetcode-cn.com/problems/find-eventual-safe-states/)

### 思路及代码

题目的意思不是很清楚，最终目标是检查有向图中的环。判定一个节点是安全节点的条件是该节点出度为零，或者该节点只有一条指向安全节点的边。所以最后的解题思路是用逆向拓扑排序的方法，先找到出度为零的节点，并减少所有指向该节点的节点的出度，再查找是否有节点出度变成了零，加入到判断队列当中。

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        // 统计每个点的出度 以及输入点
        int n = graph.size();
        vector<int> flag(n, false); // 是否已经处理过的标识
        vector<int> count(n, 0);    // 出度
        vector<vector<int>> input_node(n, vector<int>{});

        for(int i = 0; i < graph.size(); i++){
            count[i] = graph[i].size();
            for(int j = 0; j < graph[i].size(); j++){
                input_node[graph[i][j]].push_back(i);
            }
        }

        queue<int> q;
        // 初始化队列
        for(int i = 0; i < n; i++){
            if(count[i] == 0){
                flag[i] = true;
                q.push(i);
            }
        }

        while(!q.empty()){
            int cur = q.front();
            q.pop();
            for(int i = 0; i < input_node[cur].size(); i++){
                int aim = input_node[cur][i];   // 当前处理输入节点
                if(flag[aim]){
                    continue;
                }
                count[aim] -= 1;
                if(count[aim] == 0){
                    flag[aim] = true;
                    q.push(aim);
                }
            }
        }

        // 统计安全节点
        vector<int> res;
        for(int i = 0; i < n; i++){
            if(flag[i]){
                res.push_back(i);
            }
        }
        return res;
    }
};
```