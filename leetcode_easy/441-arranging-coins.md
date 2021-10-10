## 441. 排列硬币

2021-10-10 15:46:06

### 题目

你总共有 ``n``枚硬币，并计划将它们按阶梯状排列。对于一个由 ``k`` 行组成的阶梯，其第 ``i``行必须正好有 
``i``枚硬币。阶梯的最后一行 **可能** 是不完整的。

给你一个数字 ``n``，计算并返回可形成 **完整阶梯行** 的总行数。



**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/arrangecoins1-grid.jpg" style="width: 253px; height: 253px;" />
```
输入：n = 5
输出：2
解释：因为第三行不完整，所以返回 2 。
```

**示例 2：**
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/arrangecoins2-grid.jpg" style="width: 333px; height: 333px;" />
```
输入：n = 8
输出：3
解释：因为第四行不完整，所以返回 3 。
```



**提示：**


- ``1 <= n <= 2<sup>31</sup> - 1``



[LeetCode链接](https://leetcode-cn.com/problems/arranging-coins/)

### 思路及代码

二分法查找边界，找到对应硬币总数小于等于n的最大阶梯数。

```cpp
class Solution {
public:
    int arrangeCoins(int n) {
        // n >= k(k+1)/2
        int left = 1, right = n;    // 确定上下界
        while(left < right){
            long long mid = left + (right - left + 1) / 2;    // 相邻情况取靠右一侧，有助于向左缩进
            long long coin = (mid * (mid + 1)) / 2;

            if(coin <= n){
                left = mid;
            }
            else{
                right = mid - 1;
            }
        }
        return left;
    }
};
```