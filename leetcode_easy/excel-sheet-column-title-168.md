## 168. Excel Sheet Column Title
##### 2018-05-24 22:21:03
##### 一行就可以解决的题目
***
## 题目

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```
Example 1:
```
Input: 1
Output: "A"
```
Example 2:
```
Input: 28
Output: "AB"
```
Example 3:
```
Input: 701
Output: "ZY"
```
## 分析
思路很简单，具体看代码。要注意一点，因为加上的'A'，所以所有的数都应该减一。
## 示例代码
```cpp
class Solution {
public:
    string convertToTitle(int n) {
        return n == 0 ? "" : convertToTitle((n - 1) / 26) + (char) ((n - 1) % 26 + 'A');
    }
};
```
