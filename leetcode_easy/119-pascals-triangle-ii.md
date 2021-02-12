## 119. 杨辉三角 II

2021-02-12 08:38:36

### 题目

给定一个非负索引*k*，其中*k* < 33，返回杨辉三角的第*k*行。

<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif">

<small>在杨辉三角中，每个数是它左上方和右上方的数的和。</small>

**示例:**

```
输入: 3
输出: [1,3,3,1]
```

**进阶：**

你可以优化你的算法到O(<em>k</em>) 空间复杂度吗？


[LeetCode链接](https://leetcode-cn.com/problems/pascals-triangle-ii/)

### 思路及代码

```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex+1, 1);
        int cur = 0;
        while(cur <= rowIndex){
            for(int i = cur - 1; i > 0; i--){
                res[i] += res[i-1];
            }
            cur++;
        }
        return res;
    }
};
```