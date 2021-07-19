## 1966. 最高频元素的频数

2021-07-19 21:49:48

### 题目

元素的 **频数** 是该元素在一个数组中出现的次数。

给你一个整数数组 ``nums`` 和一个整数 ``k`` 。在一步操作中，你可以选择 ``nums`` 的一个下标，并将该下标对应元素的值增加 ``1`` 。

执行最多 ``k`` 次操作后，返回数组中最高频元素的 **最大可能频数**。

 

**示例 1：**

```
输入：nums = [1,2,4], k = 5
输出：3
解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
4 是数组中最高频元素，频数是 3 。
```

**示例 2：**

```
输入：nums = [1,4,8,13], k = 5
输出：2
解释：存在多种最优解决方案：
- 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
- 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
- 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
```

**示例 3：**

```
输入：nums = [3,9,6], k = 2
输出：1
```

 

**提示：**


- ``1 <= nums.length <= 10<sup>5</sup>``
- ``1 <= nums[i] <= 10<sup>5</sup>``
- ``1 <= k <= 10<sup>5</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element/)

### 思路及代码

看到题目之后没有思路，查看题解之后才意识到可以用滑动窗来解决。

```cpp
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int res = 0;    // 数组中最小值为1
        sort(nums.begin(), nums.end());
        int left = 0, right = 0;

        // 滑动窗口  计算将窗口内所有数据更改为右侧数据需要的操作次数
        long long total = 0;    // 总操作次数 len(nums) * (max(nums) - min(nums)) 可能导致整形越界
        while(right < nums.size()){
            if(right > left){
                total += (long long)(right - left) * (nums[right] - nums[right - 1]);
            }
            
            // 当操作次数大于k之后移动左边界
            while(total > k){
                total -= nums[right] - nums[left];
                left++;     // 此处极限情况为left与right重合
            }

            res = max(res, right - left + 1);
            right++;
        }
        return res;
    }
};
```