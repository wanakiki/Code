## 116. Populating Next Right Pointers in Each Node
##### 2018-04-27 22:58:22
##### 在每个节点中填充下一个正确的指针
****
## 题目
Given a binary tree
```
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.  
将每个节点的``next``指向其右侧节点，如果右侧没有节点，则指针为NULL，并且开始时每个节点的``next``都为NULL。

Note:
- You may only use constant extra space.
- Recursive approach is fine, implicit stack space does not count as - extra space for this problem.
- You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).  

注意：
- 只能使用恒定的额外空间。
- 递归方法很好，隐式堆栈空间不算作此问题的额外空间。
- 你可以假设它是一棵完美的二叉树（即所有叶子都在同一水平上，并且每个父母有两个孩子）。




Example:

Given the following perfect binary tree,
```
     1
   /  \
  2    3
 / \  / \
4  5  6  7
```
After calling your function, the tree should look like:
```
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
```
## 分析
首先要注意的地方是二叉树初始状态下所有的next都为NULL，借助这个特点很容易就想到了递归的解决方式。
- 如果节点为NUll或者没有子树，则终止递归。
- 将根节点左支指向右支，如果根节点的next不为空，则将根节点右支的next指向根节点next指向节点的左支。
- 对根节点的左右两支进行递归。
## 示例代码
```cpp
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root || !root->left && !root->right )	//每个节点一定有两个子树
					return;
				root->left->next = root ->right;
				if(root -> next){
					root->left-next = root ->right;
				}
				connect(root ->left);
				connect(root ->right);
    }
};
```
