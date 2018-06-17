## 130. Surrounded Regions
##### 2018-05-20 14:30:56
##### 四面环绕 回溯
***
## 题目
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
```
X X X X
X O O X
X X O X
X O X X
```
After running your function, the board should be:
```
X X X X
X X X X
X X X X
X O X X
```
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

## 分析
一道回溯题目，思路不对会带来很大的麻烦...

因为做习惯了，首先的想法是写一个回溯让它把所有满足条件的O变成X，写了很长时间，但是发现条件越写越乱...但是到最后还是没写出来。
看了下别人的做法，发现先把不满足条件的O排除出去更简单：把和位于边缘的O相邻的O记做1，边缘部分排除完了之后遍历一次数组，把剩下的O变成X，把1还原。

尽管这样看起来很麻烦，但是写起来简单了很多。
## 代码
```cpp
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;
        int row = board.size(), col = board[0].size();
        for (int i = 0; i < row; ++i) {
            check(board, i, 0);            
            check(board, i, col - 1);       
        }
        for (int j = 1; j < col - 1; ++j) {
            check(board, 0, j);            
            check(board, row - 1, j);      
        }
        for (int i = 0; i < row; ++i)
            for (int j = 0; j < col; ++j)
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == '1') board[i][j] = 'O';
    }
    
    void check(vector<vector<char>>& board, int i, int j) {
        if (board[i][j] == 'O') {
            board[i][j] = '1';
            if (i > 1) check(board, i - 1, j);
            if (j > 1) check(board, i, j - 1);
            if (i + 1 < board.size()) check(board, i + 1, j);
            if (j + 1 < board[0].size()) check(board, i, j + 1);
        }
    }
};
```
