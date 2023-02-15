##  ZigZag Conversion
##### 2018年2月23日15:03:47
##### 找规律
***
### 题目
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
### 分析及代码
题目相对简单，重点是找到规律。
```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char* convert(char* s, int numRows) {
    if(numRows==1)
        return s;
    //排错，当行数为一时下面代码无需执行也不能执行
    int len=strlen(s),n=numRows-1;
    char*a=(char*)malloc(sizeof(char)*(len+1));
    strcpy(a,s);
    int flag=0;
    for(int i=0;i<numRows;i++){
        if(i==0){
                for(int j=0;j*n<len;j+=2)
                        a[flag++]=s[j*n];
                continue;
        }
        if(i==n){
            for(int j=1;j*n<len;j+=2)
                a[flag++]=s[j*n];
            continue;
        }
        for(int j=0;j*n-i<len||j*n+i<len;j+=2){
            if(j==0){
                a[flag++]=s[i];
                continue;
            }
            if(j*n-i<len)
                a[flag++]=s[j*n-i];
            if(j*n+i<len)
                a[flag++]=s[j*n+i];
        }
    }
    return a;
}
int main()
{
    printf("函数的作用是将输入的字符串做倒N变换\n");
    printf("输入字符串:");
    char a[20];
    gets(a);
    printf("输入行数:");
    int x;
    scanf("%d",&x);
    char *b=convert(a,x);
    puts(b);
}
```

2022年3月1日，CPP解法

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1)    return s;
        string res(s.size(), '0');
        int index = 0;
        int loop_len = numRows * 2 - 2;
        for(int i = 0; i < numRows; i++){
            int s_index = i;
            while(s_index < s.size()){
                if(i == 0 || i == numRows - 1){
                    if(s_index >= s.size()) break;
                    res[index++] = s[s_index];
                }
                else{
                    if(s_index >= s.size()) break;
                    res[index++] = s[s_index];
                    if(s_index + (numRows - i - 1) * 2 >= s.size()) break;
                    res[index++] = s[s_index + (numRows - i - 1) * 2];
                }
                s_index += loop_len;
                cout << res << endl;
            }
        }
        return res;
    }
};
```