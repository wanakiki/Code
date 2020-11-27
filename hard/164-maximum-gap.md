## 164. 最大间距

2020-11-27 21:53:50

### 题目

给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

**示例 1:**

```
输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
```

**示例 2:**

```
输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
```

**说明:**


- 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
- 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。



### 思路及代码

这是一个我个人感觉很不错的困难题目，代码实现并不复杂，用到的算法也谈不上复杂，但是比较难想到。看到题目自然的想法是排序后遍历，但是这并不满足线性时间空间复杂度的要求。

但想要了解到排序之后相邻元素之间的最大差值，排序的步骤又是不可避免地，这时候就可以考虑平时不怎么用到的基数排序和桶排序。下面是我用桶排序思路实现的代码，用的不是很熟练，需要对桶内尺寸和总个数的具体计算规则进行确定。

不考虑相同元素时，数组中相邻数字的最小间隔应该是 ``int((max - min) / len) + 1)，照此确定桶的尺寸。

```cpp
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int res = 0;
        int min_num = INT_MAX;
        int max_num = INT_MIN;
        int len = nums.size();
        for(int i = 0; i < nums.size(); i++){
            min_num = min_num < nums[i] ? min_num : nums[i];
            max_num = max_num > nums[i] ? max_num : nums[i];
        }
        if(max_num == min_num || nums.size() < 2){
            return 0;
        }

        int bucket_size = (max_num - min_num) / len + 1;
        int bucket_len = max_num / bucket_size + 1;
        vector<pair<int, int>> buckets(bucket_len, make_pair(-1, -1));
        for(int i = 0; i < nums.size(); i++){
            int cur = get_index(bucket_size, nums[i]);
            if(buckets[cur].first == -1){
                buckets[cur].first = nums[i];
            }
            else{
                buckets[cur].first = min(buckets[cur].first, nums[i]);
            }
            buckets[cur].second = max(buckets[cur].second, nums[i]);
        }

        int start = -1;
        for(int i = 0; i < buckets.size(); i++){
            if(buckets[i].first == -1){
                continue;
            }
            int diff = buckets[i].second - buckets[i].first;    // 桶内差值
            res = max(res, diff);
            if(start == -1){
                start = buckets[i].second;
            }
            else{
                int tmp = buckets[i].first - start;
                res = max(res, tmp);
                start = buckets[i].second;
            }
        }
        return res;
    }
    int get_index(int bucket_size, int i){
        return i / bucket_size;
    }
};
```