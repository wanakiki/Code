## 110. Balanced Binary Tree
##### 2018-05-23 23:56:12
##### 简单题 平衡二叉树
***
## 题目
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

>a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:
```
    3
   / \
  9  20
    /  \
   15   7
``
Return true.

Example 2:
```
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
```
## 分析
平衡二叉树是两个子树的长度相差不超过1，并且两个子树都是平衡树的二叉树。

需要根据这两个条件判断，写一个判断深度的函数，再写一个判断是否为平衡二叉树的函数，用递归解决。
尽管感觉这样会很慢，但是大家的方法基本都是这个速度。

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
    
    int depth(TreeNode * root){
        if(!root)
            return 0;
        return 1+max(depth(root->left),depth(root->right));
    }
    
    bool isBalanced(TreeNode* root) {
        if(!root)
            return true;
        return (abs(depth(root->left)-depth(root->right))<=1 && isBalanced(root->left) && isBalanced(root->right)) ? true : false;
    }
    
    
};
```
C++，最快的方式，也用了输入输出绑定（好像叫这个？),同时对局部做了优化
```cpp
static auto x = [](){
    std::ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();



class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return dfsHeight(root) != -1;
    }
    
    int dfsHeight(TreeNode*root){
        if(!root)return 0;
        // 递归调用dfs
        int leftHeight = dfsHeight(root->left);
        // 如果有任意一个子树高度差大于1,返回-1;有任意一个不满足,也就是返回了-1,则直接返回-1;
        if(leftHeight == -1)return -1;
        // the same for the right side
        int rightHeight = dfsHeight(root->right);
        if(rightHeight == -1)return -1;
        
        //current part
        // 如果两个子树高度差大于1,返回-1
        int diff = std::abs(rightHeight-leftHeight);
        if(diff>1)return -1;
        // 返回当前子树的高度
        return std::max(leftHeight,rightHeight)+1;
        
    }
};
```
这个代码还有个神奇的C语言解法，通过两个函数的互相嵌套解决问题，逻辑有点混乱，但是运行很快。
```c
bool isBal(struct TreeNode* root, int* depth){
    if (!root) {
        *depth = 0;
        return true;
    }
    int leftdepth, rightdepth;
    if (isBal(root->left, &leftdepth) && isBal(root->right, &rightdepth)){
        if (leftdepth - rightdepth <= 1 && leftdepth - rightdepth >= -1){
            if (leftdepth > rightdepth)
                *depth = leftdepth + 1;
            else
                *depth = rightdepth + 1;
            //printf("%d, %d, %d\n", root->val, leftdepth, rightdepth);
            return true;
        }
    }
    *depth = 0;
    return false;
}

bool isBalanced(struct TreeNode* root) {
    int depth;
    return isBal(root, &depth);
}
```

