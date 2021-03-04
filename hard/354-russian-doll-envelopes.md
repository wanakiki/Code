## 354. 俄罗斯套娃信封问题

2021-03-04 13:30:52

### 题目

给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 ``(w, h)`` 出现。当另一个信封的宽
度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。      

请计算最多能有多少个信封能组成一组&ldquo;俄罗斯套娃&rdquo;信封（即可以把一个信封放到另一
个信封里面）。

**说明:**

不允许旋转信封。

**示例:**

```
输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
```


[LeetCode链接](https://leetcode-cn.com/problems/russian-doll-envelopes/)

### 思路及代码

包裹的条件是宽和高均要大于被包裹的信封，可以先固定一维数据，在另外一个维度求最长的递增序列长度（[300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)）。假定我们对宽度w升序排序，则可以对h调用求最长递增子序列长度算法得到最大可包裹个数。这里，如果高度h是递增排序的话，统计个数时需要注意排除宽度相同的信封，但如果将h递减排序，则具有相同宽度的信封高度之间不能构成递增关系，可以直接调用300题中的算法。

```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        sort(envelopes.begin(), envelopes.end(), [](vector<int>& a, vector<int>& b){
            return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1]);
        });

        vector<int> dp(envelopes.size());
        int res = 0;
        for(int i = 0; i < envelopes.size(); i++){
            dp[i] = 1;
            for(int j = 0; j < i; j++){
                if(envelopes[i][1] > envelopes[j][1]){
                    dp[i] = max(dp[i], dp[j]+1);
                }
            }
            res = max(dp[i], res);
        }
        return res;
    }
};
```