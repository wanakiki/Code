## 171. Excel Sheet Column Number
##### 2018-05-26 21:54:38
##### 简单题
***
## 题目

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```
Example 1:
```
Input: "A"
Output: 1
```
Example 2:
```
Input: "AB"
Output: 28
```
Example 3:
```
Input: "ZY"
Output: 701
```
## 分析
炒鸡简单的一道题目，不过做的时候没有结合c++的特性，运行速度较慢。
## 示例代码
```cpp
class Solution {
public:
    int titleToNumber(string s) {
        int len=s.size() , sum=0;
        for(int i=0;i<len;i++){
            sum+=sum*25 + s[i] - 'A'+1;
        }
        return sum;
    } 
   /* int titleToNumber(string s) {
        int num = 0;
        for (char c : s) {
            num += num * 25 + (c - 'A' + 1);
        }
        return num;
    }*/
    //注释的这部分是leetcode上面最快的解法，
    //我认为既然用了c++就应该想着去利用新的特性    
};
```

