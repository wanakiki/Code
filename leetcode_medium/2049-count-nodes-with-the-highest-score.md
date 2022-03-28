## 2049. 统计最高分的节点数目

2022-03-11 09:22:40

### 题目

给你一棵根节点为 ``0`` 的 **二叉树** ，它总共有 ``n`` 个节点，节点编号为 ``0`` 到 ``n - 1`` 。同时给你一个下标从 **0** 开始的整数数组 ``parents`` 表示这棵树，其中 ``parents[i]`` 是节点 ``i`` 的父节点。由于节点 ``0`` 是根，所以 ``parents[0] == -1`` 。

一个子树的 **大小** 为这个子树内节点的数目。每个节点都有一个与之关联的 **分数** 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 **删除** ，剩余部分是若干个 **非空** 子树，这个节点的 **分数** 为所有这些子树 **大小的乘积** 。

请你返回有 **最高得分** 节点的 **数目** 。



**示例 1:**

<img alt="example-1" src="https://assets.leetcode.com/uploads/2021/10/03/example-1.png" style="width: 604px; height: 266px;">

```
输入：parents = [-1,2,0,2,0]
输出：3
解释：
- 节点 0 的分数为：3 * 1 = 3
- 节点 1 的分数为：4 = 4
- 节点 2 的分数为：1 * 1 * 2 = 2
- 节点 3 的分数为：4 = 4
- 节点 4 的分数为：4 = 4
最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。
```

**示例 2：**

<img alt="example-2" src="https://assets.leetcode.com/uploads/2021/10/03/example-2.png" style="width: 95px; height: 143px;">

```
输入：parents = [-1,2,0]
输出：2
解释：
- 节点 0 的分数为：2 = 2
- 节点 1 的分数为：2 = 2
- 节点 2 的分数为：1 * 1 = 1
最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。
```



**提示：**


- ``n == parents.length``
- ``2 <= n <= 10<sup>5</sup>``
- ``parents[0] == -1``
- 对于 ``i != 0`` ，有 ``0 <= parents[i] <= n - 1``
- ``parents`` 表示一棵二叉树。



[LeetCode链接](https://leetcode-cn.com/problems/count-nodes-with-the-highest-score/)

### 思路及代码

根据输入的 parents 数组，可以完成对二叉树的还原，这里推荐使用数组进行保存，不维护指针。

在得到二叉树之后，问题就变为如何得到每个 node 对应左右子节点构成的子树的大小，由于已知总节点个数，得到上述两个量之后，便能通过减法计算出删除当前节点后，根节点对应子树的大小，上述三个量的乘积便是当前节点的分数。

这里推荐使用递归形式编写的深度优先搜索，函数返回值是每个节点对应子树的大小。

```cpp
class Solution {
public:
    int res = 0;
    long long max_val = -1;
    int helper(vector<int>& parents, vector<int>& left, vector<int>& right, int cur = 0){
        if(cur == -1)   return 0;
        int left_node = left[cur];
        int right_node = right[cur];

        int left_count = helper(parents, left, right, left_node);
        int right_count = helper(parents, left, right, right_node);

        long long cur_score = 1;
        if(left_count != 0){
            cur_score *= left_count;
        }
        if(right_count != 0){
            cur_score *= right_count;
        }

        int cur_count = left_count + right_count + 1;   // 当前节点对应子树的尺寸
        int top_count = parents.size() - cur_count;     // 删除当前节点后 以根节点为根构成子树的大小
        if(top_count != 0){
            cur_score *= top_count;
        }

        if(cur_score > max_val){
            max_val = cur_score;
            res = 1;
        }
        else if(cur_score == max_val){
            res ++;
        }

        return cur_count;
        }
    int countHighestScoreNodes(vector<int>& parents) {
        int len = parents.size();
        vector<int> left(len, -1);
        vector<int> right(len, -1);

        for(int i = 0; i < len; i++){
            if(parents[i] != -1){
                int cur = parents[i];
                if(left[cur] == -1){
                    left[cur] = i;
                }
                else{
                    right[cur] = i;
                }
            }
        }

        // 开始搜索保存每个节点对应的得分 已知根节点对应子树大小为len
        vector<int> count(len, 0);
        helper(parents, left, right);
        return res;
    }
};
```