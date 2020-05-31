## Symmetric Tree
##### 2018年02月12日21:39:49
##### 二叉树（判断是否对称）
***
### 题目
>Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).  
给定一个二叉树，检查它是否是它自己的镜像（即，围绕它的中心对称）。
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
例如，这个二叉树[1,2,2,3,4,4,3]是对称的：
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
>Note:
Bonus points if you could solve it both recursively and iteratively.  
奖励点数，如果你可以递归地和迭代地解决它。

### 分析
刚刚做过了判断两个二叉树是否相同的题目，所以直接想到了写一个反转二叉树的函数然后将这两个二叉树直接拿原来的函数进行判断。  
反转二叉树的函数很容易实现，只要将新节点的右支指向左支，新节点左支指向右支。具体看代码

### 代码
```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
//反转函数
struct TreeNode* reverse(struct TreeNode * rot){
    int temp;
    if(rot==NULL)
        return NULL;
    temp=rot->val;
    struct TreeNode* root=(struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val=temp;
    root->left=reverse(rot->right);
    root->right=reverse(rot->left);
    return root;
}

//判断是否相同函数
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if(p==NULL && q==NULL)
        return true;
    if((p!=NULL&&q==NULL) || (q!= NULL&&p==NULL))
        return false;
    if(p->val==q->val){
        if(!isSameTree(q->left,p->left))
            return false;
        if(!isSameTree(q->right,p->right))
            return false;
    }
    else
        return false;
    return true;
}

//判断是否对称函数
bool isSymmetric(struct TreeNode* root) {
    struct TreeNode* root2=reverse(root);
    return isSameTree(root,root2);
}
```

### 2020年5月31日

C++做法，直接以根节点的两个子树进行搜索，对比镜像位置节点的值是否相同。需要注意左右两个子树的入栈方向不同。

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
    bool isSymmetric(TreeNode* root) {
        if(!root)   return true;
        stack<TreeNode*> stk1, stk2;

        stk1.push(root->left);
        stk2.push(root->right);

        while(!stk1.empty() && !stk2.empty()){
            int flag = 0;
            if(stk1.top() == NULL){
                stk1.pop();
                flag++;
            }
            if(stk2.top() == NULL){
                stk2.pop();
                flag++;
            }
            if(flag == 2){
                continue;
            }
            if(flag == 1){
                break;
            }

            if(stk1.top()->val == stk2.top()->val){
                TreeNode* cur_left = stk1.top();
                TreeNode* cur_right = stk2.top();
                stk1.pop();
                stk2.pop();

                stk1.push(cur_left->right);
                stk1.push(cur_left->left);
                stk2.push(cur_right->left);
                stk2.push(cur_right->right);
            }
            else{
                return false;
            }
        }

        return stk1.empty() && stk2.empty();
    }
};
```