## 106. Construct Binary Tree from Inorder and Postorder Traversal
##### 2018-04-23 18:50:51
##### 从前序和后序遍历还原二叉树
***
## 题目
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.  
给定树的顺序遍历和后序遍历，构造二叉树。
注意：
你可以认为树中不存在重复项。

For example, given
```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```
Return the following binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```
## 解析
和105题非常相似，感觉自己要一个方法吃到老了.....同样的思路，这次花了63ms，8.56%
等着填坑
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return helper(inorder,0,inorder.size()-1,postorder,0,postorder.size()-1);
    }

    TreeNode * helper(vector<int> & inorder,int il,int ir,vector<int> postorder,int pl,int pr ){
        if(il>ir)   return NULL;
        TreeNode * root=new TreeNode(postorder[pr]);
        for(int i=il;i<=ir;i++){
            if(inorder[i] == postorder[pr]){
                root -> left = helper(inorder,il,i-1,postorder,pl,pl+i-1-il);
                root -> right = helper(inorder,i+1,ir,postorder,pl+i-il,pr-1);
            }
        }
        return root;
    }
};
```
