## 125. Valid Palindrome
##### 2018年2月22日12:16:31
##### 扩充函数认识
***
### 题目
>Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.  
判断字符串是否是回文，只考虑字母数字并忽略其他情况。空串也看做回文。

### 分析
做这道题目的时候第一次知道了标准库函数的概念。因为``strlwr()``不是标准库函数，只能在windows下（VC、MinGW等）使用，Linux GCC中需要自己定义。  
另外还了解了两个函数（``ctype.h``头文件）：
- ``isalnum(c)``检查参数是否为字母或者数字
- ``tolower(c)``把字符转化为小写字母，非字母字符不做处理

因为出现了不少问题，这道题主要参考了别人的代码。
### 代码
```c
bool isPalindrome(char *s){
	int len=strlen(s);
	if(!len) return true;
	char *p=s,*q=s+len-1;
	while(p<q){
	//这个判断条件和下面的continue配合灰常好
	if(!isalnum(*p)) {p++;continue;}
	if(!isalnum(*q)) {q--;continue;}
	if(tolower(*p++) != tolower(*q--)) return false;
	//条件中直接加加减减省去了很多麻烦
	}
	return true;
}
```
[原文地址](https://leetcode.com/problems/valid-palindrome/discuss/40142/C-solution-9-lines-4ms-using-pointer)
