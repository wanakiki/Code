## 201. Bitwise AND of Numbers Range
##### 2018年7月17日
##### 位运算
***
## 题目
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
```
Input: [5,7]
Output: 4
```
Example 2:
```
Input: [0,1]
Output: 0
```
## 分析
## 示例代码
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int i = 0;
        while(m != n){
            m >>= 1;
            n >>= 1;
            i++;
        }
        return (m << i);
    }
};
```
