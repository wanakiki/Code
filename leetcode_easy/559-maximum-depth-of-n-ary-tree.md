## 559. N叉树的最大深度

2020年10月12日

### 题目

给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 ``3叉树`` :

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;">


我们应返回其最大深度，3。

**说明:**


- 树的深度不会超过 ``1000``。
- 树的节点总不会超过 ``5000``。

### 思路及代码

进行深度优先搜索，过程中记录深度并返回。需要注意根节点为空时返回零。

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
    int maxDepth(Node* root) {
        if(root == NULL){
            return 0;
        }
        else{
            int tmp = 0;
            for(int i = 0; i < root->children.size(); i++){
                tmp = max(tmp, maxDepth(root->children[i]));
            }
            return tmp + 1;     // 附带自己
        }
    }
};
```