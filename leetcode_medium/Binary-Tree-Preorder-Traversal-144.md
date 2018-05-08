## 144. Binary Tree Preorder Traversal
##### 2018-05-08 16:37:20
##### 二叉树前序遍历
****
## 题目
Given a binary tree, return the preorder traversal of its nodes' values.

Example:
```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
```
Follow up: Recursive solution is trivial, could you do it iteratively?
## 分析
没什么值得多说的，就是将二叉树前序遍历之后存储到一个数组，并将其返回，需要注意的位置是存储的变量需要为全局变量，或者传入引用。
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        helper(root,res);
        return res;
    }
    void helper(TreeNode * root,vector<int> & res){
        if(!root)
            return;
        res.push_back(root->val);
        helper(root->left,res);
        helper(root->right,res);
    }
};
```
看了下最快的解法，使用了栈
```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;

        if (root == nullptr)
            return ret;

        stack<TreeNode*> st;
        st.push(root);

        while(!st.empty()) {
            TreeNode* tp = st.top();
            st.pop();
            ret.push_back(tp->val);
            if (tp->right != nullptr) st.push(tp->right);
            if (tp->left != nullptr) st.push(tp->left);
        }

        return ret;
    }
};
```
