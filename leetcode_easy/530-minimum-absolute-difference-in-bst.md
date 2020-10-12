## 二叉搜索树的最小绝对差

2020年10月12日

### 题目

给定一个二叉搜索树的根节点 ``root``，返回树中任意两节点的差的最小值。

**示例：**

```
输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
```



**注意：**


- 二叉树的大小范围在 ``2`` 到 ``100``。
- 二叉树总是有效的，每个节点的值都是整数，且不重复。
- 本题与 530：<a href="https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/">https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/</a> 相同

### 思路及代码

二叉搜索树中序遍历结果是有序数列，可以先对搜索树进行中序遍历，再判断相邻节点之间的差值。

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
    int getMinimumDifference(TreeNode* root) {
        stack<TreeNode*> stk;
        vector<int> nums;
        TreeNode* node = root;
        while(node != NULL || !stk.empty()){
            while(node){
                stk.push(node);
                node = node->left;
            }
            if(!stk.empty()){
                node = stk.top();
                stk.pop();
                nums.push_back(node->val);
                node = node->right;
            }
        }
        int res = INT_MAX;
        for(int i = 1; i < nums.size(); i++){
            int tmp = abs(nums[i] - nums[i-1]);
            res = min(res, tmp);
        }
        return res;
    }
};
```

通过观察可以发现，因为只需要用到相邻两个节点的值，存放数据的数组实际上可以缩减为一个变量，于是有了下面的代码。

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
    int getMinimumDifference(TreeNode* root) {
        stack<TreeNode*> stk;
        TreeNode* node = root;
        int last;
        bool flag = false;
        int res = INT_MAX;

        while(node != NULL || !stk.empty()){
            while(node){
                stk.push(node);
                node = node->left;
            }
            if(!stk.empty()){
                node = stk.top();
                stk.pop();
                if(flag){
                    res = min(res, abs(node->val - last));
                }
                else{
                    flag = true;
                }
                last = node->val;
                node = node->right;
            }
        }
        
        return res;
    }
};
```