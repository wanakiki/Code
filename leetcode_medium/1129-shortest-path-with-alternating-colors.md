## 1129. 颜色交替的最短路径

2023-02-02 12:55:46

### 题目

在一个有向图中，节点分别标记为 ``0, 1, ..., n-1``。图中每条边为红色或者蓝色，且存在自环或平行边。

``red_edges`` 中的每一个 ``[i, j]`` 对表示从节点 ``i`` 到节点 ``j`` 的红色有向边。类似地，``blue_edges`` 中的每一个 ``[i, j]`` 对表示从节点 ``i`` 到节点 ``j`` 的蓝色有向边。

返回长度为 ``n`` 的数组 ``answer``，其中 ``answer[X]`` 是从节点 ``0`` 到节点 ``X`` 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 ``answer[x] = -1``。

 

**示例 1：**

```

输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]
```

**示例 2：**

```

输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]
```

**示例 3：**

```

输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
输出：[0,-1,-1]
```

**示例 4：**

```

输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
输出：[0,1,2]
```

**示例 5：**

```

输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
输出：[0,1,1]
```

 

**提示：**


- ``1 <= n <= 100``
- ``red_edges.length <= 400``
- ``blue_edges.length <= 400``
- ``red_edges[i].length == blue_edges[i].length == 2``
- ``0 <= red_edges[i][j], blue_edges[i][j] < n``



[LeetCode链接](https://leetcode-cn.com/problems/shortest-path-with-alternating-colors/)

### 思路及代码

```cpp
class Solution {
public:
    enum Color {RED, BLUE};
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges, vector<vector<int>>& blueEdges) {
        vector<int> res(n, -1);
        vector<bool> red_visit(n, false);
        vector<bool> blue_visit(n, false);

        unordered_map<int, unordered_set<int>> red;
        unordered_map<int, unordered_set<int>> blue;
        for(auto p : redEdges){
            red[p[0]].insert(p[1]);
        }
        for(auto p : blueEdges){
            blue[p[0]].insert(p[1]);
        }


        // 广度优先
        int path_len = 0;
        queue<pair<int, Color>> q;
        q.push({0, RED});
        q.push({0, BLUE});

        while(!q.empty()){
            int q_size = q.size();
            while(q_size--){
                int cur_node = q.front().first;
                Color last_color = q.front().second;
            q.pop();


            // 先判断是否被访问过，之后设置访问颜色
            if(res[cur_node] == -1) res[cur_node] = path_len;
            if(last_color == RED){
                    if(red_visit[cur_node]){
                        continue;
                    }
                    else{
                        red_visit[cur_node] = true;
                    }
                }
                else{
                    if(blue_visit[cur_node]){
                        continue;
                    }
                    else{
                        blue_visit[cur_node] = true;
                    }
                }

                if(last_color == RED){
                    for(auto next_node : blue[cur_node]){
                        q.push({next_node, BLUE});
                    }
                }
                else{
                    for(auto next_node : red[cur_node]){
                        q.push({next_node, RED});
                    }
                }
            }

            path_len++;
        }
        return res;

    }
};
```