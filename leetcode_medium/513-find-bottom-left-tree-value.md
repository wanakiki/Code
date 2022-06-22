## 513. 找树左下角的值

2022-06-22 14:55:15

### 题目

给定一个二叉树的 **根节点** ``root``，请找出该二叉树的 **最底层 最左边** 节点的值。

假设二叉树中至少有一个节点。

 

**示例 1:**

<img src="https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg" style="width: 182px; " />

```
输入: root = [2,1,3]
输出: 1
```

**示例 2:**

<img src="https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg" style="width: 242px; " />

```
输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
```

 

**提示:**


- 二叉树的节点个数的范围是 ``[1,10<sup>4</sup>]``
- <meta charset="UTF-8" />``-2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1`` 



[LeetCode链接](https://leetcode-cn.com/problems/find-bottom-left-tree-value/)

### 思路及代码

按层遍历，用每层的第一个数据更新结果。

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
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);

        int val = -1;
        while(!q.empty()){
            int len = q.size();
            val = q.front()->val;
            while(len--){
                TreeNode* cur = q.front();
                if(cur->left){
                    q.push(cur->left);
                }
                if(cur->right){
                    q.push(cur->right);
                }
                q.pop();
            }
        }
        return val;
    }
};
```