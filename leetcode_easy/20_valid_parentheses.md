## 20. Valid Parentheses
##### 2018年02月13日18:09:23
##### 栈操作
*****
### 题目
>Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
给定一个只包含字符'（'，'）'，'{'，'}'，'['和']'的字符串，确定输入字符串是否有效。 括号必须以正确的顺序关闭，“（）”和“（）[] {}”全部有效，但“（]”和“（[）]”不是。

### 分析
先说一种取巧的方法：由于字符串只有括号，我们可以先遍历字符串，遇到右括号就向前找配对的括号，之后把这两个元素全用不是括号的字符替换（比如'a'），找不到就返回错误，遍历结束后再排查是否有多余的括号。 

但是当初学习的时候是用压栈和出栈达到配对的目的，当时就不太明白[栈](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%A0%88)，今天又看了看。  

栈也是一种数据结构，有先入后出的特点。实现的方法可以有链表或者数组，为了方便，我用数组的方法解决了这道题。
### 代码
```c
struct stack
{
        int a[1000000];	//数组方法的坏处是栈的长度是固定的，取巧设立比较大的长度，接受了leetcode测试例
        int top;
};

bool isValid(char* s) {
       struct stack new;
        new.top=0;
        int k=0;
        while(s[k]!='\0')
                k++;
        for(int i=0;i<k;i++){
                if(s[i]=='(' || s[i]=='{' || s[i]=='['){
                        new.top+=1;
                        new.a[new.top]=s[i];
                }
                else{
                        if(new.a[new.top]+1==s[i] || new.a[new.top]+2==s[i])
                                new.top-=1;
                        else
                                return false;
                }
        }
	//上面就是普通的栈操作
	//注意用下面的代码排除只有左括号的情况
        if(new.top!=0)
            return false;
        return true;
}
```

Python3同样是使用栈的思路（2018年8月3日）：

```py
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, p_map = [], {')':'(', '}':'{', ']':'['}
        for c in s:
            if c not in p_map:
                stack.append(c)
            elif not stack or p_map[c] != stack.pop():
                return False
        return not stack
```