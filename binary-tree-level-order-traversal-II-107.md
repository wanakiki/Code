## 107. Binary Tree Level Order Traversal II
##### 2018-05-27 22:29:05
##### 二叉树
***
## 题目
 Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
return its bottom-up level order traversal as:
```
[
  [15,7],
  [9,20],
  [3]
]
```
## 分析
二叉树题目，因为要求数组从底部开始，所以比较普遍的思路是先正向遍历存储元素，便利结束之后再将数组翻转，这样就能较快地解决这个问题。（最好不要按照从下到上的顺序来写.....会很麻烦）
## 示例代码
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
    void helper(vector<vector<int>> & res,int lev,TreeNode * root){
        if(!root)
            return ;
        if(res.size()<=lev)
            res.push_back(vector<int> ());
        res[lev].push_back(root->val);
        helper(res,lev+1,root->left);
        helper(res,lev+1,root->right);
    }
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if(!root)
            return res;
        helper(res,0,root);
        reverse(res.begin(),res.end());
        return res;
    }
};
```
