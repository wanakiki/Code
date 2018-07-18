## 112. Path Sum
##### 2018年02月15日12:21:11
##### 二叉樹
****
### 題目
>Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.  
给定一棵二叉树和一个和，确定树是否有根到叶的路径，以便沿路径加起来的所有值等于给定的总和。

### 分析
说不出来什么过程，感觉对二叉树还需要更深刻的理解。  
我的做法是用递归，对每个节点进行判断，最后达成目标。方法很简单，但是怎样判断最简单是个值得探讨的问题。
### 代码
```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool hasPathSum(struct TreeNode* root, int sum) {
    if(root==NULL)
        return false;
    if(root->left==NULL&&root->right==NULL){
        if(root->val!=sum)
            return false;
        else
            return true;
    }   //必须提前返回真终止判断
    if(!hasPathSum(root->left,sum-root->val) && !hasPathSum(root->right,sum-root->val))
        return false;
    return true;
}
```
