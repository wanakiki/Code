## 783. 二叉搜索树节点最小距离

2021-04-13 13:52:13

### 题目

给你一个二叉搜索树的根节点 ``root`` ，返回 **树中任意两不同节点值之间的最小差值** 。

**注意：** 本题与 530：<a href="https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/">https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/</a> 相同

 


**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" style="width: 292px; height: 301px;" />

```
输入：root = [4,2,6,1,3]
输出：1
```

**示例 2：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg" style="width: 282px; height: 301px;" />

```
输入：root = [1,0,48,null,null,12,49]
输出：1
```

 
**提示：**

- 树中节点数目在范围 ``[2, 100]`` 内
- ``0 <= Node.val <= 10<sup>5</sup>``


[LeetCode链接](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/)

### 思路及代码

中序遍历比较相邻值之间的差值。

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
    int helper(int& last, int& cur){
        if(last == -1){
            last = cur;
            return INT_MAX;
        }
        else{
            int tmp = cur - last;
            last = cur;
            return tmp;
        }
    }
    int minDiffInBST(TreeNode* root) {
        int last = -1;
        TreeNode* cur = root;
        int res = INT_MAX;
        stack<TreeNode*> stk;
        while(cur || !stk.empty()){
            while(cur){
                stk.push(cur);
                cur = cur->left;
            }

            if(!stk.empty()){
                cur = stk.top();
                stk.pop();
                res = min(helper(last, cur->val), res);
                cur = cur->right;
            }
        }
        return res;
    }
};
```