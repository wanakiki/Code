## 628. 三个数的最大乘积

2021-01-20 13:25:44

### 题目

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

**示例 1:**

```
输入: [1,2,3]
输出: 6
```

**示例 2:**

```
输入: [1,2,3,4]
输出: 24
```

**注意:**


- 给定的整型数组长度范围是[3,10<sup>4</sup>]，数组中所有的元素范围是[-1000, 1000]。
- 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。



### 思路及代码

可以直接对数组进行排序，取最大的三个数乘积或者最大的一个数与最小的两个数乘积中较大的一个作为结果。

下面的代码用了类似于求三数之和题目的思路，遍历一次数组，计算出两个数乘积每个位置可能的两个数乘积的最大值和最小值，之后再遍历一次数组，保留最大的乘积。因为进行了很多不必要的计算，执行起来会稍微慢一点。

```cpp
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int len = nums.size();
        vector<vector<int>> two_nums(len, vector<int>(2));
        int cur_min = nums[0], cur_max = nums[0];
        two_nums[0][0] = INT_MAX;
        two_nums[0][1] = INT_MIN;
        for(int i = 1; i < len; i++){
            int tmp_min, tmp_max;
            tmp_min = nums[i] * cur_max;
            tmp_max = nums[i] * cur_min;
            int rel_min = min(tmp_max, tmp_min);
            int rel_max = max(tmp_max, tmp_min);

            two_nums[i][0] = min(two_nums[i-1][0], rel_min);
            two_nums[i][1] = max(two_nums[i-1][1], rel_max);

            cur_min = min(cur_min, nums[i]);
            cur_max = max(cur_max, nums[i]);
        }
        for(auto i : two_nums){
            cout << i[0] << ' ' << i[1] << endl;
        }
        int res = INT_MIN;
        for(int i = 2; i < len; i++){
            int a = nums[i] * two_nums[i-1][0];
            int b = nums[i] * two_nums[i-1][1];
            int tmp = max(a, b);
            res = max(res, tmp);
        }
        return res;
    }
};
```