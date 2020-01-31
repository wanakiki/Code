## 643. 子数组最大平均数 I

2020年1月31日

### 题目

给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:
```no
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
```

注意:
1. 1 <= k <= n <= 30,000。
2. 所给数据范围 [-10,000，10,000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subarray-i

### 分析

这道题没有特别有效的方法，按照滑动窗口的思维，直接遍历整个数组，期间更新最大的窗口数值，最后用最大的窗口值计算平均数即可。

需要注意的是，更新条件为窗口和，不能为右侧变量大于左侧变量。在这种情况下，可能存在先减后增导致出错，例如``[0,4,0,3,0],1``这个例子，在用右侧变量和左侧变量相比判断是否更新时，最后的最大的窗口值为3，得到了错误的结果。

### 代码

```cpp
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int sum = 0;
        for(int i = 0; i < k; i++){
            sum += nums[i];
        }
        int max = sum;  //k与n相等时 只有一种方案
        for(int i = k; i < nums.size(); i++){
            int tmp = nums[i] - nums[i - k];
            sum += tmp;
            if(sum > max)
                max = sum;
        }
        return max/double(k);
    }
};
```

另一种写法，复杂度相同，提交时多运行了8ms。
```cpp
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int sum = 0;
        for(int i = 0; i < k; i++){
            sum += nums[i];
        }
        int max = sum;  //k与n相等时 只有一种方案
        int l = 0, r = 0;
        for(int i = k; i < nums.size(); i++){
            l += nums[i - k];
            r += nums[i];
            if(r > l){
                max = max + r - l;
                l = r = 0;
            }
        }
        return max/double(k);
    }
};
```
