## 449. 序列化和反序列化二叉搜索树

2022-05-11 20:08:03

### 题目

序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化**二叉搜索树** 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。     

**编码的字符串应尽可能紧凑。**



**示例 1：**

```
输入：root = [2,1,3]
输出：[2,1,3]
```

**示例 2：**

```
输入：root = []
输出：[]
```



**提示：**


- 树中节点数范围是 ``[0, 10<sup>4</sup>]``
- ``0 <= Node.val <= 10<sup>4</sup>``
- 题目数据 **保证** 输入的树是一棵二叉搜索树。



[LeetCode链接](https://leetcode-cn.com/problems/serialize-and-deserialize-bst/)

### 思路及代码

因为二叉搜索树的中序遍历满足递增排序，因此只要获得原始二叉树的前序或者后序遍历结果即可还原原始二叉树。

写反序列化的时候没怎么动脑子，代码有些繁琐。

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
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        TreeNode* cur;
        stack<TreeNode*> stk;
        stk.push(root);
        string res = "";
        while(!stk.empty()){
            cur = stk.top();
            stk.pop();

            if(cur){
                res += to_string(cur->val) + ",";

                stk.push(cur->right);
                stk.push(cur->left);
            }
        }
        
        // 不需要删除最后一个逗号便可直接返回 对反序列化无影响
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stack<TreeNode*> stk;
        TreeNode* cur = NULL;
        TreeNode* last_node = NULL;
        int last_val = -1;
        int left = 0, right = 0;
        TreeNode* res = NULL;

        while(right < data.size()){
            if(data[right] == ','){
                int val = stoi(data.substr(left, right - left));
                left = right + 1;

                if(last_val == -1){
                    cur = new TreeNode(val);
                    stk.push(cur);
                    res = cur;
                }
                else{
                    cur = new TreeNode(val);
                    if(val < last_val){
                        last_node->left = cur;
                        stk.push(cur);
                    }
                    else{
                        while(!stk.empty()){
                            TreeNode* tmp = stk.top();
                            if(val < tmp->val){
                                break;
                            }
                            last_node = tmp;
                            stk.pop();
                        }
                        last_node->right = cur;
                        stk.push(cur);
                    }
                }
                last_node = cur;
                last_val = val;
            }
            right++;
        }
        return  res;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec* ser = new Codec();
// Codec* deser = new Codec();
// string tree = ser->serialize(root);
// TreeNode* ans = deser->deserialize(tree);
// return ans;
```