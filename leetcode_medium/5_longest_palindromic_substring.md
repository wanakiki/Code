## 5. Longest Palindromic Substring
##### 2018年2月24日21:09:35
##### 马拉车法
***
### 题目
>Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.  
给定一个字符串s，找到s中最长的回文子字符串。你可以假设s的最大长度是1000。

### 分析
要求找到最长的回文字符串，没有什么有效的方法，于是逐个判断。（我的代码超时了.......）  
因为回文字串从中间展开左右对称，可以用这个性质对每个点进行判断。但是要注意**字符串长度可能是奇数个也可能是偶数个**，所以要对这两种情况分类讨论。  
我定义了一个字符串分别用来存储字符的奇偶性，增加了很多计算，也从侧面反映了对指针掌握的不熟练。更多的细节都在代码里了。
### 代码
```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//奇数
int findodd(char *s,int i){
    int len=1,j=1;
    while(i-j>=0&&i+j<strlen(s)&&s[i-j]==s[i+j]){
        len+=2;
        j++;
    }
    return len;
}
//偶数
int findeven(char *s,int i){
    int len=2,j=1;
    while(i-j>=0&&i+j+1<strlen(s)&&s[i-j]==s[i+j+1]){
        len+=2;
        j++;
    }
    return len;
}
char* longestPalindrome(char* s) {
    int len=strlen(s);
    int max[3]={1,0,0}; //字符奇偶性、长度、中点位置
    int temp=0; //暂存长度
    for(int i=0;i<len;i++){
        if(s[i-1]==s[i]&&s[i]==s[i+1]){
            temp=findodd(s,i);
            if(temp>max[1]){
                max[1]=temp;
                max[0]=1;
                max[2]=i;
            }
        }
        //避免"ccc"的情况
        if(s[i]==s[i+1]){
            temp=findeven(s,i);
            if(temp>max[1]){
                max[1]=temp;
                max[0]=0;
                max[2]=i;
            }
        }
        else{
            temp=findodd(s,i);
            if(temp>max[1]){
                max[0]=1;
                max[1]=temp;
                max[2]=i;
            }
        }
        //printf("完成\n");
    }
    //返回部分
    char *r=(char*)malloc(sizeof(char)*(max[1]+1));
    for(int i=0;i<max[1];i++){
        if(max[0]==1)
            r[i]=s[max[2]-(max[1]-1)/2+i];
        else
            r[i]=s[max[2]-max[1]/2+1+i];
    }
    r[max[1]]='\0';
    return r;
}

```
这是我的代码，在面对无数个相同元素时出现了超时的问题。我找到了别人的和我思路相似的代码，比较之下发现个人能力的薄弱。
```c
int findOdd(char* s,int center){  
    int i=center-1,j=center+1;  
    while(i>=0 && s[j]){  
        if(s[i]!=s[j])return j-1;  
        i--;j++;  
    }  
    return j-1;  
}  
int findEven(char* s,int center){  
    int i=center,j=center+1;  
    while(i>=0 && s[j]){  
        if(s[i]!=s[j]){  
            return j-1;  
        }  
        i--;j++;  
    }  
    return j-1;  
}  
char* longestPalindrome(char* s) {  
    int i=0,end,Max=1,Maxf=0,Maxe=0;  
    for(i=0;s[i];i++){  
        end=findOdd(s,i);  
        if(Max<(end-i)*2+1){  
            Max=(end-i)*2+1;  
            Maxf=i+i-end;Maxe=end;  
        }  
        end=findEven(s,i);  
        if(Max<(end-i)*2){  
            Max=(end-i)*2;  
            Maxf=i+i+1-end;Maxe=end;  
        }  
    }  
    s[Maxe+1]=0;  
    return s+Maxf;  
}  
```
优点主要有：
1. 用指针截断的方式做出返回值，省去了很多计算
2. 判断奇偶性时设置了两个变量，用着比较方便
3. 对每个点都进行了判断，而不是和我一样判断奇偶性，尽管看起来麻烦，但是却能够提交
