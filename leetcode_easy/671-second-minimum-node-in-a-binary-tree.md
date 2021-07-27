## 671. 二叉树中第二小的节点

2021-07-27 09:46:16

### 题目

给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 ``2`` 或 ``0``。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个
。

更正式地说，``root.val = min(root.left.val, root.right.val)`` 总成立。

给出这样的一个二叉树，你需要输出所有节点中的**第二小的值。**如果第二小的值不存在的话，输出 -1 **。**

 

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg" style="width: 431px; height: 302px;" />

```
输入：root = [2,2,5,null,null,5,7]
输出：5
解释：最小的值是 2 ，第二小的值是 5 。
```

**示例 2：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg" style="width: 321px; height: 182px;" />

```
输入：root = [2,2,2]
输出：-1
解释：最小的值是 2, 但是不存在第二小的值。
```

 

**提示：**


- 树中节点数目在范围 ``[1, 25]`` 内
- ``1 <= Node.val <= 2<sup>31</sup> - 1``
- 对于树中每个节点 ``root.val == min(root.left.val, root.right.val)``



[LeetCode链接](https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/)

### 思路及代码

深度优先搜索配合二叉树特性剪枝，相似的思路代码写出来没有官方题解看起来简单，还有可以改进的地方。

首先根节点对应的值一定是所有叶子节点中最小的，从根节点出发开始遍历二叉树，存在三种情况

- 无左右孩子，此时遍历终止
- 左右孩子数值相等，应对左右孩子分别搜索数据中第二大的值
- 左右孩子数值不等，此时必有一个节点的值与最小值相等，则另一节点的值可以作为结果候选，对左侧子树进行搜索，判断是否有更小的值

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
    int findSecondMinimumValue(TreeNode* root) {
        // 根节点值一定最小
        int min_val = root->val;    // 已知根节点不为空
        int res = -1;

        stack<TreeNode*> stk;
        stk.push(root);
        while(!stk.empty()){
            auto cur = stk.top();
            stk.pop();

            if(cur->left == nullptr)    continue;

            // 当两个节点值相等时均需要压栈
            if(cur->left->val == cur->right->val){
                if(cur->left->val == min_val){
                    stk.push(cur->right);
                    stk.push(cur->left);
                }
                else{
                    if(res == -1){
                        res = cur->left->val;
                    }
                    else{
                        res = min(res, cur->left->val);     // 应该无法到达
                    }
                }
            }
            else{
                int tmp;    // 暂存第二小的可选值
                if(cur->left->val == min_val){
                    stk.push(cur->left);
                    tmp = cur->right->val;
                }
                else{
                    // 此时根节点一定和右孩子等值
                    stk.push(cur->right);
                    tmp = cur->left->val;
                }

                if(res == -1){
                    res = tmp;
                }
                else{
                    res = min(res, tmp);
                }
            }
        }

        return res;
    }
};
```