## 783. 二叉搜索树中的搜索

2021-11-26 10:26:03

### 题目

给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

例如，

```

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2
```

你应该返回如下子树:

```

      2
     / \
    1   3
```

在上述示例中，如果要找的值是 ``5``，但因为没有节点值为 ``5``，我们应该返回 ``NULL``。


[LeetCode链接](https://leetcode-cn.com/problems/search-in-a-binary-search-tree/)

### 思路及代码

根据二叉搜索树特点切换当前节点。

```
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
    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* res = root;

        while(res){
            if(res->val == val){
                return res;
            }
            else if(res->val < val){
                    res = res->right;
                }
            else{
                    res = res->left;
                }
        }
        return nullptr;
    }
};
```