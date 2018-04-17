## 95. Unique Binary Search Trees II
##### 2018-04-17 17:55:00
##### 独特的二叉搜索树II
***
## 1.题目
>Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.  
给定n，存储值1 ... n的结构唯一的BST（二叉搜索树）有多少？

>For example,
Given n = 3, your program should return all 5 unique BST's shown below.  
例如，
假设n = 3，你的程序应该返回下面显示的所有5个独特的BST。  
```
1         3     3      2      1
 \       /     /      / \      \
  3     2     1      1   3      2
 /     /       \                 \
2     1         2                 3
```
## 2.分析
题目是二叉搜索树的进阶版，因为要求返回所有可能的情况，所以不能通过数学规律来解决。   

个人编程能力还不够，面对这种题目又感觉无从下手，看了别人的解决方式，发现并不是很难，只是这个递归的思路需要别人指导。  

尽管题目要求发生了变化，但是每个根节点的所有可能为其对应的左支与右支所有可能组合这个规律是不会变化的。  
为了知道这个根节点，我们需要求出其左支的所有可能与其右支的所有可能。分析可知，要求出一段数所有的可能，需要知道这段数的长度，以及开始数字大小，这样就满足了递归的实现规律。  
参考网上的代码，对于每个节点用递归求左右两支所有可能，之后在进行组合。  
## 3.代码
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
    vector<TreeNode*> generateTrees(int n) {
        if(n==0){
        vector<TreeNode*> res;
        return res;
        }
        return helper(1,n);
    }
    vector<TreeNode*> helper(int start,int sum){
        vector<TreeNode*> res;
        if(sum==0){
            res.push_back(NULL);
            return res;
        }
        if(sum==1){
            res.push_back(new TreeNode(start));
            return res;
        }
        for(int i=0;i<sum;i++){
            vector<TreeNode*> left=helper(start,i);
            vector<TreeNode*> right=helper(start+i+1,sum-1-i);
            for(int l=0;l<left.size();l++)      //长度不固定 使用size
                for(int r=0;r<right.size();r++){
                    TreeNode* root=new TreeNode(i+start);
                    root->left=left[l];
                    root->right=right[r];
                    res.push_back(root);
                }
        }
        return res;
    }
};
```
