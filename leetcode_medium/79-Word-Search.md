## 79. Word Search
##### 2018-03-26
##### 回溯 有、东西
*****
## 1.题目
>Given a 2D board and a word, find if the word exists in the grid.
>
>The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.   
>给定二维字符数组，在其中查找是否具有相邻字母组成所给单词，相邻是指上下或者左右相邻，并且每个字母只能够用一次。  

## 2.分析
因为这道题是回溯，一直不愿意去写，但实际上走出第一步之后别的就简单多了。  👌

题目解法显而易见，由于自己对回溯还是不够熟练，在处理每个字符只能用一次这点时第一个想法是再构建一个函数用来记录当前用过的字符。  
但实际上，因为回溯的实现类型，我们完全可以对原数组进行操作，赋一个新值，在回溯处理结束之后再将该位置还原，最终正常实现。

解题过程中还还出现了一个问题，因为我对于单词结束的判断是当前传入的值为0，这种情况在数组只有一个字母的时候因为不会进行回溯会出现错误。  
将单词结束的判断改为下一位为0之后成功AC。
## 3.代码
```c
bool find(char ** board,int row,int col,int i,int j,char *word){
  if(!*word)
    return true;
  if(board[i][j]!=*word)
    return false;
  char temp=board[i][j];
  board[i][j]=' ';
  //向右
  if(j+1<col && board[i][j+1]!=' ' && find(board,row,col,i,j+1,word+1))
    return true;
  //向下
  if(i+1<row && board[i+1][j]!=' ' && find(board,row,col,i+1,j,word+1))
    return true;
  //向左
  if(j>0 && board[i][j-1]!=' ' && find(board,row,col,i,j-1,word+1))
    return true;
  //向上
  if(i>0 && board[i-1][j]!=' ' && find(board,row,col,i-1,j,word+1))
    return true;
  board[i][j]=temp; //数据还原
  return false;
}

bool exist(char** board, int row, int col, char* word) {
  for(int i=0;i<row;i++)
  for(int j=0;j<col;j++){
    if(find(board,row,col,i,j,word))
      return true;
  }
  return false;
}
```

