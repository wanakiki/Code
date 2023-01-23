## 1815. 得到新鲜甜甜圈的最多组数

2023-01-23 21:08:09

### 题目

有一个甜甜圈商店，每批次都烤 ``batchSize`` 个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 **所有** 甜甜圈都必须已经全部销售完毕。给你一个整数 ``batchSize`` 和一个整数数组 ``groups`` ，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中 ``groups[i]`` 表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。

当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。

你可以随意安排每批顾客到来的顺序。请你返回在此前提下，**最多** 有多少组人会感到开心。

 

**示例 1：**

```
输入：batchSize = 3, groups = [1,2,3,4,5,6]
输出：4
解释：你可以将这些批次的顾客顺序安排为 [6,2,4,5,1,3] 。那么第 1，2，4，6 组都会感到开心。
```

**示例 2：**

```
输入：batchSize = 4, groups = [1,3,2,5,2,2,1,6]
输出：4
```

 

**提示：**


- ``1 <= batchSize <= 9``
- ``1 <= groups.length <= 30``
- ``1 <= groups[i] <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/maximum-number-of-groups-getting-fresh-donuts/)

### 思路及代码

根据题目，应该关注每个小组成员数目模batchsize之后的数值。可以通过动态规划方式，使用long long定义模batchsize之后各个数值的使用次数，进行搜索。

搞清楚核心思路之后题目实现并不困难，但具体运行时需要考虑位运算和long long的细节。如果在进行搜索时对模batchsize为0的数值正常处理则会导致超时，需要进行优化。

```cpp
class Solution {
public:
    int mask = 5;   // 使用五位二进制保存每个数字出现的次数
    int helper(int batchSize, long long cur_val, unordered_map<long long, int>& hash_val, unordered_map<long long, int>& hash_mod){
        if(hash_val.find(cur_val) != hash_val.end())    return hash_val[cur_val];

        int res = 0;
        for(int i = 1; i < batchSize; i++){
            // 获取指定位数值并判断是否已经达到零 到零不可减少
            int val = (cur_val >> ((i - 1) * mask)) & ((1 << mask) - 1);
            if(val > 0){
                // cout << cur_val << ' ' << val << ' ' << i << ' ' << (1LL << ((i - 1) * mask)) << endl;
                long long next_val = cur_val - (1LL << ((i - 1) * mask));        // 此处也需要确保左移不越界
                int happy_count = helper(batchSize, next_val, hash_val, hash_mod);
                int new_mod = (hash_mod[next_val] + i) % batchSize;

                if(hash_mod.find(cur_val) == hash_mod.end())    hash_mod[cur_val] = new_mod;    // 记录当前人数总和模batchsize的结果

                // 如果在添加当前组之前已经凑整，则当前组会感到开心
                if(hash_mod[next_val] == 0) happy_count++;
                res = max(res, happy_count);
            }
        }
        hash_val[cur_val] = res;
        return res;
    }
    int maxHappyGroups(int batchSize, vector<int>& groups) {
        unordered_map<long long, int> hash_val; // 当前配置的最大满意数
        unordered_map<long long, int> hash_mod; // 当前配置下模batchsize的结果
        

        vector<long long> count(batchSize, 0);
        for(auto n : groups){
            count[n % batchSize]++;
        }

        // 深度优先搜索
        long long max_val = 0;
        hash_val[0] = count[0];    // 搜索终止条件
        hash_mod[0] = 0;

        // 构造首项
        // for(int i = 0; i < batchSize; i++){
        //     max_val |= (count[i] << (i * mask));    // 此处需要确保 count[i] 为long long格式，避免左移越界
        // }

        // 反向处理并不需要保证count为long long
        for(int i = batchSize - 1; i > 0; i--){
            max_val = (max_val << mask) | count[i];
        }
        return helper(batchSize, max_val, hash_val, hash_mod);
    }
};
```