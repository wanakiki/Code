## 653. 两数之和 IV - 输入 BST

2022-03-21 08:56:16

### 题目

给定一个二叉搜索树 ``root`` 和一个目标结果 ``k``，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 ``true``。



**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg" style="height: 229px; width: 400px;" />
```
输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
```

**示例 2：**
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg" style="height: 229px; width: 400px;" />
```
输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
```



**提示:**


- 二叉树的节点个数的范围是  ``[1, 10<sup>4</sup>]``.
- ``-10<sup>4</sup> <= Node.val <= 10<sup>4</sup>``
- ``root`` 为二叉搜索树
- ``-10<sup>5</sup> <= k <= 10<sup>5</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/)

### 思路及代码

深度优先搜索搭配哈希表，不确定是否有通过利用 BST 特性对搜索进行加速的方法。

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
    bool findTarget(TreeNode* root, int k) {
        unordered_map<int, int> hash;
        stack<TreeNode*> stk;
        stk.push(root);

        while(!stk.empty()){
            auto cur = stk.top();
            stk.pop();

            if(cur){
                int val = cur->val;
                if(hash.find(k - val) != hash.end()){
                    return true;
                }
                hash[val] = 1;
                stk.push(cur->left);
                stk.push(cur->right);
            }
        }
        return false;
    }
};
```