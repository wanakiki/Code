## 419. 甲板上的战舰

2021-12-18 10:32:51

### 题目

给你一个大小为 ``m x n`` 的矩阵 ``board`` 表示甲板，其中，每个单元格可以是一艘战舰 ``'X'`` 或者是一个空位 ``'.'`` ，返回在甲板 ``board`` 上放置的 **战舰** 的数量。

**战舰** 只能水平或者垂直放置在 ``board`` 上。换句话说，战舰只能按 ``1 x k``（``1`` 行，``k`` 列）或 ``k x 1``（``k`` 行，``1`` 列）的形状建造，其中 ``k`` 可以是任意大小。两艘战
舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。



**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/battelship-grid.jpg" style="width: 333px; height: 333px;" />
```
输入：board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
输出：2
```

**示例 2：**

```
输入：board = [["."]]
输出：0
```



**提示：**


- ``m == board.length``
- ``n == board[i].length``
- ``1 <= m, n <= 200``
- ``board[i][j]`` 是 ``'.'`` 或 ``'X'``




**进阶：**你可以实现一次扫描算法，并只使用** **``O(1)``** **额外空间，并且不修改 ``board`` 的值来解决这个问题吗？


[LeetCode链接](https://leetcode-cn.com/problems/battleships-in-a-board/)

### 思路及代码

利用战舰的分布只能在同一行或者在同一列的特点，首先检查第一行和第一列中的全部战舰，之后对剩余网格进行检查，如果发现当前位置是x且上方和左方均没有x则进行计数。

```cpp
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int res = 0;
        
        // 对第一行第一列进行检查
        for(int i = 0; i < board.size(); i++){
            if(board[i][0] == 'X' && (i == 0 || board[i-1][0] !='X'))   res++;
        }
        for(int j = 1; j < board[0].size(); j++){
            if(board[0][j] == 'X' && (board[0][j-1] != 'X'))    res++;
        }

        for(int i = 1; i < board.size(); i++){
            for(int j = 1; j < board[0].size(); j++){
                if(board[i][j] == 'X'){
                    bool check_row = (board[i-1][j] != 'X');
                    bool check_col = (board[i][j-1] != 'X');

                    // 两个条件均满足 计数
                    if(check_col && check_row)
                    res++;
                }
            }
        }
        return res;
    }
};
```