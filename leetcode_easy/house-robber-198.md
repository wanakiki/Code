## 198. House Robber
##### 2018-06-05 12:39:29
##### 动态规划
***
## 题目
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```
Example 2:
```
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```
## 分析
简单的动态规划题目，因为只需要得到最大的数，也可以只用两个变量来处理，不需要对数组进行多次操作，不过个人不太熟练，还是选择了相对麻烦的写法。
## 示例代码
```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int len=nums.size();
        if(len== 0)
            return 0;
        if(len == 1)
            return nums[0];
        for(int i=2;i<len;i++){
            if(i==2){
                nums[2]+=nums[0];
                continue;
            }
            nums[i]+= max(nums[i-2],nums[i-3]);
        }
        return max(nums[len-1],nums[len-2]);
    }
};
```

dp[i] = max(dp[i-1], dp[i-1]+nums[i])

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0)    return 0;
        int a = 0, b = nums[0];
        for(int i = 1; i < nums.size(); i++){
            int tmp = max(a + nums[i], b);
            a = b;
            b = tmp;
        }
        return b;
    }
};
```