## Length of Last Word
##### 2018年02月08日18:55:53
##### 相对简单的题目
***
### 题目
>Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.  
If the last word does not exist, return 0.  
Note: A word is defined as a character sequence consists of non-space characters only.  

### 分析
得出字符串长度，从最后不为空格的元素开始计数，返回单词长度。

注意输入为空，字符串末尾是空格的特殊情况。
### 代码
```c
int lengthOfLastWord(char* s) {
    if(s=="")
        return 0;
    int len=strlen(s);
    int len2=0;
    for(int i=len-1;i>=0;i--){
        if(s[i]!=' '){
            while(s[i]!=' '&&i>=0){
                i--;
                len2++;
            }
            return len2;
        }
    }
}
```
