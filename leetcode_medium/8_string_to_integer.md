##  String to Integer (atoi)
##### 2018年2月23日16:12:21
##### 写自己的atoi函数
***
### 分析
*题目要求实现atoi函数，并且给出了该函数的要求：*
- 函数要能够提取出字符串中的整数
- 函数需要丢弃字符串开头的空白，紧接着正负号，然后提取数字。（正负号非必须）
- 只提取第一个有效整数
- 当第一个非空白字符序列不是有效整数（包括正负号）时，或者字符串为空时返回零。
- 当整数溢出时，返回INT_MAX或者INT_MIN
- 例如：“       +45aaa12" 	返回45

*具体的思路就是逐个判断，没有什么好说的，说一点细节*
- 用``long``判断溢出，INT_MAX需要头文件``<limits.h>``
- ``isspace()、isdigit()``可以用来判断是否是空白、数字，头文件``<ctype.h>``
- **提交发现``+-2``返回值为0，但个人认为应为-2**，对于这个疑惑写了另一种判断方法解决（见代码）

### 代码
```c
#include<stdio.h>
#include<ctype.h>
#include<limits.h>
int myAtoi(char* str) {
    int flag=0;
    //用于标记符号，同时能够避免多个正负号的情况
    long num=0;   //做返回值，同时判断溢出
    while(isspace(*str))
        str++;
    if(*str=='-'||*str=='+'){
        if(*str=='-')
            flag-=1;
        else
            flag+=1;
        str++;
    }
    /*个人认为较正确的方法
    int flag=1;
    while(*str=='-'||*str=='+'){
        if(*str=='-')
            flag=-flag;
        str++;
    }*/
    if(!isdigit(*str))
        return 0;
    while(isdigit(*str) && num<=INT_MAX){
        num=num*10+*str-'0';
        str++;
    }
    if(num>INT_MAX)
        return flag<0? INT_MIN : INT_MAX;
    return flag<0? -num: num;

}
int main(){
    printf("测试自己的atoi函数\n");
    printf("输入字符串，20以内：");
    char a[20];
    gets(a);
    printf("结果是：%d",myAtoi(a));
}
```
