## 968. 监控二叉树

2020年9月22日

### 题目

给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视**其父对象、自身及其直接子对象。**

计算监控树的所有节点所需的最小摄像头数量。

 

**示例 1：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_01.png" style="height: 163px; width: 138px;">

```
输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。
```

**示例 2：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_02.png" style="height: 312px; width: 139px;">

```
输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
```



**提示：**


- 给定树的节点数的范围是 ``[1, 1000]``。
- 每个节点的值都是 0。


### 思路及代码

本题采用深度优先搜索加递归的做法，自下向上判断每个节点的情况。需要注意，每个节点的状态仅与其周围三个节点相关，且空节点的状态相当于被其更下一层的虚拟节点放置的相机监视。（因为如果把相机放在叶子节点，显然会造成大量浪费）

对树中结点的可能状态进行分析，不难发现有下面三种状态：

1. 放置相机
2. 无相机，且不被底层节点相机覆盖
3. 无相机，被底层节点覆盖

状态转移关系表如下：

|左孩子状态|右孩子状态|父节点状态（待推导）|简述|
|:-:|:-:|:-:|:-:|
|3|3|2|左右孩子都没有相机且被覆盖，当前节点应由上一层节点覆盖
|3|2|1|存在不被覆盖的左右孩子，必须在当层放相机
|3|1|3|左右孩子被覆盖且有一个孩子有相机，相当于本层被下层覆盖
|2|2|1|左右孩子都不被覆盖，在当层放置相机
|2|1|1|存在不被覆盖的左右孩子，必须在当层放置相机
|1|1|3|左右孩子都有相机，当层被下层覆盖

推出上面的状态转移关系表之后便可写出下面的代码，但需要注意的是根节点需要进行特殊判断。

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
    int res = 0;

    // 1 有相机，2 不被覆盖，3 无相机 被覆盖
    int dfs(TreeNode* root){
        if(root == NULL){
            return 3;   // 所有的空结点均为无相机且被覆盖的情况
        }
        int left = dfs(root->left);
        int right = dfs(root->right);

        if(left == 2 || right == 2){
            res ++;
            return 1;
        }
        else if(left == 1 || right == 1){
            return 3;
        }
        else{
            return 2;
        }
    }
    int minCameraCover(TreeNode* root) {
        int tmp = dfs(root);
        // 如果最后根节点不被覆盖需要多一个相机
        if(tmp == 2){
            res ++;
        }
        return res;
    }
};
```



