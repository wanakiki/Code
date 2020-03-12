## 941. 有效的山脉数组

2020年2月27日

### 题目

给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

- A.length >= 3
- 在 0 < i < A.length - 1 条件下，存在 i  使得：
  - A[0] < A[1] < ... A[i-1] < A[i]
  - A[i] > A[i+1] > ... > A[B.length - 1]
 
示例 1：
```no
输入：[2,1]
输出：false
```
示例 2：
```no
输入：[3,5,5]
输出：false
```
示例 3：
```no
输入：[0,3,2,1]
输出：true
``` 

提示：

1. 0 <= A.length <= 10000
2. 0 <= A[i] <= 10000 

来源：力扣（LeetCode）  
链接：https://leetcode-cn.com/problems/valid-mountain-array

### 代码
执行用时:36ms,在所有C++提交中击败了43.79%的用户  
内存消耗:23.4MB,在所有C++提交中击败了5.35%的用户

```cpp
class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        if(A.size() < 3)
            return false;
        bool flag = true;
        int index;
        for(int i = 1; i < A.size(); i++){
            if(A[i] == A[i-1])
                return false;
            if(A[i] < A[i-1]){
                if(flag){
                    flag = false;
                    index = i-1;
                }
            }
            else{
                if(!flag)
                    return false;
            }
        }
        if(flag)
            return false;
        else{
            if(index == 0)
                return false;
            return true;
        }
    }
};
```
