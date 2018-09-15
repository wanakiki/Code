# 289. Game of Life

2018年9月15日

## 题目

According to the [Wikipedia's article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight [neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood) (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

```no
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
```

Follow up:

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

## 分析

题目大意很清楚，每个位置都有可能诞生出细胞，要求统计每个位置周围的活细胞数，按照给定的规则统一进行更新。因为要求不使用额外的空间，我的做法是遍历数组，如果该位置有细胞就给他的每个邻居都加二。因为初始只有0和1两种情况，所以加2之后我们通过对2取余和除2两种运算可以得出该位置的初始值，以及周围的活细胞数。统计结束之后，再遍历一次数组进行更新。

但是因为邻居是周围的八个位置，判断某个位置是否有值我处理的比较麻烦。

## 示例代码

C++

```cpp
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        if(!m)
            return ;
        int n = board[0].size();
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] % 2){
                    if(i)
                        board[i - 1][j] += 2;
                    if(j)
                        board[i][j - 1] += 2;
                    if(i + 1 < m)
                        board[i + 1][j] += 2;
                    if(j + 1 < n)
                        board[i][j + 1] += 2;
                    if(i && j)
                        board[i - 1][j - 1] += 2;
                    if(i && j + 1 < n)
                        board[i - 1][j + 1] += 2;
                    if(j && i + 1 < m)
                        board[i + 1][j - 1] += 2;
                    if(i + 1 < m && j + 1 < n)
                        board[i + 1][j + 1] += 2;
                }
            }
        }
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] % 2){
                    if(board[i][j] / 2 < 2 || board[i][j] / 2 > 3)
                        board[i][j] = 0;
                    else
                        board[i][j] = 1;
                }
                else{
                    if(board[i][j] / 2 == 3)
                        board[i][j] = 1;
                    else
                        board[i][j] = 0;
                }
            }
        }
        return ;
    }
};
```