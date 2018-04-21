## 103. Binary Tree Zigzag Level Order Traversal
##### 2018-04-20 23:13:31
##### 二叉树锯齿水平遍历
***
## 1.题目
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).  
给定一个二叉树，返回其节点值的锯齿级顺序遍历。 （即，从左到右，然后从右到左进入下一个级别并在其间交替）。

For example:
Given binary tree [3,9,20,null,null,15,7],
```
3
/ \
9  20
/  \
15   7
```
return its zigzag level order traversal as:
```
[
  [3],
  [20,9],
  [15,7]
]
```

## 2.分析
与之前的二叉树级别遍历相似，不过这次的要求是达到之字形的路线。  
如果我来写这个算法，我一定会选择deque来写，这样很方便的根据层数选择在开头还是结尾添加变量就可以解决问题了。

大体做法与102题相同，只是需要根据当前层数的奇偶性来判断添加元素的位置，vector 需要使用insert(a.begin(),num) 这种写法来达到在开头添加元素的目的。

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        helper(res,root,0);
        return res;
    }
    void helper(vector<vector<int>> & res,TreeNode *root,int lev){
        if(!root)   return;
        if(res.size()==lev)
            res.push_back(vector<int>());
        if(lev%2){
            res[lev].insert(res[lev].begin(),root->val);
        }
        else
            res[lev].push_back(root->val);
        helper(res,root->left,lev+1);
        helper(res,root->right,lev+1);
    }
};
```
