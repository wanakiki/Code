## 448. 找到所有数组中消失的数字

2021-02-13 16:06:35

### 题目

给定一个范围在  1 < a[i] < n (n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为<em>O(n)</em>的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

**示例:**

```
输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
```


[LeetCode链接](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/)

### 思路及代码

数组中元素的可能取值不会超过n，所以可以用该位置数值加n的操作对数据出现次数进行统计。

```cpp
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        int n = nums.size();
        for(int i = 0; i < nums.size(); i++){
            int x = (nums[i] - 1) % n;  // 避免索引为负值
            nums[x] += n;
        }
        for(int i = 0; i < n; i++){
            if(nums[i] <= n){
                res.push_back(i + 1);
            }
        }
        return res;
    }
};
```