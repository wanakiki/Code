## 1321. 尽可能使字符串相等

2021-02-05 13:13:48

### 题目

给你两个长度相同的字符串，``s`` 和 ``t``。

将 ``s`` 中的第 ``i`` 个字符变到 ``t`` 中的第 ``i`` 个字符需要 ``|s[i] - t[i]|`` 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是 ``maxCost``。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 ``s`` 的子字符串转化为它在 ``t`` 中对应的子字符串，则返回可以转化的最大长度。

如果 ``s`` 中没有子字符串可以转化成 ``t`` 中对应的子字符串，则返回 ``0``。

 

**示例 1：**

```
输入：s = "abcd", t = "bcdf", cost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
```

**示例 2：**

```
输入：s = "abcd", t = "cdef", cost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
```

**示例 3：**

```
输入：s = "abcd", t = "acde", cost = 0
输出：1
解释：你无法作出任何改动，所以最大长度为 1。
```

 

**提示：**


- ``1 <= s.length, t.length <= 10^5``
- ``0 <= maxCost <= 10^6``
- ``s`` 和 ``t`` 都只含小写英文字母。



[LeetCode链接](https://leetcode-cn.com/problems/get-equal-substrings-within-budget/)

### 思路及代码

因为这几天每日一题都是和滑动窗相关的，这次也直接往滑动窗方向去想，发现题目还是比较简单的。首先计算每个位置变更字符的花费，接着就变成了滑动窗口求最大长度的问题。

```cpp
class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int len = s.size();
        vector<int> cost(len, 0);   // 转化花费
        for(int i = 0; i < len; i++){
            cost[i] = abs(s[i] - t[i]);
        }

        int left = 0, right = 0;
        int cur_len = 0;
        int total_cost = 0;
        int res = 0;
        while(right < len){
            total_cost += cost[right];
            cur_len += 1;
            if(total_cost <= maxCost){
                res = max(res, cur_len);
            }
            else{
                // 当花费大于最大值时移动左端点 该过程长度只会减少 不用更新长度
                while(total_cost > maxCost && left <= right){
                    total_cost -= cost[left];
                    left++;
                    cur_len -= 1;
                }
            }
            right++;
        }
        return res;
    }
};
```

写完代码之后看了看题解区，发现还有两处可以进行优化：一点是每处变更的花费是可以在O(1)的时间里计算出来的，可以不开辟数组保存；第二点是由于题目要求的是最大的长度，所以在花费超过最大值时可以只让左端点增加一次，保留可能的最大区间长度，但这种方法我用的还是不太习惯。