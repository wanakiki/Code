## 129. Sum Root to Leaf Numbers
##### 2018-04-30 23:13:20
##### 根到叶的总和
*****
## 题目
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

给定一个只包含0-9数字的二叉树，每个根到叶子路径可以代表一个数字。  一个例子是代表数字123的根到叶路径1-> 2-> 3。
查找所有根到叶数量的总和。
注意：叶子是没有孩子的节点。

Example:
```
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```
Example 2:
```
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```
## 分析
具体的问题两个示例已经说得很清楚了，稍微需要注意到的地方是数字只有0-9，如果考虑负数又会稍微麻烦一些。

采用了相对简单的方法，设置一个变量sum存储总和，将其引用传入函数，函数拥有一个变量用来计算当前的总和（不是用于返回的总和），从根节点开始判断，为空则直接返回，遇到叶子则对sum进行操作，遇不到则对当前对应的左右两树进行判断，直到结束。
## 示例代码
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
    int sumNumbers(TreeNode* root) {
        int sum=0;
        helper(sum,root,0);
        return sum;
    }
    void helper(int & sum,TreeNode * root,int now){
        if(!root)
            return ;
        if(!root->left && !root->right){
            sum+=(root->val + now*10);
            return ;
        }
            helper(sum,root->left,now*10+root->val);
            helper(sum,root->right,now*10+root->val);
    }
};
```
代码很简单，还有一种更快的解决方式是设置sum为全局变量，但是个人觉得实际解决问题不方便应用，但是仔细考虑一下因为这个函数处在一个类内，完全可以将sum设置为类的成员变量加快解题速度。
