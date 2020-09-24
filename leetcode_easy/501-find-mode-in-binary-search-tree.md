## 501. 二叉搜索树中的众数

2020年9月24日

### 题目

给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：


- 结点左子树中所含结点的值小于等于当前结点的值
- 结点右子树中所含结点的值大于等于当前结点的值
- 左子树和右子树都是二叉搜索树


例如：

给定 BST ``[1,null,2,2]``,

```
   1
    \
     2
    /
   2
```

``返回[2]``.

**提示**：如果众数超过1个，不需考虑输出顺序

**进阶：**你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

### 思路及代码

首先感觉这个题目不属于简单题目的范畴（当然也有可能是自己太菜了），在做这个题目的时候一直想广搜的时候怎么记录数据，但是发现不满足空间要求，看了一些别人的题解之后才意识到要用二叉树中序遍历的特点来做。

在中序遍历的前提下，记录上一个点的值及其出现的次数并于当前节点进行对比，之后更新结果数组。另外从官方题解学到可以专门写一个函数还更新结果数组，让程序看起来更清晰。剩下的就没有太多可以说的点了，具体看代码：

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
    int max_time = 0;
    vector<int> res;
    void update(int cur, int cur_count){
        if(cur_count < max_time){
            return ;
        }

        if(cur_count > max_time){
            max_time = cur_count;
            res.clear();
        }
        res.push_back(cur);
    }
    void helper(TreeNode* root, int& last, int& count){ // 遍历左子树时会改变last 和 count的值 需要传入引用
        if(!root){
            return ;
        }

        helper(root->left, last, count);
        if(last == root->val){
            count++;
        }
        else{
            last = root->val;
            count = 1;
        }
        update(last, count);
        helper(root->right, last, count);
    }
    vector<int> findMode(TreeNode* root) {
        int last = -1, count = 0;
        helper(root, last, count);
        return res;
    }
};
```

另外，无耻的哈希法应该也可以在规定时间内解出题目。