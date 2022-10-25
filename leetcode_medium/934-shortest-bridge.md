## 934. 最短的桥

2022-10-25 09:38:19

### 题目

给你一个大小为 ``n x n`` 的二元矩阵 ``grid`` ，其中 ``1`` 表示陆地，``0`` 表示水域。

**岛** 是由四面相连的 ``1`` 形成的一个最大组，即不会与非组内的任何其他 ``1`` 相连。``grid`` 中 **恰好存在两座岛** 。

<div class="original__bRMd">
<div>
你可以将任意数量的 ``0`` 变为 ``1`` ，以使两座岛连接起来，变成 **一座岛** 。

返回必须翻转的 ``0`` 的最小数目。
</div>
</div>



**示例 1：**

```

输入：grid = [[0,1],[1,0]]
输出：1
```

**示例 2：**

```

输入：grid = [[0,1,0],[0,0,0],[0,0,1]]
输出：2
```

**示例 3：**

```

输入：grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1
```



**提示：**


- ``n == grid.length == grid[i].length``
- ``2 <= n <= 100``
- ``grid[i][j]`` 为 ``0`` 或 ``1``
- ``grid`` 中恰有两个岛



[LeetCode链接](https://leetcode-cn.com/problems/shortest-bridge/)

### 思路及代码

两次广搜，第一次找第一个岛屿的元素并标记，第二次广搜找到联通第二个岛屿的最短路。

广搜写了两次，代码有点长，感觉可以自己写一些模板了。

```cpp
class Solution {
public:
    vector<vector<int>> directions = {{0,1}, {0, -1}, {1, 0}, {-1, 0}};
    int shortestBridge(vector<vector<int>>& grid) {
        // 第一次广搜 找到联通的岛屿并标记
        vector<vector<int>> island(grid.size(), vector<int>(grid.size(), 0));
        queue<pair<int,int>> myq;
        queue<pair<int,int>> myq_path;

        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid.size(); j++){
                if(grid[i][j] == 1){
                    myq.push(make_pair(i, j));
                    break;
                }
            }

            if(!myq.empty())    break;
        }


        while(!myq.empty()){
            int cur_size = myq.size();
            while(cur_size--){
                auto p = myq.front();
                myq.pop();

                int i = p.first;
                int j = p.second;

                if(island[i][j])    continue;
                island[i][j] = 1;


                for(int k = 0; k < 4; k++){
                    int next_i = i + directions[k][0];
                    int next_j = j + directions[k][1];

                    if(next_i >=0 && next_i < grid.size() && next_j >= 0 && next_j < grid.size() && island[next_i][next_j] == 0){
                        if(grid[next_i][next_j] == 1){
                            myq.push(make_pair(next_i, next_j));
                        }
                        else{
                            myq_path.push(make_pair(next_i, next_j));
                        }
                    }
                }
            }
        }


        // 广搜所有的边缘水域 找到最短联通路径 路径长度即为答案
        int res = 1;
        while(!myq_path.empty()){
            int cur_size = myq_path.size();
            while(cur_size--){
                auto p = myq_path.front();
                myq_path.pop();

                int i = p.first;
                int j = p.second;

                if(island[i][j] == 2)    continue;
                island[i][j] = 2;


                for(int k = 0; k < 4; k++){
                    int next_i = i + directions[k][0];
                    int next_j = j + directions[k][1];

                    if(next_i >=0 && next_i < grid.size() && next_j >= 0 && next_j < grid.size() && island[next_i][next_j] == 0){
                        if(grid[next_i][next_j] == 0){
                            myq_path.push(make_pair(next_i, next_j));
                        }
                        else{
                            return res;
                        }
                    }
                }
            }
            res++;
        }
        return res;
    }
};
```