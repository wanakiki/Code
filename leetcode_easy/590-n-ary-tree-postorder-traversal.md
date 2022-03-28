## 776. N 叉树的后序遍历

2022-03-12 09:22:26

### 题目

给定一个 n 叉树的根节点 ``root`` ，返回其节点值的**后序遍历** 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 ``null`` 分隔（请参见示例）。



**示例 1：**

<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="height: 193px; width: 300px;" />

```
输入：root = [1,null,3,2,4,null,5,6]
输出：[5,6,3,2,4,1]
```

**示例 2：**

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="height: 269px; width: 296px;" />

```
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
```



**提示：**


- 节点总数在范围 ``[0, 10<sup>4</sup>]`` 内
- ``0 <= Node.val <= 10<sup>4</sup>``
- n 叉树的高度小于或等于 ``1000``




**进阶：** 递归法很简单，你可以使用迭代法完成此题吗?


[LeetCode链接](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)

### 思路及代码

后序遍历的顺序是左右根，使用根右左的顺序进行先序遍历后，将得到的数组反转即是后序遍历的结果。

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> res;
        stack<Node*> stk;
        stk.push(root);

        while(!stk.empty()){
            Node* cur = stk.top();
            stk.pop();
            if(cur == nullptr)  continue;

            res.push_back(cur->val);
            for(int i = 0; i < cur->children.size(); i++){
                stk.push(cur->children[i]);
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```