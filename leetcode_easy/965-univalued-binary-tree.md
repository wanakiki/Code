## 965. 单值二叉树

2022-05-24 11:32:40

### 题目

如果二叉树每个节点都具有相同的值，那么该二叉树就是<em>单值</em>二叉树。

只有给定的树是单值二叉树时，才返回 ``true``；否则返回 ``false``。



**示例 1：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50104-pm.png" style="height: 159px; width: 200px;">

```
输入：[1,1,1,1,1,null,1]
输出：true
```

**示例 2：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50050-pm.png" style="height: 158px; width: 200px;">

```
输入：[2,2,2,5,2]
输出：false
```



**提示：**


- 给定树的节点数范围是 ``[1, 100]``。
- 每个节点的值都是整数，范围为 ``[0, 99]`` 。



[LeetCode链接](https://leetcode-cn.com/problems/univalued-binary-tree/)

### 思路及代码

深度优先搜索，判断是否有第二个数值出现。

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        int last = -1;
        stack<TreeNode*> stk;
        stk.push(root);
        while(!stk.empty()){
            auto cur = stk.top();
            stk.pop();
            if(!cur)    continue;

            if(last == -1){
                last = cur->val;
            }
            else{
                if(last != cur->val)    return false;
            }

            stk.push(cur->left);
            stk.push(cur->right);
        }
        return true;
    }
};
```