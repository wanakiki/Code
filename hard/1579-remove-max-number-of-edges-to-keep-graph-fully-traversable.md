## 1701. 保证图可完全遍历

2021-01-27 13:26:22

### 题目

Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：


- 类型 1：只能由 Alice 遍历。
- 类型 2：只能由 Bob 遍历。
- 类型 3：Alice 和 Bob 都可以遍历。


给你一个数组 ``edges`` ，其中 ``edges[i] = [type<sub>i</sub>, u<sub>i</sub>, v<sub>i</sub>]`` 表示节点 ``u<sub>i</sub>`` 和 ``v<sub>i</sub>`` 之间存在类型为 ``type<sub>i</sub>`` 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。

返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。

 

**示例 1：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/06/5510ex1.png" style="height: 191px; width: 179px;">**

```
输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
输出：2
解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。
```

**示例 2：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/06/5510ex2.png" style="height: 190px; width: 178px;">**

```
输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
输出：0
解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。
```

**示例 3：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/06/5510ex3.png" style="height: 190px; width: 178px;">**

```
输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
输出：-1
解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。
```

 

**提示：**


- ``1 <= n <= 10^5``
- ``1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)``
- ``edges[i].length == 3``
- ``1 <= edges[i][0] <= 3``
- ``1 <= edges[i][1] < edges[i][2] <= n``
- 所有元组 ``(type<sub>i</sub>, u<sub>i</sub>, v<sub>i</sub>)`` 互不相同



### 思路及代码

虽然是个困难题，但是思路比较简单。对于题目中所给的三种类型的边，容易想到要优先保留第三种类型的通用边。在保留最简通用边之后，再去求A、B两人构成连通图最小的边。因此首先遍历通用边，构成局部联通的一个个子图，在此基础之上，对A、B两人的专用边进行遍历，如果专用边连接的两个节点不连通，则将新的边加入。

```cpp
class UnionFind{
public:
    vector<int> parent;
    int n;
    int count;
    UnionFind(int _n) : n(_n), count(_n), parent(_n){
        for(int i = 0; i < _n; i++){
            parent[i] = i;
        }
    }

    int findx(int x){
        if(parent[x] != x){
            parent[x] = findx(parent[x]);
        }
        return parent[x];
    }

    bool unite(int x, int y){
        x = findx(x);
        y = findx(y);
        if(x == y){
            return false;
        }
        else{
            parent[y] = x;
            count--;
            return true;
        }
    }

    bool connected(int x, int y){
        return findx(x) == findx(y);
    }
};
class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        UnionFind ufa(n), ufb(n);
        int res = 0;
        //使节点编号从零开始
        for(auto& nums : edges){
            nums[1]--;
            nums[2]--;
        }

        // 通用边
        for(int i = 0; i < edges.size(); i++){
            if(edges[i][0] == 3){
                if(!ufa.unite(edges[i][1], edges[i][2])){
                    // 两者已经联通 当前通用边可删除
                    res++;
                }
                else{
                    ufb.unite(edges[i][1], edges[i][2]);
                }
            }
        }
       

        // 特殊边
        for(int i = 0; i < edges.size(); i++){
            if(edges[i][0] == 1){
                if(!ufa.unite(edges[i][1], edges[i][2])){
                    res++;
                }
            }
            else if(edges[i][0] == 2){
                if(!ufb.unite(edges[i][1], edges[i][2])){
                    res++;
                }
            }
        }

        if(ufb.count != 1 || ufa.count != 1){
            return -1;
        }
        else{
            return res;
        }
    }
};
```