## Longest Common Prefix
##### 2018年02月05日10:27:20
##### 注意基础....
***
### 题目
>Write a function to find the longest common prefix string amongst an array of strings.  
编写一个函数来查找字符串数组中最长的公共前缀字符串。  

### 分析
区分C语言中的单引号和双引号：
 - 双引号引起字符串，代表的是指向无名数组起始字符的指针，大小为字符大小加一（会在字符串末尾自动添加字符'\0'）   
 
 - 单引号引起的字符实际上代表一个整数，整数值对应于该字符在编译器采用的字符集中的序列值。一般我们的编译器采用的都是ASCII字符集。因此's'的含义其实和十进制数115的含义是一致的。大小为一个字节。

**截断字符串的技巧：将该位的值变为``\0``**
 
由于要求找出来最长的公共前缀，实现方法很简单，从每个字符串的第一位开始逐个比较，如果有不同直接返回。还要注意输入为空的特殊情况。  
  
起初我的做法是定义一个极长的字符串temp用于返回，从字符串第一位开始，将每个字符串和它的下一个字符串进行比较，一个循环向temp存储一个值，发现不同在该位截断返回temp。方法虽然麻烦但是能实现。    

之后发现由于是公共的前缀，**所以所有的字符串都有该部分**，我们可以直接复制第一个字符串到temp，与其他的字符串逐位比较，不同处截断，开始比较下一个，比较完之后返回temp，方法简洁明了。

最后补充一下输入为空的特殊情况，当输入为空时，由于我们最终的做法是直接复制第一个字符串，所以我们的返回值也为空（null），但是理想结果是``""``，所以我们可以加一个判断，当字符串个数为零时我们直接返回``""``就可以解决这个问题。

### 代码
```c
char* longestCommonPrefix(char** strs, int strsSize) {
if(strsSize<=0)
        return "";	//判断是否为空
char *temp;
temp=strs[0];
int index=0;
for(int i=1;i<strsSize;i++)
for(int j=0;temp[j]!='\0';j++){
	if(temp[j]!=strs[i][j]){
		temp[j]='\0';	//不同处截断字符串
		continue;
	}
}
return temp;
}
```

~~最后说一句，我尝试了几个方法，但是没能写出能够自定义测试案例的主函数，如果你写了出来谢谢指教。~~
***
2018年7月31日补充主函数：

```c
int main(){
    int strsSize = 0;
    printf("Input the number of strs:");
    scanf("%d", &strsSize);

    char ** strs;
    strs = (char **) malloc (sizeof(char*) * strsSize);
    for(int i = 0; i < strsSize; i++){
        strs[i] = (char*) malloc(sizeof(char) * 11);
    }
    printf("Please input the strs, no longer than 10, divided by enter:\n");

    char temp = 0;
    for(int i = 0; i < strsSize; i++){
        scanf("%s", strs[i]);
        scanf("%c", &temp);
    }
    char *p = longestCommonPrefix(strs, strsSize);
        printf("The result is: %s\n", p );
}
```

可能这个时候自己还真的不会用malloc😂