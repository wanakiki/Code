## 117. Populating Next Right Pointers in Each Node II
##### 2018-04-28 18:39:35
##### 在每个节点中填充下一个正确的指针2
***
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

Note:
- You may only use constant extra space.
- Recursive approach is fine, implicit stack space does not count as extra space for this problem.

填充每个下一个指针指向其下一个右侧节点。如果没有下一个正确的节点，则应该将下一个指针设置为NULL。
最初，所有下一个指针都设置为NULL。

注意：
只能使用恒定的额外空间。
递归方法很好，隐式堆栈空间不算作此问题的额外空间。

Example:

Given the following binary tree,
```
     1
   /  \
  2    3
 / \    \
4   5    7
```
After calling your function, the tree should look like:
```
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
```
## 分析
和116题一样的解决方式，不过这次并不保证为满二叉树的情况。
对于左节点，先查找同根的右节点，再查找根节点next指向的节点，判断是否有右子树和左子树，如果有则将最初左节点的next指向该节点，若无则一直向右查找到根的next节点的两个子树为空停止；对于右节点，大体步骤相同，只是少了最初的一个判断。

之所以要这么麻烦，是为了避免中间相隔很多个节点的情况，像这样：
``{1,2,3,4,5,#,6,7,#,#,#,#,8}``   
输出应为：``{1,#,2,3,#,4,5,6,#,7,8,#}``

为了方便查找，我另外定义了一个函数，返回当前next应该指向的值。

**注意，由于这种做法是一层一层解决的，为了避免左支处理到最后右支还没有处理而无法查找的情况，应从右支开始处理。**

## 代码
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
        if(!root || !root->left && !root->right)
                return;
         if(root -> right){
                root->right->next = get(2,root);
                connect(root ->right);
        }
        if(root -> left){
                root->left->next = get(1,root);
                connect(root -> left);
        }

    }

    TreeLinkNode * get(int case_,TreeLinkNode *root){
            if(case_==1){
                    if(root->right)
                            return root->right;
            }
            while(root->next){
                if(!root->next->left && !root->next->right){
                    root=root->next;
                    continue;
                }
                    if(root->next->left)
                            return root->next->left;
                    if(root->next->right)
                            return root->next->right;
            }
            return NULL;
    }
};
```
尽管看起来有些小麻烦，不过运行速度还是比较快的，90%

这是最快的解决方式：
```cpp
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
static int x = [](){
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (!root)  return ;
        while(root){
            TreeLinkNode* cur = root;
            TreeLinkNode* left = nullptr;
            root = nullptr;
            while(cur){
                if (cur->left){
                    if (!left) {root = left = cur->left;}
                    else   left = left->next = cur->left;
                }
                if (cur->right){
                    if (!left) {root = left= cur->right;}
                    else   left = left->next = cur->right;
                }
                cur = cur->next;
            }
        }
    }
};
```
还有些现在不懂的写法
