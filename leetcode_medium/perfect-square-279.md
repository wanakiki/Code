## 279. Perfect Squares
##### 2018年7月22日
***
### 题目
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
```
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```
Example 2:
```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

### 分析
这道题目考察的是四平方和定理，一个从来没有听过的定理，即一个数一定能由四个以内的数的平方的和组成。[维基](https://zh.wikipedia.org/wiki/%E5%9B%9B%E5%B9%B3%E6%96%B9%E5%92%8C%E5%AE%9A%E7%90%86)
针对这个问题还有两种特殊的情况，如果一个数除以八余七，则这个数一定由三个数组成；第二点是想3、8，4、12这种大数除小数得到四的情况，返回的结果相同。

### 示例代码
```cpp
class Solution {
public:
    /* int helper(int n){
        if(n){
            for(int i = 1;;i++){
                if(pow(i + 1, 2) > n){
                    return 1 + helper(n - pow(i,2));
                }
            }
        }
        else
            return 0;
    }
    注释掉的这部分是我的错误代码..*/
    int numSquares(int n) {
        while(n % 4 == 0)   n /=4;
        if( n % 8 ==7)  return 4;
        for(int a  = 0; a * a <= n; a++){
            int b = sqrt(n - a * a);
            if (a * a + b == n)
                return !!a + !!b; //逻辑取反
        }
        return 3;
    }
};
```
[参考](https://www.cnblogs.com/grandyang/p/4800552.html)
