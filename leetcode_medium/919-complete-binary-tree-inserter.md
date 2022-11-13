## 955. 完全二叉树插入器

2022-07-25 09:44:52

### 题目

**完全二叉树** 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。

实现 ``CBTInserter`` 类:


- ``CBTInserter(TreeNode root)`` 使用头节点为 ``root`` 的给定树初始化该数据结构；
- ``CBTInserter.insert(int v)``  向树中插入一个值为 ``Node.val == val``的新节点 ``TreeNode``。使树保持完全二叉树的状态，**并返回插入节点** ``TreeNode`` **的父节点的值**；
- ``CBTInserter.get_root()`` 将返回树的头节点。







**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/08/03/lc-treeinsert.jpg" style="height: 143px; width: 500px;" />

```
输入
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
输出
[null, 1, 2, [1, 2, 3, 4]]

解释
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // 返回 1
cBTInserter.insert(4);  // 返回 2
cBTInserter.get_root(); // 返回 [1, 2, 3, 4]
```



**提示：**


- 树中节点数量范围为 ``[1, 1000]``
- ``0 <= Node.val <= 5000``
- ``root`` 是完全二叉树
- ``0 <= val <= 5000``
- 每个测试用例最多调用 ``insert`` 和 ``get_root`` 操作 ``10<sup>4</sup>`` 次



[LeetCode链接](https://leetcode-cn.com/problems/complete-binary-tree-inserter/)

### 思路及代码

直接按照层序遍历维护队列并编写插入节点代码。

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
class CBTInserter {
public:
    queue<TreeNode*> q;
    TreeNode* head;
    CBTInserter(TreeNode* root) {
        q.push(root);
        head = root;
        while(!q.empty()){
            TreeNode* cur_node = q.front();
            if(cur_node->left == nullptr){
                break;
            }
            else{
                q.push(cur_node->left);
            }

            if(cur_node->right == nullptr){
                break;
            }
            else{
                q.push(cur_node->right);
            }
            q.pop();
        }
    }
    
    int insert(int val) {
        TreeNode* cur_node = q.front();
        if(cur_node->left == nullptr){
            cur_node->left = new TreeNode(val);
            q.push(cur_node->left);
        }
        else{
            cur_node->right = new TreeNode(val);
            q.push(cur_node->right);
            q.pop();    // 只有右节点才能pop
        }

        
        return cur_node->val;
    }
    
    TreeNode* get_root() {
        return head;
    }
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter* obj = new CBTInserter(root);
 * int param_1 = obj->insert(val);
 * TreeNode* param_2 = obj->get_root();
 */
 ```