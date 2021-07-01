## 1000063. 传递信息

2021-07-01 22:49:04 

### 题目

小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：


- 有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0
- 每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 
传信息）。
- 每轮信息必须需要传递给另一个人，且信息可重复经过同一个人


给定总玩家数 ``n``，以及按 ``[玩家编号,对应可传递玩家编号]`` 关系组成的二维数组 ``relation``。返回信息从小 A (编号 0 )  
经过 ``k`` 轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。

**示例 1：**

<blockquote>
输入：``n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3``

输出：``3``

解释：信息从小 A 编号 0 处开始，经 3 轮传递，到达编号 4。共有 3 种方案，分别是 0->2->0->4， 0->2->1->4， 0->2->3->4。   
</blockquote>

**示例 2：**

<blockquote>
输入：``n = 3, relation = [[0,2],[2,1]], k = 2``

输出：``0``

解释：信息不能从小 A 处经过 2 轮传递到编号 2
</blockquote>

**限制：**


- ``2 <= n <= 10``
- ``1 <= k <= 5``
- ``1 <= relation.length <= 90, 且 relation[i].length == 2``
- ``0 <= relation[i][0],relation[i][1] < n 且 relation[i][0] != relation[i][1]``



[LeetCode链接](https://leetcode-cn.com/problems/chuan-di-xin-xi/)

### 思路及代码

建图，深度优先搜索。

```cpp
class Solution {
public:
    set<string> s;

    void helper(int cur, int count, string path, int k, vector<vector<int>>& map){
        if(count == k){
            if(cur == map.size() - 1){
                s.emplace(path);
            }
            return ;
        }

        
        for(auto i : map[cur]){
            helper(i, count + 1, path + "-" + to_string(i), k, map);
        }
    }
    int numWays(int n, vector<vector<int>>& relation, int k) {
        vector<vector<int>> map(n);

        for(auto r : relation){
            map[r[0]].push_back(r[1]);
        }

        helper(0, 0, "0", k, map);
        return s.size();
    }
};
```


但实际上并不存在相同的路径，所以可以取消使用set对路径进行统计的代码，加快执行速度。

```cpp
class Solution {
public:
    set<string> s;

    void helper(int cur, int count, string path, int k, vector<vector<int>>& map){
        if(count == k){
            if(cur == map.size() - 1){
                s.emplace(path);
            }
            return ;
        }

        
        for(auto i : map[cur]){
            helper(i, count + 1, path + "-" + to_string(i), k, map);
        }
    }
    int numWays(int n, vector<vector<int>>& relation, int k) {
        vector<vector<int>> map(n);

        for(auto r : relation){
            map[r[0]].push_back(r[1]);
        }

        helper(0, 0, "0", k, map);
        return s.size();
    }
};
```