## 179. 最大数

2021-04-12 20:49:54

### 题目

给定一组非负整数 ``nums``，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

**注意：** 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

 

**示例 1：**

```
输入：nums = [10,2]
输出："210"
```

**示例 2：**

```
输入：nums = [3,30,34,5,9]
输出："9534330"
```

**示例 3：**

```
输入：nums = [1]
输出："1"
```

**示例 4：**

```
输入：nums = [10]
输出："10"
```

 

**提示：**


- ``1 <= nums.length <= 100``
- ``0 <= nums[i] <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/largest-number/)

### 思路及代码

三年之前错了好几次才交上这个题，今天做到了还是没能快速想到合适的比较方法。

```cpp
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](const int& x, const int& y){
            long sx = 10, sy = 10;
            while(sx <= x){
                sx *= 10;
            }
            while(sy <= y){
                sy *= 10;
            }
            return sy * x + y > sx * y + x;
        });

        // 存在多个零需要提前处理
        if(nums[0] == 0){
            return "0";
        }
        string res;
        for(auto x : nums){
            res += to_string(x);
        }
        return res;
    }
};
```

除了上面计算x、y位数的方法，也可以转化为字符串类型拼接后比较哪个更大。