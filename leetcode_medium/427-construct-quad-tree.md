## 772. 建立四叉树

2022-04-29 19:38:59

### 题目

给你一个 ``n * n`` 矩阵 ``grid`` ，矩阵由若干 ``0`` 和 ``1`` 组成。请你用四叉树表示该矩阵 ``grid`` 。

你需要返回能表示矩阵的 四叉树 的根结点。

注意，当 ``isLeaf`` 为 **False**时，你可以把 **True** 或者 **False** 赋值给节点，两种值都会被判题机制 **接受** 。

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


<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/new_top.png" style="height: 181px; width: 777px;">

如果你想了解更多关于四叉树的内容，可以参考 <a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a> 。

**四叉树格式：**

输出为使用层序遍历后四叉树的序列化形式，其中 ``null`` 表示路径终止符，其下面不存在节点。

它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 ``[isLeaf, val]`` 。

如果 ``isLeaf`` 或者 ``val`` 的值为 True ，则表示它在列表 ``[isLeaf, val]`` 中的值为 **1** ；如果 ``isLeaf`` 或者 ``val`` 的值为 False ，则表示值为 **0**。



**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/grid1.png" style="height: 99px; width: 777px;">

```
输入：grid = [[0,1],[1,0]]
输出：[[0,1],[1,0],[1,1],[1,1],[1,0]]
解释：此示例的解释如下：
请注意，在下面四叉树的图示中，0 表示 false，1 表示 True 。
```
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e1tree.png" style="height: 186px; width: 777px;">

**示例 2：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e2mat.png" style="height: 343px; width: 777px;">

```
输入：grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
输出：[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
解释：网格中的所有值都不相同。我们将网格划分为四个子网格。
topLeft，bottomLeft 和 bottomRight 均具有相同的值。
topRight 具有不同的值，因此我们将其再分为 4 个子网格，这样每个子网格都具有相同的值。
解释如下图所示：
```
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e2tree.png" style="height: 328px; width: 777px;">

**示例 3：**

```
输入：grid = [[1,1],[1,1]]
输出：[[1,1]]
```

**示例 4：**

```
输入：grid = [[0]]
输出：[[1,0]]
```

**示例 5：**

```
输入：grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
输出：[[0,1],[1,1],[1,0],[1,0],[1,1]]
```



**提示：**


- ``n == grid.length == grid[i].length``
- ``n == 2^x`` 其中 ``0 <= x <= 6``



[LeetCode链接](https://leetcode-cn.com/problems/construct-quad-tree/)

### 思路及代码

采用递归方式建立，思路比较清晰，对于四个子节点能否合并为新的叶子节点的条件是：子节点均为叶子节点且子节点的值相同。

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
    Node* getNode(vector<vector<int>>& grid, int x, int y, int size){
        if(size == 1){
            return new Node(grid[x][y], true);
        }
        else{
            vector<Node* > res;
            int len = size / 2;
            res.push_back(getNode(grid, x, y, len));
            res.push_back(getNode(grid, x, y + len, len));
            res.push_back(getNode(grid, x + len, y, len));
            res.push_back(getNode(grid, x + len, y + len, len));


            // 只有四个底层都是叶子并且值相等才能抽象为新的叶子
            bool flag = true;
            for(int i = 0; i < 4; i++){
                if(res[i]->isLeaf == false) flag = false;
                if(i != 0){
                    if(res[i]->val != res[i-1]->val)    flag = false;
                }
                
                if(flag == false)   break;
            }

            if(flag){
                return new Node(res[0]->val, true);
            }
            else{
                return new Node(res[0]->val, false, res[0], res[1], res[2], res[3]);
            }
        }
    }
    Node* construct(vector<vector<int>>& grid) {
        return getNode(grid, 0, 0, grid.size());
    }
};
```

上述递归算法实现复杂度较高，可以使用前缀和辅助建树。由于只有零一两种数值，可以通过前缀和得到当前区域内零和一的个数，如果满足全为零或者全为一则不需要进一步探索。使用前缀和对不需要深入访问的区域进行了剪枝。

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
    bool checkSize(vector<vector<int>>& grid, int x, int y, int size){
        int num = grid[x + size - 1][y + size - 1];
        if(x > 0)   num -= grid[x - 1][y + size - 1];
        if(y > 0)   num -= grid[x + size - 1][y - 1];
        if(x > 0 && y > 0)  num += grid[x-1][y-1];

        return (num == 0) || (num == size * size);
    }
    Node* getNode(vector<vector<int>>& o_grid, vector<vector<int>>& grid, int x, int y, int size){
        if(size == 1){
            return new Node(o_grid[x][y], true);
        }
        else{
            vector<Node* > res;
            int len = size / 2;
            for(int i = 0; i < 2; i++){
                for(int j = 0; j< 2; j++){
                    int curx = x + i * len;
                    int cury = y + j * len;
                    if(checkSize(grid, curx, cury, len)){
                        res.push_back(new Node(o_grid[curx][cury], true));
                    }
                    else{
                        res.push_back(getNode(o_grid, grid, curx, cury, len));
                    }
                }
            }

            // 只有四个底层都是叶子并且值相等才能抽象为新的叶子
            bool flag = true;
            for(int i = 0; i < 4; i++){
                if(res[i]->isLeaf == false) flag = false;
                if(i != 0){
                    if(res[i]->val != res[i-1]->val)    flag = false;
                }
                
                if(flag == false)   break;
            }

            if(flag){
                return new Node(res[0]->val, true);
            }
            else{
                return new Node(res[0]->val, false, res[0], res[1], res[2], res[3]);
            }
        }
    }

    void helper(vector<vector<int>>& grid){
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                cout << grid[i][j] << ' ';
            }
            cout << endl;
        }
        cout << "=====" << endl;
    }
    Node* construct(vector<vector<int>>& grid) {
        vector<vector<int>> o_grid = grid;
        int len = grid.size();
        for(int i = 1; i < len; i++){
            grid[0][i] += grid[0][i-1];
            grid[i][0] += grid[i-1][0];
        }
        for(int i = 1; i < len; i++){
            for(int j = 1; j < len; j++){
                grid[i][j] += grid[i][j-1] + grid[i-1][j];
                grid[i][j] -= grid[i-1][j-1];
            }
        }
        // helper(o_grid);
        // helper(grid);
        return getNode(o_grid, grid, 0, 0, grid.size());
    }
};
```