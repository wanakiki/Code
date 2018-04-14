## 94. Binary Tree Inorder Traversal
##### 2018-04-14 17:41:21
##### 二叉树中序遍历
***
## 1.题目
>Given a binary tree, return the inorder traversal of its nodes' values.  
Note: Recursive solution is trivial, could you do it iteratively?  
>给定一个二叉树，返回它的节点值的inorder遍历。注意：递归解决方案是微不足道的，你可以迭代执行吗？

## 2.分析
起初以为只是遍历二叉树，暴露了自己的无知。
#### 二叉树的遍历
遍历即将树的所有结点访问且仅访问一次。按照根节点位置的不同分为前序遍历，中序遍历，后序遍历。
- 前序遍历：根节点->左子树->右子树
- 中序遍历：左子树->根节点->右子树
- 后序遍历：左子树->右子树->根节点

正如题目所说，递归版本很容易就实现了，迭代算法要用到栈，暂时留坑。
下面是递归解决方案
## 3.代码
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
   vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        change(res,root);
        return res;
    }

    void change(vector<int> &res,TreeNode * root){
      if(!root) return;
      if(root->left)  change(res,root->left);
      res.push_back(root->val);
      if(root->right) change(res,root->right);
    }
};
```
