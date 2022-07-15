## 558. 四叉树交集

2022-07-15 09:43:22

### 题目

二进制矩阵中的所有元素不是 **0** 就是 **1 **。

给你两个四叉树，``quadTree1`` 和 ``quadTree2``。其中 ``quadTree1`` 表示一个 ``n * n`` 二进制矩阵，而 ``quadTree2`` 表示另一个 ``n * n`` 二进制矩阵。

请你返回一个表示 ``n * n`` 二进制矩阵的四叉树，它是 ``quadTree1`` 和 ``quadTree2`` 所表示的两个二进制矩阵进行 **按位逻辑或运算** 的结果。

注意，当 ``isLeaf`` 为 **False **时，你可以把 **True** 或者 **False** 赋值给节点，两种值都会被判题机制 **接受** 。

四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：


- ``val``：储存叶子结点所代表的区域的值。1 对应 **True**，0 对应 **False**；
- ``isLeaf``: 当这个节点是一个叶子结点时为 **True**，如果它有 4 个子节点则为 **False** 。


```
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```

我们可以按以下步骤为二维区域构建四叉树：


- 如果当前网格的值相同（即，全为 ``0`` 或者全为 ``1``），将 ``isLeaf`` 设为 True ，将 ``val`` 设为网格相应的值，并将四个子节点都设为 Null 然后停止。
- 如果当前网格的值不同，将 ``isLeaf`` 设为 False， 将 ``val`` 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
- 使用适当的子网格递归每个子节点。


<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/new_top.png" style="height: 181px; width: 777px;" />

如果你想了解更多关于四叉树的内容，可以参考 <a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a> 。

**四叉树格式：**

输出为使用层序遍历后四叉树的序列化形式，其中 ``null`` 表示路径终止符，其下面不存在节点。

它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 ``[isLeaf, val]`` 。

如果 ``isLeaf`` 或者 ``val`` 的值为 True ，则表示它在列表 ``[isLeaf, val]`` 中的值为 **1** ；如果 ``isLeaf`` 或者 ``val`` 的值为 False ，则表示值为 **0 **。

 

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/qt1.png" style="height: 196px; width: 550px;" /> <img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/qt2.png" style="height: 278px; width: 550px;" />

```
输入：quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
, quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
输出：[[0,0],[1,1],[1,1],[1,1],[1,0]]
解释：quadTree1 和 quadTree2 如上所示。由四叉树所表示的二进制矩阵也已经给出。
如果我们对这两个矩阵进行按位逻辑或运算，则可以得到下面的二进制矩阵，由一个作为结果的四叉树表示。
注意，我们展示的二进制矩阵仅仅是为了更好地说明题意，你无需构造二进制矩阵来获得结果四叉树。
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/qtr.png" style="height: 222px; width: 777px;" />
```

**示例 2：**

```
输入：quadTree1 = [[1,0]]
, quadTree2 = [[1,0]]
输出：[[1,0]]
解释：两个数所表示的矩阵大小都为 1*1，值全为 0
结果矩阵大小为 1*1，值全为 0 。
```

**示例 3：**

```
输入：quadTree1 = [[0,0],[1,0],[1,0],[1,1],[1,1]]
, quadTree2 = [[0,0],[1,1],[1,1],[1,0],[1,1]]
输出：[[1,1]]
```

**示例 4：**

```
输入：quadTree1 = [[0,0],[1,1],[1,0],[1,1],[1,1]]
, quadTree2 = [[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]
输出：[[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]
```

**示例 5：**

```

输入：quadTree1 = [[0,1],[1,0],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
, quadTree2 = [[0,1],[0,1],[1,0],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1]]
输出：[[0,0],[0,1],[0,1],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1],[1,0],[1,0],[1,1],[1,1]]
```

 

**提示：**


- ``quadTree1`` 和 ``quadTree2`` 都是符合题目要求的四叉树，每个都代表一个 ``n * n`` 的矩阵。
- ``n == 2^x`` ，其中 ``0 <= x <= 9``.



[LeetCode链接](https://leetcode-cn.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/)

### 思路及代码

采用递归方式对两个四叉树进行对等位置遍历，返回结点指针。为保证结果正确，在真正返回节点指针之前，需要判断节点是否满足合并为叶子节点的条件。

```cpp
/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    Node* helper(Node* tree1, Node* tree2){
        if(tree1 == NULL && tree2 == NULL)  return NULL;
        Node * curNode = new Node();

        if(tree1->isLeaf && tree2->isLeaf){
            curNode->isLeaf = true;
            curNode->val = tree1->val | tree2->val;
            return curNode;
        }
        else if(tree1->isLeaf == false && tree2->isLeaf == false){
            curNode->topLeft = helper(tree1->topLeft, tree2->topLeft);
            curNode->topRight = helper(tree1->topRight, tree2->topRight);
            curNode->bottomLeft = helper(tree1->bottomLeft, tree2->bottomLeft);
            curNode->bottomRight = helper(tree1->bottomRight, tree2->bottomRight);

            // 如果子节点都是叶子节点且值相等
            if(
                curNode->topLeft->isLeaf &&
                curNode->topRight->isLeaf &&
                curNode->bottomLeft->isLeaf &&
                curNode->bottomRight->isLeaf &&
                curNode->topLeft->val == curNode->topRight->val &&
                curNode->topRight->val == curNode->bottomLeft->val &&
                curNode->bottomLeft->val == curNode->bottomRight->val){
                    curNode->isLeaf = true;
                    curNode->val = curNode->topLeft->val;

                    delete(curNode->topLeft);
                    delete(curNode->topRight);
                    delete(curNode->bottomLeft);
                    delete(curNode->bottomRight);

                    curNode->topLeft = curNode->topRight = curNode->bottomLeft = curNode->bottomRight = NULL;
                }
            return curNode;
        }
        else{
            // 如果有一个为叶子节点 则叶子节点不需要继续访问孩子
            Node* tmp1;
            Node* tmp2;

            if(tree1->isLeaf){
                tmp1 = tree1;
                tmp2 = tree2;
            }
            else{
                tmp1 = tree2;
                tmp2 = tree1;
            }

            // 开始遍历
            curNode->topLeft = helper(tmp1, tmp2->topLeft);
            curNode->topRight = helper(tmp1, tmp2->topRight);
            curNode->bottomLeft = helper(tmp1, tmp2->bottomLeft);
            curNode->bottomRight = helper(tmp1, tmp2->bottomRight);

            // 如果子节点都是叶子节点且值相等
            if(
                curNode->topLeft->isLeaf &&
                curNode->topRight->isLeaf &&
                curNode->bottomLeft->isLeaf &&
                curNode->bottomRight->isLeaf &&
                curNode->topLeft->val == curNode->topRight->val &&
                curNode->topRight->val == curNode->bottomLeft->val &&
                curNode->bottomLeft->val == curNode->bottomRight->val){
                    curNode->isLeaf = true;
                    curNode->val = curNode->topLeft->val;

                    delete(curNode->topLeft);
                    delete(curNode->topRight);
                    delete(curNode->bottomLeft);
                    delete(curNode->bottomRight);

                    curNode->topLeft = curNode->topRight = curNode->bottomLeft = curNode->bottomRight = NULL;
                }
                
            return curNode;
        }
    }
    Node* intersect(Node* quadTree1, Node* quadTree2) {
        return helper(quadTree1, quadTree2);
    }
};
```