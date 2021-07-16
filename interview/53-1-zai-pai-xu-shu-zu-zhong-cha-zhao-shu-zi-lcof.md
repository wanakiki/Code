## 100329. 在排序数组中查找数字 I   

2021-07-16 18:31:05

### 题目

统计一个数字在排序数组中出现的次数。



**示例 1:**

```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```

**示例 2:**

```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```



**限制：**

``0 <= 数组长度 <= 50000``



**注意：** 本题与主站 34 题相同（仅返回值不同）：<a href="https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/">https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/</a>


[LeetCode链接](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

### 思路及代码

普通方法直接遍历数组统计：

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int count = 0;
        for(auto n : nums){
            if(target == n){
                count++;
            }
        }
        return count;
    }
};
```

二分法查找第一个起始位置，之后统计连续相同数据长度。

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        // 二分法查找大于等于目标值的第一个元素
        int left = 0, right = nums.size() - 1;
        while(left < right){
            int mid = left + (right - left) / 2;
            if(nums[mid] > target){
                right = mid;
            }
            else if(nums[mid] == target){
                right = mid;
            }
            else{
                left = mid + 1;     // 若当前元素小于目标值，则当前元素必不在查找范围内
            }
        }

        int count = 0;
        while(left < nums.size() && nums[left] == target){
            count++;
            left++;
        }
        return count;
    }
};
```

二分法查找两个边界，通过减法计算个数。

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        // 二分法查找大于等于目标值的第一个元素
        int left = 0, right = nums.size();
        int real_left = 0, real_right = 0;
        while(left < right){
            int mid = left + (right - left) / 2;
            if(nums[mid] > target){
                right = mid;
            }
            else if(nums[mid] == target){
                right = mid;
            }
            else{
                left = mid + 1;     // 若当前元素小于目标值，则当前元素必不在查找范围内
            }
        }
        real_left = left;

        // 二分法查找大于目标值的第一个元素
        left = 0;
        right = nums.size();
        while(left < right){
            int mid = left + (right - left) / 2;
            if(nums[mid] <= target){
                left = mid + 1;
            }
            else{
                right = mid;
            }
        }
        real_right = right;
        return real_right - real_left;
    }
};
```