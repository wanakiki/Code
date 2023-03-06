## 1653. 使字符串平衡的最少删除次数

2023-03-06 10:55:53

### 题目

给你一个字符串 ``s`` ，它仅包含字符 ``'a'`` 和 ``'b'``​​​​ 。

你可以删除 ``s`` 中任意数目的字符，使得 ``s`` **平衡** 。当不存在下标对 ``(i,j)`` 满足 ``i < j`` ，且 ``s[i] = 'b'`` 的同时 ``s[j]= 'a'`` ，此时认为 ``s`` 是 **平衡 **的。

请你返回使 ``s`` **平衡** 的 **最少** 删除次数。

 

**示例 1：**

```
输入：s = "aababbab"
输出：2
解释：你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
```

**示例 2：**

```
输入：s = "bbaaaaabb"
输出：2
解释：唯一的最优解是删除最前面两个字符。
```

 

**提示：**


- ``1 <= s.length <= 10<sup>5</sup>``
- ``s[i]`` 要么是 ``'a'`` 要么是 ``'b'``​** **。​



[LeetCode链接](https://leetcode-cn.com/problems/minimum-deletions-to-make-string-balanced/)

### 思路及代码

一共有三种情况：

- 删除所有的 a
- 删除所有的 b
- 找到一个位置，删除元素使该位置左侧只有 a 右侧只有 b

考虑上述情况即可。

```cpp
class Solution {
public:
    int minimumDeletions(string s) {
        vector<int> count_a(s.size(), 0);
        vector<int> count_b(s.size(), 0);

        for(int i = 0; i < s.size(); i++){
            if(s[i] == 'a'){
                count_a[i] = 1;
            }
            else{
                count_b[i] = 1;
            }
            if(i != 0)  count_b[i] += count_b[i-1];
            if(i != 0)  count_a[i] += count_a[i-1];
        }

        int max_a = count_a[s.size() - 1];
        int max_b = count_b[s.size() - 1];

        // 找到最合适的位置
        int res = INT_MAX;
        res = min(max_a, max_b);    // 选择在边界

        for(int i = 1; i < s.size(); i++){
           //  res = min(res, count_a[i-1] + max_b - count_b[i-1]);
            res = min(res, count_b[i-1] + max_a - count_a[i-1]);
        }
        return res;
    }
};
```