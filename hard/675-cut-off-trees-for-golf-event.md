## 675. 为高尔夫比赛砍树

2022-05-23 20:52:06

### 题目

你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 ``m x n`` 的矩阵表示，在这个矩阵中：


- ``0`` 表示障碍，无法触碰
- ``1`` 表示地面，可以行走
- ``比 1 大的数`` 表示有树的单元格，可以行走，数值表示树的高度


每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒 
它。

你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 ``1``（即变为地面）。

你将从 ``(0, 0)`` 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 ``-1`` 。    

可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

 

**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/trees1.jpg" style="width: 242px; height: 242px;" />
```
输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。
```

**示例 2：**
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/trees2.jpg" style="width: 242px; height: 242px;" />
```
输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。
```

**示例 3：**

```
输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。
```

 

**提示：**


- ``m == forest.length``
- ``n == forest[i].length``
- ``1 <= m, n <= 50``
- ``0 <= forest[i][j] <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/cut-off-trees-for-golf-event/)

### 思路及代码

搜索题目，本质上是寻找高度相邻树木之间的最短距离。将所有树的坐标及高度进行记录，并按照高度升序排序。从起始节点出发，使用广度优先搜索查找到高度数组中第一个节点的距离，累加距离数值。以新找到的节点作为起点，进一步寻找下一个待砍伐的树。

```cpp
class Solution {
public:
    int cutOffTree(vector<vector<int>>& forest) {
        int m = forest.size();
        int n = forest[0].size();
        int mask = max(m, n);
        vector<vector<int>> directions = {{1,0}, {-1,0}, {0, 1}, {0, -1}};
        vector<vector<int>> tree;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(forest[i][j] > 1){
                    tree.push_back({forest[i][j], i, j});
                }
            }
        }

        sort(tree.begin(), tree.end(), [&](const vector<int>& a, const vector<int>& b){
            return a[0] < b[0];
        });


        // 使用广搜进行寻路
        int res = 0;
        queue<pair<int,int>> q;
        q.emplace(make_pair(0,0));
        for(int i = 0; i < tree.size(); i++){
            bool flag = false;
            //cout << tree[i][1] << ' ' << tree[i][2] << endl;
            vector<vector<bool>> visited(m, vector<bool>(n, false));
            while(!q.empty()){
                auto cur = q.front();
                q.pop();

                int cur_x = cur.first / mask;
                int cur_y = cur.first % mask;
                int cur_time = cur.second;
                if(visited[cur_x][cur_y])   continue;
                visited[cur_x][cur_y] = true;

                if(cur_x == tree[i][1] && cur_y == tree[i][2]){
                    forest[cur_x][cur_y] = 1; // 砍树
                    res += cur_time;
                    flag = true;
                    
                    // 手动清空队列元素
                    while(!q.empty())   q.pop();

                    q.emplace(make_pair(cur_x*mask +  cur_y, 0));
                    break;
                }
                else{
                    for(int j = 0; j < 4; j++){
                        int next_x = cur_x + directions[j][0];
                        int next_y = cur_y + directions[j][1];

                        // 只有障碍不可越过
                        if(next_x >= 0 && next_x < m && next_y >= 0 && next_y < n && visited[next_x][next_y]==false && forest[next_x][next_y] != 0){
                            q.emplace(make_pair(next_x * mask + next_y, cur_time + 1));
                        }
                    }
                }
            }

            if(!flag)   return -1;  // 不可达
        }
        return res;
    }
};
```

采用广搜的做法虽然能够找到最短距离，但整体复杂度较高，进行了较多的无用搜索。可以使用 A* 或者 dijkstra 提高搜索效率。