## 151. Reverse Words in a String
##### 2018-05-12 12:50:45
##### 相对较麻烦的题目(至少对于我)
***
## 题目
Given an input string, reverse the string word by word.

Example:
```
Input: "the sky is blue",
Output: "blue is sky the".
```
Note:

- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up: For C programmers, try to solve it in-place in O(1) space.
## 分析
要求实现单词出现顺序的反转，同时将单词之间的多个空格合并。

既然要实现反转，字符串反转函数我认为是必不可少的。其次因为有合并多个空格的要求，还要注意用``resize``函数重置字符串的长度。

尽管知道了这些该注意的点，但是想到具体的操作还不是件简单的事。我参考了下别人的方案：
>遍历，先将空格合并，再将单词字母顺序反转，遍历结束后将整个字符串反转，这样就达到了保证单词字母顺序不变改变出现顺序的目的。

## 示例代码
```cpp
class Solution {
public:
    void reverse(string & s,int i,int j){
        while(i<j){
            char t=s[i];
            s[i++]=s[j];
            s[j--]=t;
        }
    }
    void reverseWords(string &s) {
        int i=0,j=0;
        int len=s.size();
        int word=0;
        int l=0;

        while(1){
            while(i<len && s[i]==' ')   i++;        //删除空格 用while
            if(i==len)  break;
            if(word)    s[j++]=' '; //保留单词之间的空格

            l=j;
            while(i<len && s[i]!=' ') //j一定小于等于i
                s[j++]=s[i++];
            reverse(s,l,j-1);
            word++;
        }
        s.resize(j);
        reverse(s,0,j-1);   //注意为j-1
    }
};
```
