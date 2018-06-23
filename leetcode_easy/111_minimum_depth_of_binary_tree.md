##  Minimum Depth of Binary Tree
##### 2018年02月15日10:40:18
##### 二叉树
***
### 题目
>Given a binary tree, find its minimum depth.  
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.  
给定一个二叉树，找到它的最小深度。 最小深度是沿着从根节点到最近叶节点的最短路径的节点数量。

### 分析
用递归的方法很容易解决这个问题  
但是要注意对于``[1,#,2]``类似的情况，最小的深度是二。

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
int minDepth(struct TreeNode* root) {
    if(root==NULL)
        return 0;
    int a=minDepth(root->left);
    int b=minDepth(root->right);
    if(a==0)
        return 1+b;
    if(b==0)
        return 1+a;
    return a>b ? 1+b : 1+a;
}
```
