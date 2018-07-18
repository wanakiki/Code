## 278. First Bad Version
##### 第一个错误的版本号 
##### 2018年7月13日
****
## 题目
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
```
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
```
## 分析
题目要求找到第一个错误的版本号，并且要尽量减少判断函数的调用。实际上还是一个查找问题，自然而然地想到了二分法，测试之后发现大部分人也都是这个思路，目前最快的也是这种做法。

不知道还能不能再进行优化~
## 示例代码
C++:
```cpp
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int l = 1, r = n, mid;
        while(l < r){
            mid = l + (r - l)/2;
            if(isBadVersion(mid))
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
};
```
