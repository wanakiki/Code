## 886. 可能的二分法

2022-10-16 15:55:51

### 题目

给定一组 ``n`` 人（编号为 ``1, 2, ..., n``）， 我们想把每个人分进**任意**大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。

给定整数 ``n`` 和数组 ``dislikes`` ，其中 ``dislikes[i] = [a<sub>i</sub>, b<sub>i</sub>]`` ，表示不允许将编号为 ``a<sub>i</sub>`` 和  ``b<sub>i</sub>``的人归入同一组。当可以用这种方法将所有人分进两组时，返回 ``true``；否则返回 ``false``。






**示例 1：**

```

输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]
```

**示例 2：**

```

输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false
```

**示例 3：**

```

输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false
```



**提示：**


- ``1 <= n <= 2000``
- ``0 <= dislikes.length <= 10<sup>4</sup>``
- ``dislikes[i].length == 2``
- ``1 <= dislikes[i][j] <= n``
- ``a<sub>i</sub> < b<sub>i</sub>``
- ``dislikes`` 中每一组都 **不同**





[LeetCode链接](https://leetcode-cn.com/problems/possible-bipartition/)

### 思路及代码

二分图判定题目，采用染色法，最终只有两种颜色，且必须保证与不喜欢的人异色。采用并查集求解，遍历成员i，将其所有不喜欢的人合并到相同集合，再判断i是否在该集合内，如果发现冲突则无法染色。

```cpp
class Solution {
public:
    int findx(int x, vector<int>& parent){
        if(x == parent[x]){
            return x;
        }
        else{
            parent[x] = findx(parent[x], parent);
            return parent[x];
        }
    }

    void unit(int a, int b, vector<int>& parent){
        int p_a = findx(a, parent);
        int p_b = findx(b, parent);

        if(p_a != p_b){
            parent[p_a] = p_b;
        }
    }
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<vector<int>> my_dis(n+1);
        vector<int> parent(n + 1, 0);
        for(int i = 1; i <= n; i++) parent[i] = i;


        for(int i = 0; i < dislikes.size(); i++){
            my_dis[dislikes[i][0]].push_back(dislikes[i][1]);
            my_dis[dislikes[i][1]].push_back(dislikes[i][0]);
        }

        for(int i = 1; i <= n; i++){
            for(int j = 1; j < my_dis[i].size(); j++){
                // 将每个人不喜欢的人进行合并
                unit(my_dis[i][0], my_dis[i][j], parent);

                if(findx(i, parent) == findx(my_dis[i][j], parent)) return false;
            }
        }
        return true;
    }
};
```