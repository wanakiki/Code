## 2469. 和有限的最长子序列

2023-04-01 11:36:14

### 题目

给你一个长度为 ``n`` 的整数数组 ``nums`` ，和一个长度为 ``m`` 的整数数组 ``queries`` 。

返回一个长度为 ``m`` 的数组<em>*``answer``<em>*，其中<em>*``answer[i]``<em>*是 ``nums`` 中<span style=""> </span>元素之和小于等于 ``queries[i]`` 的 **子序列** 的 **最大** 长度<span style=""> </span><span style=""> </span>。

**子序列** 是由一个数组删除某些元素（也可以不删除）但不改变剩余元素顺序得到的一个数组。



**示例 1：**

```

输入：nums = [4,5,2,1], queries = [3,10,21]
输出：[2,3,4]
解释：queries 对应的 answer 如下：
- 子序列 [2,1] 的和小于或等于 3 。可以证明满足题目要求的子序列的最大长度是 2 ，所以 answer[0] = 2 。
- 子序列 [4,5,1] 的和小于或等于 10 。可以证明满足题目要求的子序列的最大长度是 3 ，所以 answer[1] = 3 。
- 子序列 [4,5,2,1] 的和小于或等于 21 。可以证明满足题目要求的子序列的最大长度是 4 ，所以 answer[2] = 4 。
```

**示例 2：**

```

输入：nums = [2,3,4,5], queries = [1]
输出：[0]
解释：空子序列是唯一一个满足元素和小于或等于 1 的子序列，所以 answer[0] = 0 。```



**提示：**


- ``n == nums.length``
- ``m == queries.length``
- ``1 <= n, m <= 1000``
- ``1 <= nums[i], queries[i] <= 10<sup>6</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/longest-subsequence-with-limited-sum/)

### 思路及代码

一个容易被误导的题目，题目中强调的子序列需要保证剩余元素顺序不变对结果是没有影响的，实际上只需要从最小元素开始查找即可。

```cpp
class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        vector<int> res;

        for(auto q : queries){
            int cur = 0;
            int index = 0;
            while(cur < q && index < nums.size()){
                cur += nums[index];
                index++;
            }

            if(cur > q) index--;
            
            res.push_back(index);
        }
        return res;
    }
};
```


构建前缀和，之后二分查找：

```cpp
class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        for(int i = 1; i < nums.size(); i++){
            nums[i] += nums[i-1];
        }
        vector<int> res;
        for(auto q : queries){
            res.push_back(upper_bound(nums.begin(), nums.end(), q) - nums.begin());
        }
        return res;
    }
};
```