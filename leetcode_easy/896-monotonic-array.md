## 932. 单调数列

2021-02-28 09:29:12

### 题目

如果数组是单调递增或单调递减的，那么它是<em>单调的</em>。

如果对于所有 ``i <= j``，``A[i] <= A[j]``，那么数组 ``A`` 是单调递增的。 如果对于所有 ``i <= j``，``A[i]> = A[j]``，那么数组 ``A`` 是单调递减的。

当给定的数组 ``A`` 是单调数组时返回 ``true``，否则返回 ``false``。

 

**示例 1：**

```
输入：[1,2,2,3]
输出：true
```

**示例 2：**

```
输入：[6,5,4,4]
输出：true
```

**示例 3：**

```
输入：[1,3,2]
输出：false
```

**示例 4：**

```
输入：[1,2,4,5]
输出：true
```

**示例 5：**

```
输入：[1,1,1]
输出：true
```

 

**提示：**


- ``1 <= A.length <= 50000``
- ``-100000 <= A[i] <= 100000``



[LeetCode链接](https://leetcode-cn.com/problems/monotonic-array/)

### 思路及代码

如果数列中同时出现了增长和减少两种情况，则不单调。

```cpp
class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        bool inc = false, dec = false;
        for(int i = 1; i < A.size(); i++){
            if(A[i] > A[i-1]){
                inc = true;
            }
            if(A[i] < A[i-1]){
                dec = true;
            }

            if(inc && dec){
                return false;
            }
        }
        return true;
    }
};
```