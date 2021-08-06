## 847. 访问所有节点的最短路径

2021-08-06 20:32:39

### 题目

存在一个由 ``n`` 个节点组成的无向连通图，图中的节点按从 ``0`` 到 ``n - 1`` 编号。

给你一个数组 ``graph`` 表示这个图。其中，``graph[i]`` 是一个列表，由所有与节点 ``i`` 直接相连的节点组成。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。






**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest1-graph.jpg" style="width: 222px; height: 183px;" />

```
输入：graph = [[1,2,3],[0],[0],[0]]
输出：4
解释：一种可能的路径为 [1,0,2,0,3]
```

**示例 2：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest2-graph.jpg" style="width: 382px; height: 222px;" />

```
输入：graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
输出：4
解释：一种可能的路径为 [0,1,4,2,3]
```



**提示：**


- ``n == graph.length``
- ``1 <= n <= 12``
- ``0 <= graph[i].length < n``
- ``graph[i]`` 不包含 ``i``
- 如果 ``graph[a]`` 包含 ``b`` ，那么 ``graph[b]`` 也包含 ``a``
- 输入的图总是连通图



[LeetCode链接](https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes/)

### 思路及代码

是不会做的类型，参照官方题解把代码修修改改写了出来，基本理解了方法，在这里复述一遍。

采取的方法是状态压缩配合广度优先搜索，首先应该想到图搜索/遍历，之后再考虑状态压缩，二者的结合是关键步骤。采用状态压缩的原因是：为了在搜索过程中了解当前的状态（本题指节点的访问情况），需要对不同状态进行保存并在搜索过程中更新和传递。直接使用布尔数组保存会增加程序的复杂程度，鉴于本体节点个数小于等于12，可以直接使用12位二进制数代表节点是否被访问。

审题可以发现，搜索过程需要的参数分别是当前访问节点、当前全局节点访问情况以及在此情况下访问到本节点对应的路径长度。需要注意的是，本题保证数据是连通图，必然存在通路满足条件。

在此基础之上，便可对于上述三维数据使用搜索算法对路径进行查找，由于题目要求的是所有路径中最短的路径，可以考虑使用广度优先搜索算法。首先将所有的节点添加到队列当中，之后访问队列元素，根据graph数组访问节点临边并将新的节点和全局访问状态添加到队列当中。重复该过程，保存遇到的最短路径。

由于题目条件允许对同一节点重复访问，为了避免出现在两个节点之间循环跳转的情况，需要额外使用一部分内存，保存已经遇到的（节点，全局访问信息），避免重复。

```cpp
class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        int res = INT_MAX;
        int n = graph.size();

        // unordered_map<pair<int, int>, int> count;    // 记录状态是否已经被搜索过
        // unordered_map使用pair作为键需要自定义哈希函数

        vector<vector<bool>> count(n, vector<bool>((1<<n) + 1, false));
        queue<tuple<int, int, int>> q;

        // 添加初始节点
        for(int i = 0; i < graph.size(); i++){
            q.emplace(i, 1<<i, 0);
            count[i][1<<i] = true;
        }

        // 广度优先搜索
        while(!q.empty()){
            auto [u, mask, dist] = q.front();       // 必须使用方括号对数据进行接收
            q.pop();

            // 判断是否已经走完
            if(mask == (1<<n) - 1){
                // return dist;
                res = min(res, dist);
                continue;
            }

            for(int i = 0; i < graph[u].size(); i++){
                int next_u = graph[u][i];
                int next_mask = mask | (1 << next_u);
                if(!count[next_u][next_mask]){
                    q.emplace(next_u, next_mask, dist + 1);
                    count[next_u][next_mask] = true;
                }
            }
        }
        return res;
    }
};
```

首次了解到了C++中的tuple结构，之后可以不写一些超级简单的结构体了。

但目前还有几个问题：

1. 由于搜索的过程中带有不同的状态，很难想到搜索的过程是什么样的。
2. 按照以往的经验，最短路+广度搜索，第一个遇到的满足要求的结果便是真正的结果。修改代码提交之后发现本题同样适用，但是想不到怎么证明。
3. 上面的做法针对于本题非常有效，但不具备泛用性，更加泛用性的做法是状态压缩+动态规划，一个之前经常听到却没有详细了解过的算法。