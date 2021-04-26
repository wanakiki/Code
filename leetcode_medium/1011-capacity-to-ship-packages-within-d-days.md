## 1056. 在 D 天内送达包裹的能力

2021-04-26 15:52:35

### 题目

传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 ``i`` 个包裹的重量为 ``weights[i]``。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会
超过船的最大运载重量。

返回能在 ``D`` 天内将传送带上的所有包裹送达的船的最低运载能力。



**示例 1：**

```
输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是 
不允许的。
```

**示例 2：**

```
输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
```

**示例 3：**

```
输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
```



**提示：**


- ``1 <= D <= weights.length <= 50000``
- ``1 <= weights[i] <= 500``



[LeetCode链接](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/)

### 思路及代码

核心是用二分法查找可装运区间的左边界，查找数据范围为``[单个包裹最大重量, 包裹总重量]``，区间内一定存在解。

```cpp
class Solution {
public:
    int max_weight = INT_MIN;
    int max_d = 0;

    bool helper(int c, vector<int>& weights){
        int count = 0;
        int cur_sum = 0;
        for(auto n : weights){
            cur_sum += n;

            if(cur_sum == c){
                cur_sum = 0;
                count++;
            }
            else if(cur_sum > c){
                cur_sum = n;
                count++;
            }

            if(count > max_d){
                return false;
            }
        }

        if(cur_sum != 0){
            count++;
        }
        return count <= max_d;
    }

    int shipWithinDays(vector<int>& weights, int D) {
        // 计算累加和并统计最小值
        int len = weights.size();
        int sum_weight = 0;
        max_d = D;

        for(int i = 0; i < weights.size(); i++){
            max_weight = max(max_weight, weights[i]);
            sum_weight += weights[i];
        }

        // 二分法查找边界
        int left = max_weight, right = sum_weight;

        while(left < right){
            int mid = left + (right - left) / 2;
            if(helper(mid, weights)){
                right = mid;
            }
            else{
                left = mid + 1;
            }
        }
        return right;   // 区间一定存在解 不用考虑特殊情况
    }
};
```