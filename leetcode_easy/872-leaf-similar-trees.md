## 904. 叶子相似的树

2020-12-13 20:05:47

### 题目

请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个*叶值序列</em> 。

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png" style="height: 240px; width: 300px;">

举个例子，如上图所示，给定一棵叶值序列为 ``(6, 7, 4, 9, 8)`` 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是*叶相似*的。

如果给定的两个头结点分别为 ``root1`` 和 ``root2`` 的树是叶相似的，则返回 ``true``；否则返回 ``false`` 。

 

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg" style="height: 297px; width: 750px;">

```
输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
输出：true
```

**示例 2：**

```
输入：root1 = [1], root2 = [1]
输出：true
```

**示例 3：**

```
输入：root1 = [1], root2 = [2]
输出：false
```

**示例 4：**

```
输入：root1 = [1,2], root2 = [2,2]
输出：true
```

**示例 5：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg" style="height: 165px; width: 450px;">

```
输入：root1 = [1,2,3], root2 = [1,3,2]
输出：false
```

 

**提示：**


- 给定的两棵树可能会有 ``1`` 到 ``200`` 个结点。
- 给定的两棵树上的值介于 ``0`` 到 ``200`` 之间。



### 思路及代码

遍历获取叶节点，之后进行比较。

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
    vector<int> helper(TreeNode* root){
        if(root == nullptr){
            return {};
        }
        vector<int> res;
        stack<TreeNode* > stk;
        stk.push(root);
        while(!stk.empty()){
            TreeNode* cur = stk.top();
            stk.pop();
            if(cur->left == nullptr && cur->right == nullptr){
                res.push_back(cur->val);
                continue;
            }
            if(cur->left){
                stk.push(cur->left);
            }
            if(cur->right){
                stk.push(cur->right);
            }
        }
        return res;
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> nums1(helper(root1));
        vector<int> nums2(helper(root2));
        return nums1 == nums2;
    }
};
```