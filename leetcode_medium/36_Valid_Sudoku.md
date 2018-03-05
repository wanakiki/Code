## 36. Valid Sudoku
##### 2018-03-05 
##### 新想法
***
## 1.题目
>Determine if a Sudoku is valid, according to: [Sudoku Puzzles - The Rules](http://sudoku.com.au/TheRules.aspx).  
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.    
根据：Sudoku Puzzles - 规则确定一个数独是否有效。 数独板可以部分填充，空单元格填充字符'。'。'

## 2.分析
判断一个数独是否有效，数组可以不被填满，空白位置填充'.'。数独一定是9*9规格的，C语言中函数的传参并不必要。  
开始的想法就是直接遍历全部，分别看行、列、独立的九个格，用值全为零的数组判断。但是因为进行了三次遍历，超时。  

发现了一个更有效的解法，只用了两个for循环进行遍历，定义了三个数组同时判断，很简单但是自己很难想到。  
对于独立的九个格子的顺序的判断语句：``k=i/3*3+j/3``很方便的确定了位置。  
总之增加了自己的积累。
## 3.代码
```c
bool isValidSudoku(char** board, int boardRowSize, int boardColSize) {
    int nums1[9][9]={0},nums2[9][9]={0},nums3[9][9]={0};
    for(int i=0;i<9;i++)
        for(int j=0;j<9;j++){
            if(board[i][j]=='.')
                continue;
            int num=board[i][j]-'0'-1;
            int k=i/3*3+j/3;
            if(nums1[i][num]||nums2[j][num]||nums3[k][num])
                return false;
            nums1[i][num]=nums2[j][num]=nums3[k][num]=1;
        }
    return true;
}
```
真的非常简单
