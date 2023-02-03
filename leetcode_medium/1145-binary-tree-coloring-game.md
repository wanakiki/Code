## 1145. 二叉树着色游戏

2023-02-03 10:13:06

### 题目

有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 ``root``，树上总共有 ``n`` 个节点，且 ``n`` 为奇数，其中每个节点上的值从 ``1`` 到 ``n`` 各不相同。

最开始时：


- 「一号」玩家从 ``[1, n]`` 中取一个值 ``x``（``1 <= x <= n``）；
- 「二号」玩家也从 ``[1, n]`` 中取一个值 ``y``（``1 <= y <= n``）且 ``y != x``。


「一号」玩家给值为 ``x`` 的节点染上红色，而「二号」玩家给值为 ``y`` 的节点染上蓝色。

之后两位玩家轮流进行操作，「一号」玩家先手。每一回合，玩家选择一个被他染过色的节点，将所选节点一个 **未着色 **的邻节点（即左右子节点、或父节点）进行染色（「一号」玩家染红色，「二号」玩家染蓝色）。

如果（且仅在此种情况下）当前玩家无法找到这样的节点来染色时，其回合就会被跳过。

若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。

现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 ``y`` 值可以确保你赢得这场游戏，则返回 ``true`` ；若无法获胜，就请返回 ``false`` 。
 

示例 1 ：

<img alt="" src="https://assets.leetcode.com/uploads/2019/08/01/1480-binary-tree-coloring-game.png" style="width: 500px; height: 310px;" />

```
输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
输出：true
解释：第二个玩家可以选择值为 2 的节点。
```

示例 2 ：

```
输入：root = [1,2,3], n = 3, x = 1
输出：false
```

 

**提示：**


- 树中节点数目为 ``n``
- ``1 <= x <= n <= 100``
- ``n`` 是奇数
- ``1 <= Node.val <= n``
- 树中所有值 **互不相同**



[LeetCode链接](https://leetcode-cn.com/problems/binary-tree-coloring-game/)

### 思路及代码

红色节点把整个二叉树划分成了三个区域，只要找到三个区域中的节点个数最大值并判断是否大于所有节点总数的一半即可。

实际实现代码时不需要像下面一样使用哈希表维护这么多的数据。

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    unordered_map<int, TreeNode*> hash;
    unordered_map<int, int> count;

    void helper(TreeNode* root){
        if(root == nullptr) return ;
        helper(root->left);
        helper(root->right);

        hash[root->val] = root;
        int cur_count = 1;
        if(root->left)  cur_count += count[root->left->val];
        if(root->right) cur_count += count[root->right->val];
        count[root->val] = cur_count;
        return ;
    }
    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        // 遍历二叉树获得每个节点可以染色的数目
        helper(root);

        // 红色节点把二叉树分为左子树 右子树 上级节点三个区域
        // 蓝色节点只能选择其中的一个区域进行染色
        // 如果有一个区域的节点数量大于其他两个区域和加1 则有必胜法则
        int left_count = 0;
        int right_count = 0;
        int parent_count = 0;
        TreeNode* red_node = hash[x];
        if(red_node->left)  left_count = count[red_node->left->val];
        if(red_node->right) right_count = count[red_node->right->val];
        parent_count = n - 1 - left_count - right_count;

        int max_count = max(left_count, max(right_count, parent_count));
        if(max_count > n /2)    return true;
        else    return false;
    }
};
```