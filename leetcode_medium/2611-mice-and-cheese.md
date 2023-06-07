## 2611. 老鼠和奶酪

2023-06-07 10:00:53

### 题目

有两只老鼠和 ``n`` 块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。

下标为 ``i`` 处的奶酪被吃掉的得分为：


- 如果第一只老鼠吃掉，则得分为 ``reward1[i]`` 。
- 如果第二只老鼠吃掉，则得分为 ``reward2[i]`` 。


给你一个正整数数组 ``reward1`` ，一个正整数数组 ``reward2`` ，和一个非负整数 ``k`` 。

请你返回第一只老鼠恰好吃掉 ``k`` 块奶酪的情况下，**最大** 得分为多少。

 

**示例 1：**

```

输入：reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
输出：15
解释：这个例子中，第一只老鼠吃掉第 2 和 3 块奶酪（下标从 0 开始），第二只老鼠吃掉第 0 和 1 块奶酪。
总得分为 4 + 4 + 3 + 4 = 15 。
15 是最高得分。
```

**示例 2：**

```

输入：reward1 = [1,1], reward2 = [1,1], k = 2
输出：2
解释：这个例子中，第一只老鼠吃掉第 0 和 1 块奶酪（下标从 0 开始），第二只老鼠不吃任何奶酪。
总得分为 1 + 1 = 2 。
2 是最高得分。
```

 

**提示：**


- ``1 <= n == reward1.length == reward2.length <= 10<sup>5</sup>``
- ``1 <= reward1[i], reward2[i] <= 1000``
- ``0 <= k <= n``



[LeetCode链接](https://leetcode-cn.com/problems/mice-and-cheese/)

### 思路及代码

由全部的reward2计算出基准得分，之后在reward1中选择k个性价比最高的奶酪进行得分替换。

```cpp
class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        int res = 0;
        for(int i = 0; i < reward1.size(); i++){
            reward1[i] -= reward2[i];
            res += reward2[i];
        }   

        sort(reward1.begin(), reward1.end(), greater<int>());
        for(int i = 0; i < k;i++){
            res += reward1[i];
        }
        return res;
    }
};
```