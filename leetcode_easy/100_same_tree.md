## Same Tree
##### 2018年02月12日20:35:28
##### 二叉树遍历
***
### 题目
>Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.  
 给定两个二叉树，写一个函数来检查它们是否相同。 如果两棵树在结构上相同并且节点具有相同的值，则认为它们是相同的。

### 分析
第一次做二叉树的题目，花了点时间理解了下二叉树的运作模式，根据二叉树的遍历方法很容易写出来了这道题目。  
不过代码写的有点复杂。
### 代码
```c
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
```



