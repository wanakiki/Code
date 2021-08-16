## 526. 优美的排列

2021-08-16 09:58:06

### 题目

假设有从 1 到 N 的 **N** 个整数，如果从这 **N** 个数字中成功构造出一个数组，使得数组的第 **i** 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：


- 第 **i**位的数字能被 **i**整除
- **i** 能被第 **i** 位上的数字整除


现在给定一个整数 N，请问可以构造多少个优美的排列？

**示例1:**

```
输入: 2
输出: 2
解释:

第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
```

**说明:**


- **N** 是一个正整数，并且不会超过15。



[LeetCode链接](https://leetcode-cn.com/problems/beautiful-arrangement/)

### 思路及代码


题目的要求是使用1-n一共n个数字构建长度为n的数组，使数组满足优美条件。由于数组长度不超过十五，可以预先计算每个位置可以放置的值，之后回溯探索可能的放置情况并统计。

```cpp
class Solution {
public:
    int res = 0;
    vector<int> visited;
    vector<vector<int>> match;

    void helper(int index, int n){
        if(index == n + 1){
            res++;
            return;
        }

        for(int i = 0; i < match[index].size(); i++){
            if(visited[match[index][i]] == 1)    continue;
            visited[match[index][i]] = 1;
            helper(index + 1, n);
            visited[match[index][i]] = 0;
        }
    }
    int countArrangement(int n) {
        visited.resize(n + 1);
        match.resize(n + 1);

        // 预计算可放置的数值
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                if(j % i == 0 || i % j == 0){
                    match[i].push_back(j);
                }
            }
        }
        helper(1, n);
        return res;
    }
};
```