## 1830. 大餐计数  

2021-07-07 10:12:34

### 题目

**大餐** 是指 **恰好包含两道不同餐品** 的一餐，其美味程度之和等于 2 的幂。

你可以搭配 **任意** 两道餐品做一顿大餐。

给你一个整数数组 ``deliciousness`` ，其中 ``deliciousness[i]`` 是第 ``i<sup>​​​​​​</sup>​​​​``​​​​ 道餐品的美味程度，返 
回你可以用数组中的餐品做出的不同 **大餐** 的数量。结果需要对 ``10<sup>9</sup> + 7`` 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。

 

**示例 1：**

```
输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
```

**示例 2：**

```
输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
```

 

**提示：**


- ``1 <= deliciousness.length <= 10<sup>5</sup>``
- ``0 <= deliciousness[i] <= 2<sup>20</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/count-good-meals/)

### 思路及代码

哈希表统计每种数值出现的次数，之后通过数据左移获取所有范围内2的幂，查找是否有能够和当前数字累加之后恰好为2的幂的数字，之后计算对应的组合数。当自己能和自己构成大餐时，需要按照组合公式计算，稍微麻烦一些。上面的做法在查找元素时需要确保待查找的元素大于当前元素来避免重复。

官方题解的做法是在统计数据出现次数的同时计算能构成大餐的数对个数，按照这种方法不需要注意重复情况也不需要计算组合数。

```cpp
class Solution {
public:
    long long helper(int n, int m = 2){
        if(n == m) return 1;

        if(m < n - m) m = n - m;
        long long res = 1;
        for(int i = m + 1; i <= n; i++){
            res *= i;
        }
        for(int i = 1; i <= n - m; i++){
            res /= i;
        }
        return res;
    }

    int countPairs(vector<int>& deliciousness) {
        int MOD = 1e9 + 7;

        unordered_map<int, int> hash;
        for(auto i : deliciousness){
            hash[i]++;
        }

        long long res = 0;

        for(auto p : hash){
            int cur = 1;
            for(int i = 0; i < 22; i++){
                int left = cur - p.first;   // 剩余部分数字

                // 只计算右侧数字大于等于左侧的情况 避免重复计算
                if(left >= 0 && p.first <= left){
                    // 相同数值配对 仅在有多个时成立
                    if(left == p.first){
                        if(p.second > 1){
                            res += helper(p.second);
                            res %= MOD;
                        }
                    }
                    else{
                        auto it = hash.find(left);
                        if(it != hash.end()){
                            res += p.second * it->second;
                            res %= MOD;
                        }
                    }
                }
                cur <<= 1;
            }
        }
        return res;
    }
};
```