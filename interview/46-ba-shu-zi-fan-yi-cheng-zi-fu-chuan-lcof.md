## 面试题46. 把数字翻译成字符串

2020年6月9日

### 题目

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 &ldquo;a&rdquo; ，1 翻译成 &ldquo;b&rdquo;，&hellip;&hellip;，11 翻译成 &ldquo;l&rdquo;，&hellip;&hellip;，25 翻译成 &ldquo;z&rdquo;。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

**示例 1:**

```
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
```

 

**提示：**


- ``0 <= num < 2^31``


### 代码

数字对应的字符串第i位的翻译种数有下面两种情况：

- 作为单独的一位出现，可能翻译情况和上一位的可能情况数相同
- 若能够和上一位组成10-25的数字，则当前位的可能翻译种数就是i-1位和i-2位的累加

按照上面的递推关系，不难写出下面的动态规划代码：

```cpp
class Solution {
public:
    int translateNum(int num) {
        string nums = to_string(num);
        nums = '3' + nums;  // 制造空头 方便处理
        vector<int> dp(nums.size(), 1);

        for(int i = 1; i < nums.size(); i++){
            if(nums[i - 1] == '1'){
                dp[i] = dp[i - 1] + dp[i - 2];
            }
            else if(nums[i - 1] == '2' && nums[i] < '6'){
                dp[i] = dp[i - 1] + dp[i - 2];
            }
            else{
                dp[i] = dp[i - 1];
            }
        }

        return dp[nums.size() - 1];
    }
};
```

仔细观察，dp数组不是必须的，需要记住的量只有三个，可以用滚动数组的方式对上面的动态规划代码进行进一步优化。


