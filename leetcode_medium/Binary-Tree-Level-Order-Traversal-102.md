## 102. Binary Tree Level Order Traversal
##### 2018-04-19 16:00:39
##### 二叉树级别遍历
***
## 1.题目
>Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
>给定一个二叉树，返回其节点值的级别遍历。 （即从左到右，逐级）。

## 2.分析
这道题算是相对简单的二叉树题目了，数据结构很清楚，用C++的容器很容易写出来。

每遍历到新的一层，首先检查该层是否构造容器，接着向该层添加元素，当遇到空的时候返回零。  辅助函数用lev标记当前的层，如果层数由0开始，则可以根据当前的层数是否等于返回vector的长度来判断该层是否被构建。（因为只有每层最左边的节点才会出现lev等于size的情况）
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        helper(root,0,res);
        return res;
    }
    void helper(TreeNode*root,int lev,vector<vector<int>> & res){
        if(!root)   return ;

        /*if(lev==res.size()) {
            vector<int> temp;
            temp.push_back(root->val);
            res.push_back(temp);
        }
        else{
            res[lev].push_back(root->val);
        }*/
        //上面这部分可以优化为下面的

        if(lev==res.size())
          res.push_back(vector<int> ())
        res[lev].push_back(root->val);

        helper(root->left,lev+1,res);
        helper(root->right,lev+1,res);
        return ;
    }
};
```
