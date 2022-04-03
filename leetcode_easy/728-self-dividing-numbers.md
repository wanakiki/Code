## 728. 自除数

2022-03-31 14:34:03

### 题目

**自除数** 是指可以被它包含的每一位数整除的数。


- 例如，``128`` 是一个 **自除数** ，因为 ``128 % 1 == 0``，``128 % 2 == 0``，``128 % 8 == 0``。


**自除数** 不允许包含 0 。

给定两个整数 ``left`` 和 ``right`` ，返回一个列表，列表的元素是范围 ``[left, right]`` 内所有的 **自除数**。



**示例 1：**

```
输入：left = 1, right = 22
输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
```

**示例 2:**

```
输入：left = 47, right = 85
输出：[48,55,66,77]
```



**提示：**


- ``1 <= left <= right <= 10<sup>4</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/self-dividing-numbers/)

### 思路及代码

数据量不大，直接采用暴力做法，遍历区间中的每个数字，提取数字的每一位并判断是否为零或者是否能够被整除，返回满足条件的数字。

```cpp
class Solution {
public:
    bool helper(int n){
        int t = n;
        while(t > 0){
            int cur = t % 10;
            t /= 10;

            if(cur == 0 || n % cur != 0)    return false;
        }
        return true;
    }
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        for(int i = left; i <= right; i++){
            if(helper(i)){
                res.push_back(i);
            }
        }
        return res;
    }
};
```