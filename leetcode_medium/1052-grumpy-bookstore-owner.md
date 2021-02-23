## 1138. 爱生气的书店老板

2021-02-23 11:25:27

### 题目

今天，书店老板有一家店打算试营业 ``customers.length`` 分钟。每分钟都有一些顾客（``customers[i]``）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 ``i`` 分钟生气，那么 ``grumpy[i] = 1``，否则 ``grumpy[i] = 0``。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 ``X`` 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。

 

**示例：**

```
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
```

 
**提示：**


- ``1 <= X <= customers.length == grumpy.length <= 20000``
- ``0 <= customers[i] <= 1000``
- ``0 <= grumpy[i] <= 1``



[LeetCode链接](https://leetcode-cn.com/problems/grumpy-bookstore-owner/)

### 思路及代码

之前校赛的时候遇到过这个问题，用滑动窗统计新增满意用户的最大值即可。

```cpp
class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int X) {
        // 不考虑老板的不生气能力 总的满意客户数是固定的
        // 题目要求的是能够带来最多新的满意客户的窗
        int initial_sum = 0;
        for(int i = 0; i < customers.size(); i++){
            if(grumpy[i] == 0){
                initial_sum += customers[i];
            }
        }

        int res = 0;
        int cur_cus = 0;    // 指当前窗内新增满意顾客
        int left = 0, right = X;
        for(int i = 0; i < right; i++){
            if(grumpy[i]){
                cur_cus += customers[i];
            }
        }
        res = cur_cus;

        while(right < customers.size()){
            if(grumpy[left]){
                cur_cus -= customers[left];
            }
            left++;
            
            if(grumpy[right]){
                cur_cus += customers[right];
            }
            right++;
            res = max(res, cur_cus);
        }
        return initial_sum + res;
    }
};
```

上面的方法还可以进行改进，将统计原有满意用户这一步骤整合到窗口滑动过程中。