## 1817. 计算力扣银行的钱

2022-01-15 15:37:40

### 题目

Hercy 想要为购买第一辆车存钱。他 **每天** 都往力扣银行里存钱。

最开始，他在周一的时候存入 ``1`` 块钱。从周二到周日，他每天都比前一天多存入 ``1`` 块钱。在接下来每一个周一，他都会
比 **前一个周一** 多存入 ``1`` 块钱。<span style=""> </span>

给你 ``n`` ，请你返回在第 ``n`` 天结束的时候他在力扣银行总共存了多少块钱。

 

**示例 1：**

```
输入：n = 4
输出：10
解释：第 4 天后，总额为 1 + 2 + 3 + 4 = 10 。
```

**示例 2：**

```
输入：n = 10
输出：37
解释：第 10 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37 。注意到第二个星期一，Hercy 存入 2 块钱。 
```

**示例 3：**

```
输入：n = 20
输出：96
解释：第 20 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96 
。
```

 

**提示：**


- ``1 <= n <= 1000``



[LeetCode链接](https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank/)

### 思路及代码

等差数列计算

```cpp
class Solution {
public:
    int totalMoney(int n) {
        int total_week = n / 7;
        int last_day = n % 7;
        int res = 0;

        if(total_week > 0){
            int week_val = 7 * (1 + 7) / 2;
            res = week_val * total_week + total_week * (0 + 7 * (total_week - 1)) / 2;
        }
        
        int start_val = total_week + 1;
        res += last_day * (start_val + start_val + last_day - 1) / 2;
        return res;
    }
};
```