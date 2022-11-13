## 857. 雇佣 K 名工人的最低成本

2022-09-11 11:04:57

### 题目

有 ``n`` 名工人。 给定两个数组 ``quality`` 和 ``wage`` ，其中，``quality[i]`` 表示第 ``i`` 名工人的工作质量，其最低期望工资为 ``wage[i]`` 。

现在我们想雇佣 ``k`` 名工人组成一个工资组。在雇佣 一组 ``k`` 名工人时，我们必须按照下述规则向他们支付工资：


- 对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。
- 工资组中的每名工人至少应当得到他们的最低期望工资。


给定整数 ``k`` ，返回*组成满足上述条件的付费群体所需的最小金额*。在实际答案的 ``10<sup>-5</sup>`` 以内的答案将被接受。。






**示例 1：**

```
输入： quality = [10,20,5], wage = [70,50,30], k = 2
输出： 105.00000
解释： 我们向 0 号工人支付 70，向 2 号工人支付 35。
```

**示例 2：**

```
输入： quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
输出： 30.66667
解释： 我们向 0 号工人支付 4，向 2 号和 3 号分别支付 13.33333。
```



**提示：**


- ``n == quality.length == wage.length``
- ``1 <= k <= n <= 10<sup>4</sup>``
- ``1 <= quality[i], wage[i] <= 10<sup>4</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/minimum-cost-to-hire-k-workers/)

### 思路及代码

读题可知，工资数应满足以下条件：$$\begin{gather*}
cost \cdot \frac{quality[i]}{total\_quality} \geq wage[i] \\
cost \geq total\_quality \cdot \frac{wage[i]}{quality[i]}
\end{gather*}$$

定义$\frac{wage[i]}{quality[i]}$为对于每个工人单位质量的价值，则对于确定的工资组，单价最高的工人决定了整个组的工资标准。

为获取最小的总工资数值，则应该满足在单价尽可能小的情况下获得最小的总质量。可以将每个人按照单价升序排序，之后使用大顶堆记录最小的总质量，过程中按照最大单价计算工资数值。



```cpp
class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        vector<int> index(quality.size(), 0);
        iota(index.begin(), index.end(), 0);    // 递增顺序填充

        sort(index.begin(), index.end(), [&](int& a, int& b){
            return wage[a] * quality[b] < wage[b] * quality[a];
        });

        priority_queue<int, vector<int>, less<int>> q;
        double res = DBL_MAX;
        double total_quality = 0;
        for(int i = 0; i < k-1; i++){
            q.push(quality[index[i]]);
            total_quality += quality[index[i]];
        }

        for(int i = k-1; i < index.size(); i++){
            total_quality += quality[index[i]];
            double tmp_cost = total_quality * wage[index[i]] / quality[index[i]];
            res = min(res, tmp_cost);
            q.push(quality[index[i]]);
            total_quality -= q.top();
            q.pop();
        }

        return res;
    }
};
```