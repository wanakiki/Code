## 893. 二叉树中所有距离为 K 的结点

2021-07-28 11:18:07

### 题目

给定一个二叉树（具有根结点 ``root``）， 一个目标结点 ``target`` ，和一个整数值 ``K`` 。

返回到目标结点 ``target`` 距离为 ``K`` 的所有结点的值的列表。 答案可以以任何顺序返回。 


**示例 1：**

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1

注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。
```
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" style="height: 240px; width: 280px;">


**提示：**


- 给定的树是非空的。
- 树上的每个结点都具有唯一的值 ``0 <= node.val <= 500`` 。
- 目标结点 ``target`` 是树上的结点。
- ``0 <= K <= 1000``.



[LeetCode链接](https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/)

### 思路及代码

搜索+哈希表

题目中给出了目标节点的指针，针对于距离为k的目标节点的子节点，可以通过层序遍历得到。但是针对于满足距离条件的上级节点，由于节点设计中不包含指向父级的指针，所以不能直接向上访问得到。

想到这里，我最初的想法是通过深度优先搜索查找到目标节点，由于深度优先搜索的特性，此时栈中仍保留着多个上级节点的信息，可以以这部分节点为根再次展开层序遍历，得到想要的结果。

看起来可行，但是在实现后会发现存在节点信息丢失的问题。当k为1时，应保存target的父节点的数值，但此时栈中已经没有这部分数据。

简单看了一眼官方题解的标题，发现用到了哈希表，这时候不难联想到可以使用哈希表来存储每个节点的父节点信息，达到向上访问的目的。实现时不难发现，为了避免重复遍历数据，除了保存父节点信息之外，还应保存当前节点对应的左右子树情况，以便查找对侧子树的数据。

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
    // 从指定根节点向下搜索指定层数
    vector<int> helper(TreeNode* root, int k){
        if(root == NULL || k < 0)   return {}; 
        vector<int> res;
        queue<TreeNode*> q;
        q.push(root);

        int depth = 0;
        while(!q.empty()){
            int len = q.size();
            while(len--){
                auto cur = q.front();
                q.pop();

                if(depth == k){
                    res.push_back(cur->val);
                }
                else{
                    if(cur->left)   q.push(cur->left);
                    if(cur->right)  q.push(cur->right);
                }
            }
            depth++;
        }

        return res;
    }

    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        if(k == 0)  return {target->val};

        // 深度优先搜索到target 过程中是用哈希表保存不同节点的父节点 再反向查找
        vector<int> res = helper(target, k);
        unordered_map<TreeNode*, pair<TreeNode*, bool>> hash;

        stack<TreeNode*> stk;
        stk.push(root);

        while(!stk.empty()){
            auto cur = stk.top();
            stk.pop();

            // 查找到目标节点后开始反向遍历
            if(cur == target){
                break;
            }
            else{
                if(cur->left){
                    stk.push(cur->left);
                    hash[cur->left] = make_pair(cur, true);
                }
                if(cur->right){
                    stk.push(cur->right);
                    hash[cur->right] = make_pair(cur, false);
                }
            }
        }

        // 反向搜索过程
        auto cur = target;
        int len = 1;    // 代表节点与target的距离
        while(cur != root){
            auto p = hash[cur];
            cur = p.first;
            if(len == k){
                // 距离与k相等时只有一个节点
                res.push_back(cur->val);
            }
            else if(len < k){
                // 距离小于k时 查找另外方向的子树
                if(p.second){
                    vector<int> tmp = helper(cur->right, k - len - 1);      // 注意左右子树可能为空
                    res.insert(res.end(), tmp.begin(), tmp.end());
                }
                else{
                    vector<int> tmp = helper(cur->left, k - len - 1);
                    res.insert(res.end(), tmp.begin(), tmp.end());
                }
            }
            else{
                // 距离大于k后停止查找
                break;
            }
            len++;
        }
        return res;
    }
};
```