## 1227. 等价多米诺骨牌对的数量

2021-01-26 17:49:34

### 题目

给你一个由一些多米诺骨牌组成的列表 ``dominoes``。

如果其中某一张多米诺骨牌可以通过旋转 ``0`` 度或 ``180`` 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上，``dominoes[i] = [a, b]`` 和 ``dominoes[j] = [c, d]`` 等价的前提是 ``a==c`` 且 ``b==d``，或是 ``a==d`` 且 ``b==c``。

在 ``0 <= i < j < dominoes.length`` 的前提下，找出满足 ``dominoes[i]`` 和 ``dominoes[j]`` 等价的骨牌对 ``(i, j)`` 的数量。

 

**示例：**

```
输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
```

**提示：**


- ``1 <= dominoes.length <= 40000``
- ``1 <= dominoes[i][j] <= 9``


### 思路及代码

哈希表统计相同骨牌的数目，之后计算可能的等价对。

```cpp
class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<int, int> my_hash;
        for(int i = 0; i < dominoes.size(); i++){
            int a = min(dominoes[i][0], dominoes[i][1]);
            int b = max(dominoes[i][0], dominoes[i][1]);
            int cur = a * 10 + b;
            my_hash[cur]++;
        }

        int res = 0;
        for(auto it = my_hash.begin(); it != my_hash.end(); it++){
            int cur = it->second;
            res += (cur - 1) * cur / 2;
        }
        return res;
    }
};
```

结合题目所给数据范围可以直接用数组存储骨牌，并在统计过程中计算结果。

```cpp
class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        int res = 0;
        vector<int> count(100, 0);
        for(int i = 0; i < dominoes.size(); i++){
            int a = min(dominoes[i][0], dominoes[i][1]);
            int b = max(dominoes[i][0], dominoes[i][1]);
            int cur = a * 10 + b;
            res += count[cur];
            count[cur]++;
        }
        return res;
    }
};
```