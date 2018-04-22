## 105. Construct Binary Tree from Preorder and Inorder Traversal
##### 2018-04-22 22:24:18
##### 从前序和中序遍历构造二叉树
***
## 题目
Given preorder and inorder traversal of a tree, construct the binary tree.  

Note:
You may assume that duplicates do not exist in the tree.

给定树的前序和中序，构造二叉树。  
注意：
您可能会认为树中不存在重复项。
For example, given
```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```
Return the following binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```

## 分析
这道题我没有生产思路，我只是[知识](https://www.tianmaying.com/tutorial/LC105)的搬运工与受益者......

因为题目中含有二叉树元素不重复的条件，根据二叉树前序与中序遍历的特点，前序遍历集合的首个元素为根节点，根节点可以在中序遍历集合中找到，并且中序遍历的根节点将集合分割为了左树和右数，根据所得左数与右树的长度反过来也可以确定前序遍历中两树的位置。而分割的左树和右数又满足上面的条件。很明显，用递归可以解决。
为了使得左树右树区分明确，递归函数的参数需要有两种遍历方式对应的开始和结束位置，最开始为整个数组，但递归一次之后就发生了变化。
## 参考代码
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder,0,preorder.size()-1,inorder,0,inorder.size()-1);
    }

    TreeNode * helper(vector<int> & preorder,int pl,int pr,vector<int>& inorder,int il,int ir){
        if(pl>pr)   return NULL;
        TreeNode * root=new TreeNode(preorder[pl]);     //赋初始值，不然为空指针访问
        for(int i=il;i<=ir;i++){
            if(inorder[i]==preorder[pl]){
                root->left=helper(preorder,pl+1,pl+i-il,inorder,il,i-1);
                root->right=helper(preorder,pl+i-il+1,pr,inorder,i+1,ir);
            }
        }
        return root;
    }
};
```
