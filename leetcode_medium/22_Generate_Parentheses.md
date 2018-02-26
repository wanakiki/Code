## 22. Generate Parentheses
##### 2018年2月26日22:13:22
##### 加强递归
***
### 题目
>Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.  
给出n对括号的全部有效排列
For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```
### 分析
与17. Letter Combinations of a Phone Number相似，也是需要写出来很多种排列。  
没有想到有效的推导方式，于是又去网上找的代码，然后给自己又留了一个坑。   
因为最开始的想法是从一对开始排，然后逐个添加，出现了很多重复有没有有效的排除方式，带着这种思路不明白逐个添加的递归方式怎么处理重复。   
但现在发现好像没有重复.......

### 代码
```c
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
 void generate(char** res,int *returnSize,int l,int r,char *temp,int index)
 {
     if(l==0&&r==0){
        res[*returnSize]=(char*)malloc(sizeof(char)*(index));
        temp[index]='\0';
        strcpy(res[*returnSize],temp);
        (*returnSize)++;
        return;
     }
     if(l>0){
        temp[index]='(';
        generate(res,returnSize,l-1,r,temp,index+1);
     }
     if(r>0&&l<r)   //l<r才能输入
     {
         temp[index]=')';
         generate(res,returnSize,l,r-1,temp,index+1);
     }
 }
char** generateParenthesis(int n, int* returnSize) {
    char **res;
    res=(char**)malloc(sizeof(char*)*1000000);
    char *temp=(char*)malloc(sizeof(char)*(n*2+1));
    int l=n,r=n;    //左括号右括号个数
    *returnSize=0;
    generate(res,returnSize,l,r,temp,0);
    return res;
}
```
