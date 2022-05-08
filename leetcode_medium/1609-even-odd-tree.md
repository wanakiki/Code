## 1609. 奇偶树

2021-12-25 09:45:00

### 题目

如果一棵二叉树满足下述几个条件，则可以称为 **奇偶树** ：


- 二叉树根节点所在层下标为 ``0`` ，根的子节点所在层下标为 ``1`` ，根的孙节点所在层下标为 ``2`` ，依此类推。
- **偶数下标** 层上的所有节点的值都是 **奇** 整数，从左到右按顺序 **严格递增**
- **奇数下标** 层上的所有节点的值都是 **偶** 整数，从左到右按顺序 **严格递减**


给你二叉树的根节点，如果二叉树为 **奇偶树 **，则返回 ``true`` ，否则返回 ``false`` 。

 

**示例 1：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/sample_1_1966.png" style="height: 229px; width: 362px;" />**

```
输入：root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
输出：true
解释：每一层的节点值分别是：
0 层：[1]
1 层：[10,4]
2 层：[3,7,9]
3 层：[12,8,6,2]
由于 0 层和 2 层上的节点值都是奇数且严格递增，而 1 层和 3 层上的节点值都是偶数且严格递减，因此这是一棵奇偶树。
```

**示例 2：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/sample_2_1966.png" style="height: 167px; width: 363px;" />**

```
输入：root = [5,4,2,3,3,7]
输出：false
解释：每一层的节点值分别是：
0 层：[5]
1 层：[4,2]
2 层：[3,3,7]
2 层上的节点值不满足严格递增的条件，所以这不是一棵奇偶树。
```

**示例 3：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/sample_1_333_1966.png" style="height: 167px; width: 363px;" />

```
输入：root = [5,9,1,3,5,7]
输出：false
解释：1 层上的节点值应为偶数。
```

**示例 4：**

```
输入：root = [1]
输出：true
```

**示例 5：**

```
输入：root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
输出：true
```

 

**提示：**


- 树中节点数在范围 ``[1, 10<sup>5</sup>]`` 内
- ``1 <= Node.val <= 10<sup>6</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/even-odd-tree/)

### 思路及代码

按层遍历，并根据每层对应特点进行判断。

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
    bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);

        int count = 1;
        int level = 0;
        while(!q.empty()){
            int next_count = 0;
            int last_val = -1;

            while(count--){
                auto cur_node = q.front();
                q.pop();
                if(cur_node == nullptr) continue;

                int cur_val = cur_node->val;
                if(last_val == -1){
                    last_val = cur_val;

                    // 需要判断当前数字奇偶性是否正确
                    if(level & 1 && cur_val % 2 == 1)   return false;
                    if(!(level & 1) && cur_val % 2 == 0)    return false;
                }
                else{
                    // 奇数
                    if(level & 1){
                        if(cur_val % 2 == 1 || cur_val >= last_val) return false;
                        last_val = cur_val;
                    }
                    else{
                        if(cur_val % 2 == 0 || cur_val <= last_val) return false;
                        last_val = cur_val;
                    }
                }

                // 子节点入队
                q.push(cur_node->left);
                q.push(cur_node->right);
                next_count += 2;
            }

            count = next_count;
            level += 1;
        }

        return true;
    }
};
```