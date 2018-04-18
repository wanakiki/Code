## 98. Validate Binary Search Tree
##### 2018-04-18 17:28:49
##### 验证二叉搜索树
***
## 1.题目
>Given a binary tree, determine if it is a valid binary search tree (BST).
>
>Assume a BST is defined as follows:
>
>- The left subtree of a node contains only nodes with keys less than the node's key.
>- The right subtree of a node contains only nodes with keys greater than the node's key.
>- Both the left and right subtrees must also be binary search trees.  
>
>验证所给二叉树是否为二叉搜索树，二叉搜索树的定义如下：
>- 节点的左侧子树只包含密钥小于节点密钥的节点。
>- 节点的右侧子树只包含密钥大于节点密钥的节点。
>- 左边和右边的子树也必须是二叉搜索树。
## 2.分析
最开始的做法是对左右两支分别判断，各自列了一个函数但是没有考虑到右支的节点存在最小值，左支的节点存在最大值的情况，运行出错。每个节点都有其被限制好的范围。

尽管发现了这个问题，但花了很长时间还是没有设计出来好的解决办法，感觉就在眼前却怎么也摸不到.....  

还是自己的经验不够充分，明明已经总结出了每个节点都具有的特性却写不出来解决方法。参照别人的代码，函数设立三个参数，在函数内判断值节点值是否满足条件，同时不断更新下一个节点值的范围。  
还要注意，初始的范围应大于int型的范围。

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
    bool isValidBST(TreeNode* root) {
        return helper(root,LONG_MIN,LONG_MAX);
    }
    bool helper(TreeNode *root,long min,long  max){
        if(!root)   return true;
        if(root->val<=min || root->val >=max)   return false;
        else return helper(root->left,min,root->val) && helper(root->right,root->val,max);
    }
};
```
看到的不需要INT_MAX INT_MIN的方法，按顺序遍历
```cpp
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        TreeNode* prev = NULL;
        return validate(root, prev);
    }
    bool validate(TreeNode* node, TreeNode* &prev) {
        if (node == NULL) return true;
        if (!validate(node->left, prev)) return false;
        if (prev != NULL && prev->val >= node->val) return false;
        prev = node;
        return validate(node->right, prev);
    }
};
```
