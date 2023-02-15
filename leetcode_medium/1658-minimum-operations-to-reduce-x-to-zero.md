## 1658. 将 x 减到 0 的最小操作数

2023-01-07 12:44:53

### 题目

给你一个整数数组 ``nums`` 和一个整数 ``x`` 。每一次操作时，你应当移除数组 ``nums`` 最左边或最右边的元素，然后从 ``x`` 中减去该元素的值。请注意，需要 **修改** 数组以供接下来的操作使用。

如果可以将 ``x`` **恰好** 减到 ``0`` ，返回**最小操作数**；否则，返回 ``-1`` 。

 

**示例 1：**

```

输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
```

**示例 2：**

```

输入：nums = [5,6,7,8,9], x = 4
输出：-1
```

**示例 3：**

```

输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
```

 

**提示：**


- ``1 <= nums.length <= 10<sup>5</sup>``
- ``1 <= nums[i] <= 10<sup>4</sup>``
- ``1 <= x <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero/)

### 思路及代码

题目等价于找到数组中和为目标值且长度最大的连续子数组，可以使用前缀和，枚举连续子数组的左边界，用二分法查找右边界。

```cpp
class Solution {
   public:
    int minOperations(vector<int>& nums, int x) {
        vector<long long> pre(nums.size(), 0);
        pre[0] = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            pre[i] = pre[i - 1] + nums[i];
        }

        long long global_target = pre[pre.size() - 1] - x;
        if(global_target == 0)  return pre.size();      // 所有数字都需要被删除，直接返回
        
        // 找到和为目标值的最长数组
        int res = -1;
        cout << endl;
        for (int i = 0; i < pre.size(); i++) {
            long long cur_target = global_target;
            if (i != 0) cur_target += pre[i - 1];

            // 二分查找
            int left = i;
            int right = pre.size() - 1;
            while (left < right) {
                int mid = left + (right - left + 1) / 2;
                if (pre[mid] == cur_target) {
                    left = mid;
                } else if (pre[mid] > cur_target) {
                    right = mid - 1;
                } else {
                    left = mid;
                }
            }

            if (left < pre.size() && pre[left] == cur_target) {
                res = max(res, left - i + 1);
            }
        }

        if (res == -1)
            return res;
        else
            return pre.size() - res;
    }
};
```

超时的回溯做法：

```cpp
class Solution {
public:
    unordered_map<long long, int> hash;
    int helper(vector<int>& nums, int left, int right, int x){
        if(x < 0)   return INT_MAX;
        else if(x == 0) return 0;

        if(left > right)   return INT_MAX;


        int index = left * 1000000 + right;
        if(hash.find(index) == hash.end()){
            int res = min(helper(nums, left + 1, right, x - nums[left]), helper(nums, left, right - 1, x - nums[right]));
            if(res != INT_MAX)  res += 1;
            hash[index] = res;
        }

        // cout << index << ' ' << hash[index] << endl;
        return hash[index];
    }
    int minOperations(vector<int>& nums, int x) {
        int res = helper(nums, 0, nums.size() - 1, x);
        if(res == INT_MAX)  return -1;
        else    return res;
    }
};
```