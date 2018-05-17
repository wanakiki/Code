## 199. Binary Tree Right Side View
##### 2018-05-17 19:22:23
##### 从右边看的二叉树
***
## 题目
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```
## 分析
发现最近二叉树的题目好像都没太大的困难，这个题也很简单，找到每层最右边的数据，具体看代码吧。
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
    int lev =0;
    void helper(TreeNode * root,vector<int> & res,int l){
        if(!root)
            return ;
        if(l==lev){
            res.push_back(root->val);
            lev++;
        }
        if(root->right)
            helper(root->right,res,l+1);
        if(root->left)
            helper(root->left,res,l+1);
    }
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        helper(root,res,0);
        return res;
    }
};
```
运行速度还很快 100%

