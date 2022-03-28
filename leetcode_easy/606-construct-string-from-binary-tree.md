## 606. 根据二叉树创建字符串

2022-03-19 09:39:32

### 题目

你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

**示例 1:**

```
输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

输出: "1(2(4))(3)"

解释: 原本将是&ldquo;1(2(4)())(3())&rdquo;，
在你省略所有不必要的空括号对之后，
它将是&ldquo;1(2(4))(3)&rdquo;。
```

**示例 2:**

```
输入: 二叉树: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

输出: "1(2()(4))(3)"

解释: 和第一个示例相似，
除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。
```


[LeetCode链接](https://leetcode-cn.com/problems/construct-string-from-binary-tree/)

### 思路及代码

采用递归方法进行前序遍历，需要注意的是为方便维护括号，在进行递归前需要对节点的值是否为空进行判断，左右节点按照不同的规则添加括号。

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
    string res;
    void helper(TreeNode* node){
        if(node == nullptr)  return ;
        res += to_string(node->val);
        
        // 为省略不必要的空括号 在左侧不为空或者右侧不为空时 均需要为左侧添加括号
        if(node->left || node->right){
            res += "(";
            helper(node->left);
            res += ")";
        }
            

        if(node->right){
           res += "(";
            helper(node->right);
            res += ")"; 
        }
        return ;
    }
    string tree2str(TreeNode* root) {
        res = "";
        if(root == nullptr) return res;
        helper(root);
        return res;
    }
};
```