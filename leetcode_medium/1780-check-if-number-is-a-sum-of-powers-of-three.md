## 1780. 判断一个数字是否可以表示成三的幂的和

2022-12-09 18:11:54

### 题目

给你一个整数 ``n`` ，如果你可以将 ``n`` 表示成若干个不同的三的幂之和，请你返回 ``true`` ，否则请返回 ``false`` 。

对于一个整数 ``y`` ，如果存在整数 ``x`` 满足 ``y == 3<sup>x</sup>`` ，我们称这个整数 ``y`` 是三的幂。

 

**示例 1：**

```
输入：n = 12
输出：true
解释：12 = 3<sup>1</sup> + 3<sup>2</sup>
```

**示例 2：**

```
输入：n = 91
输出：true
解释：91 = 3<sup>0</sup> + 3<sup>2</sup> + 3<sup>4</sup>
```

**示例 3：**

```
输入：n = 21
输出：false
```

 

**提示：**


- ``1 <= n <= 10<sup>7</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/check-if-number-is-a-sum-of-powers-of-three/)

### 思路及代码

```cpp
class Solution {
public:
    bool checkPowersOfThree(int n) {
        // 转换为3进制 保证每一位不会出现2

        while(n){
            int cur = n % 3;
            if(cur == 2)    return false;
            n /= 3;
        }
        return true;
    }
};
```