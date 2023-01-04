## 1802. 有界数组中指定下标处的最大值

2023-01-04 11:06:12

### 题目

给你三个正整数 ``n``、``index`` 和 ``maxSum`` 。你需要构造一个同时满足下述所有条件的数组 ``nums``（下标 **从 0 开始** 计数）：


- ``nums.length == n``
- ``nums[i]`` 是 **正整数** ，其中 ``0 <= i < n``
- ``abs(nums[i] - nums[i+1]) <= 1`` ，其中 ``0 <= i < n-1``
- ``nums`` 中所有元素之和不超过 ``maxSum``
- ``nums[index]`` 的值被 **最大化**


返回你所构造的数组中的 ``nums[index]`` 。

注意：``abs(x)`` 等于 ``x`` 的前提是 ``x >= 0`` ；否则，``abs(x)`` 等于 ``-x`` 。

 

**示例 1：**

```
输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
```

**示例 2：**

```
输入：n = 6, index = 1,  maxSum = 10
输出：3
```

 

**提示：**


- ``1 <= n <= maxSum <= 10<sup>9</sup>``
- ``0 <= index < n``



[LeetCode链接](https://leetcode-cn.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/)

### 思路及代码

题目整体不难，边界处理比较麻烦。看到题目之后进行分析，在 index 处取到最大数值且数组元素和最小的情况对应数组从 index 处向两侧递减。因此可以递增 index 处数值，计算对应的数组和看其是否小于 maxSum。需要注意的是，由于数组边界的存在，两侧数据并不是一定递减到1。

下面是模拟整个搜索过程的代码，在数据较为极端的情况下会超时。

```cpp
class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        int max_left = index;
        int max_right = n - (index + 1);
        int cur_left = 0;
        int cur_right = 0;

        int cur_val = 1;
        int sum_left = maxSum -  n; // 初始全为1
        
        while(1){
            int new_val = 1 + cur_left + cur_right;
            if(new_val <= sum_left){
                cur_val ++;
                sum_left -= new_val;

                if(cur_left < max_left) cur_left++;
                if(cur_right < max_right)   cur_right++;
            }
            else{
                break;
            }
        }
        return cur_val;
    }
};
```

上述做法超时后，考虑到伴随 index 处数值递增的同时，数组元素和也是递增的，可以使用二分法加速这一搜索过程。

```cpp
class Solution {
public:
    long long calArray(int len, long long max_val){
        // 计算单调序列的和
        return len * (max_val + (max_val + 1 - len)) / 2;
    }
    long long calSum(int n, int index, int val){
        if(val == 1)    return n;
        if(val == 2)    return n + 1;


        // 根据当前index数值计算数组元素和
        int max_left = index;
        int max_right = n - (index + 1);

        int cur_left = min(max_left, val - 1);
        int cur_right = min(max_right, val - 1);

        long long  sum_val = val + calArray(cur_left, val - 1) + calArray(cur_right, val - 1);
        // 判断是否有多余的1
        int cur_len = cur_left + cur_right + 1; // 当前被计算的长度
        if(cur_len < n){
            sum_val += n - cur_len;
        }
        return sum_val;
    }

    int maxValue(int n, int index, int maxSum) {
        int max_value = maxSum;
        int min_value = 1;

        while(min_value < max_value){
            int mid = min_value + (max_value - min_value + 1) / 2;

            long long  cur_sum = calSum(n, index, mid);
            if(cur_sum > maxSum){
                max_value = mid - 1;
            }
            else{
                min_value = mid;
            }
        }
        return min_value;
    }
};
```