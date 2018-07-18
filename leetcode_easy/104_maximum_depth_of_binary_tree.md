## Maximum Depth of Binary Tree
##### 2018年02月13日11:32:52
##### 二叉树....
***
### 题目
>Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.  
给定一个二叉树，找到它的最大深度。 最大深度是从根节点到最远叶节点沿着最长路径的节点数量。

### 分析
看到题目直接想到了递归，稍微理解二叉树就很容易写出来。
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
int maxDepth(struct TreeNode* root) {
    if(root == NULL)
        return 0;
    int a=maxDepth(root->left);
    int b=maxDepth(root->right);
    if(a>b)
        return 1+a;
    else
        return 1+b;
}
```
