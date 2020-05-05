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

### 2020年5月5日

这个题目比较合理的解决办法是进行一次中序遍历，过程中记录当前节点的上一个节点，与之比较大小。中序遍历出的结果相当于整个二叉树垂直向下投影，若满足二叉搜索树的条件，遍历出的序列应该是单调递增的。

普通的先序遍历加边界代码↓，没有使用超过整形范围的数值，多添加了两个布尔值变量来判断左右是否为无穷大，代码写得有点繁琐可以进行简化。

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
    bool check(TreeNode* root, int left, int right, bool leftInf = true, bool rightInf = true){
        if(!root)   return true;
        if(leftInf && rightInf){
            return check(root->left, left, root->val, true, false) && check(root->right, root->val, right, false, true);
        }
        else if(leftInf){
            if(root->val >= right)  return false;
            return check(root->left, left, root->val, true, false) && check(root->right, root->val, right, false, false);
        }
        else if(rightInf){
            if(root->val <= left)   return false;
            return check(root->left, left, root->val, false, false) && check(root->right, root->val, right, false, true);
        }
        else{
            if(root->val <= left || root->val >= right)     return false;
            return check(root->left, left, root->val, false, false) && check(root->right, root->val, right, false, false);
        }
    }
    bool isValidBST(TreeNode* root) {
        return check(root, 0, 0);   
    }
};
```

中序遍历做法，注意传递的参数为pre的引用，这个值需要一直更改，另外需要注意pre更改的位置。

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
    bool check(TreeNode* root, TreeNode* &pre){
        if(root == NULL)     return true;

        // 如果左子树出现错误
        if(!check(root->left, pre)){
            return false;
        }

        if(pre!= NULL && pre->val >= root->val){
            return false;
        }

        pre = root;
        return check(root->right, pre);
    }
    bool isValidBST(TreeNode* root) {
        TreeNode* pre = NULL;
        return check(root, pre);
    }
};
```
