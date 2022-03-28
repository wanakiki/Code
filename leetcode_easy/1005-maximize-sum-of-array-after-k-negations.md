## 1047. K 次取反后最大化的数组和

2021-12-03 09:52:28

### 题目

给你一个整数数组 ``nums`` 和一个整数 ``k`` ，按以下方法修改该数组：


- 选择某个下标 ``i`` 并将 ``nums[i]`` 替换为 ``-nums[i]`` 。


重复这个过程恰好 ``k`` 次。可以多次选择同一个下标 ``i`` 。

以这种方式修改数组后，返回数组 **可能的最大和** 。



**示例 1：**

```
输入：nums = [4,2,3], k = 1
输出：5
解释：选择下标 1 ，nums 变为 [4,-2,3] 。
```

**示例 2：**

```
输入：nums = [3,-1,0,2], k = 3
输出：6
解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
```

**示例 3：**

```
输入：nums = [2,-3,-1,5,-4], k = 2
输出：13
解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
```



**提示：**


- ``1 <= nums.length <= 10<sup>4</sup>``
- ``-100 <= nums[i] <= 100``
- ``1 <= k <= 10<sup>4</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/)

### 思路及代码

对数组排序，统计原始数组中负数的个数，根据负数与k的大小关系进行判断，尽量将绝对值大的负数转为正数。如果k大于负数的个数，应多次对一个元素进行取反操作，如果模2为1则代表需要对数组中的最小元素进行取反（k大于负数个数时已提前对所有负数进行了取反）。

```cpp
class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int count = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] >= 0)    break;
            count++;
        }

        // 负数个数大于等于k 从绝对值大的开始取反
        // 负数个数小于k 全部取反后 判断k-count模2是否有值 如果有值则再取反第一个
        // 注意绝对值大的数在左侧
        if(count >= k){
            int index = 0;
            while(k){
                nums[index] = -nums[index];
                index++;
                k--;
            }
        }
        else{
            int left = k - count;
            for(int i = 0; i < count; i++){
                nums[i] = -nums[i];
            }

            // 将数组中绝对值最小的数字翻转
            if(left % 2 != 0){
                sort(nums.begin(), nums.end());
            nums[0] = -nums[0];
            }
            
        }

        int res = 0;
        for(auto n : nums){
            res += n;
        }
        return res;
    }
};
```

上面的代码实现起来还需要加一些特殊情况的判断，在题解区看到了使用最小堆的做法，实现起来会让代码简洁不少。