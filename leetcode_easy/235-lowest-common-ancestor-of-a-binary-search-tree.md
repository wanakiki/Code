## 235. 二叉搜索树的最近公共祖先

2020年9月22日

### 题目

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

<a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：&ldquo;对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。&rdquo;

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png" style="height: 190px; width: 200px;">

 

**示例 1:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
```

**示例 2:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
```

**说明:**

- 所有节点的值都是唯一的。
- p、q 为不同节点且均存在于给定的二叉搜索树中。


### 思路及代码

首先要清楚二叉搜索树的特点：左子树的所有值都小于当前节点，而右子树的所有值都大于当前节点。在此基础上，假设p结点的值小于q节点，当前节点为c，则可能出现的情况有：

|当下情况|下一步动作|
|:-:|:-:|
|p < c < q|返回c|
|p = c < q|返回c|
|p < c = q|返回c|
|p < q < c|遍历右子树|
|c < p < q|遍历左子树|

实现上面的逻辑即可解开本题。这里简单介绍一下前两种情况，由于我们是从根结点出发的，如果满足``p < c < q``则证明p和q位于两个子树当中，最近祖先为当前节点。在此基础之上，如果p或q变为了当下正在访问的节点，则二者一定在相同的子树上。

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
    TreeNode* helper(TreeNode* root, TreeNode* p, TreeNode* q){
        // 从上向下判断能保证当root为p或q时 pq在同一子树
        if(root == p || root == q){
            return root;
        }

        if(root->val > p->val && root->val < q->val){
            return root;
        }
        if(root->val > q->val){
            return helper(root->left, p, q);
        }
        if(root->val < p->val){
            return helper(root->right, p, q);
        }
        return root;
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // 确保p<q
        if(q->val < p->val){
            TreeNode* tmp = p;
            p = q;
            q = tmp;
        }

        return helper(root, p, q);
    }
};
```