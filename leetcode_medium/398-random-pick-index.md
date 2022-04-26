## 398. 随机数索引

2022-04-25 14:14:41

### 题目

给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

**注意：**

数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

**示例:**

```
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);

// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);
```


[LeetCode链接](https://leetcode-cn.com/problems/random-pick-index/)

### 思路及代码

哈希表搭配数组，占用 O(n) 空间。

```cpp
class Solution {
public:
    unordered_map<int, vector<int>> hash;
    Solution(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++){
            hash[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        int len = hash[target].size();
        return hash[target][rand() % len];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
```

水塘抽样法，占用 O(1) 空间。

该方法的好处是，如果输入数据的量特别大，在随机选择元素时不需要将全部元素加载进内存。只需要顺序加载元素，并统计已经遇到 target 的次数，根据 ``rand() % count`` 的值是否为零决定是否更换当前索引为最终结果。可按照如下方式推导出保留每个索引的概率相同：

假设目标元素共有 k 个，则恰好保存第 i 个元素对应索引的概率是：

$$\frac{1}{i} \cdot \frac{i}{i+1} \cdot \frac{i+1}{i+2} \dots \frac{k-1}{k} = \frac{1}{k}$$

```cpp
class Solution {
public:
    unordered_map<int, vector<int>> hash;
    Solution(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++){
            hash[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        int len = hash[target].size();
        return hash[target][rand() % len];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
```