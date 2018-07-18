## Add Binary
##### 2018年02月10日17:50:08
##### 指针，字符串还是不够熟练
***
### 题目
>Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
给定两个二进制字符串，返回它们的和（也是一个二进制字符串）。

### 分析
这种加和问题简单点考虑就是从最后一位开始向前加，注意进位。我的做法是定义字符指针，起始位置和两个数组中较长的一样，设置循环变量temp用于相加。当最大一位需要进位的时候我的做法是新建字符串"1"，两个相连接。
**两个数相加最大进位只能是一，0对应阿斯克码表的值为48**  
解法很简单，但是做的时候还是花费了很长时间，因为对指针的操作还不够熟练，出现了不少问题：
- 输入字符串时我用scanf逐个输入的方法出现了错误（缺少最后一个'\0'）

 ```c
	int x,y;
        scanf("%d %d",&x,&y);
        scanf("%c",&c);
        char zu[2],zu2[3],c;
        scanf("%c",&c);
        for(int i=0;i<2;i++)
                scanf("%c",&zu[i]);
        scanf("%c",&c);
        for(int i=0;i<3;i++)
                scanf("%c",&zu2[i]);
```
- 新建字符串时如果用malloc则不能直接用``a="1"``赋值 


### 代码
```c
char* addBinary(char* a, char* b) {
 int l1,l2;
        l1=strlen(a)-1;
        l2=strlen(b)-1;
        int l3=l1>l2 ? l1 : l2;
        char *c;
        if(l3==l1)
                c=a;
        else
                c=b;
        int temp=0;
        while(l1>=0 || l2>=0){
                if(l1>=0){
                        temp+=(a[l1]-48);
                        l1--;
                }
                if(l2>=0){
                        temp+=(b[l2]-48);
                        l2--;
                }
                c[l3]=temp%2+48;
                temp/=2;
                l3--;
        }
        if(temp==1){
                char *d;
                d=(char *)malloc(sizeof(char)*3);
                d[0]='1';
                d[1]='\0';      //原来是d="1" 不知道为什么不成功
                strcat(d,c);
                return d;
        }
        else{
                return c;
        }

}
```
