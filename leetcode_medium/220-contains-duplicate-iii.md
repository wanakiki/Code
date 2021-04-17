## 220. 存在重复元素 III

2021-04-17 10:44:47

### 题目

给你一个整数数组 ``nums`` 和两个整数 ``k`` 和 ``t`` 。请你判断是否存在 <b>两个不同下标</b> ``i`` 和 ``j``，使得 ``abs(nums[i] - nums[j]) <= t`` ，同时又满足 ``abs(i - j) <= k``。

如果存在则返回 ``true``，不存在返回 ``false``。

 

**示例 1：**

```
输入：nums = [1,2,3,1], k = 3, t = 0
输出：true
```

**示例 2：**

```
输入：nums = [1,0,1,1], k = 1, t = 2
输出：true
```

**示例 3：**

```
输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false
```

 

**提示：**


- ``0 <= nums.length <= 2 * 10<sup>4</sup>``
- ``-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1``
- ``0 <= k <= 10<sup>4</sup>``
- ``0 <= t <= 2<sup>31</sup> - 1``



[LeetCode链接](https://leetcode-cn.com/problems/contains-duplicate-iii/)

### 思路及代码

最开始看错了题目，以为是``abs(nums[i] - nums[j]) = t``，写了下面的代码：

```cpp
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if(k == 0)  return false;   // 一个数不满足条件

        unordered_map<int,int> hash;
        int left = 0, right = 0;
        // k += 1;
        int len = 0;
        hash[nums[left] + t] = 1;
        hash[nums[left] - t] = 1;

        
        // 判断当前长度是否越界 窗满则调整左边界
        // 判断新增元素是否可以与之前元素满足要求
        // 若不满足要求添加新元素
        for(right = left + 1; right < nums.size(); right++){
            if(len >= k){
                hash.erase(nums[left] + t);
                hash.erase(nums[left] - t);
                len -= 1;
            }

            if(hash.find(nums[right]) != hash.end()){
                return true;
            }
            else{
                hash[nums[right] + t] = 1;
                hash[nums[right] - t] = 1;
                len += 1;
            }
        }
        return false;
    }
};
```

但实际上应该对滑动窗内值的区间进行查找，之前基本没有做过区间查找的题目，想了一段时间没有想到解法，最后还是求助了题解。题解给我印象最深的地方是``lower_bound``函数的使用，这个函数只在课上见过自己的程序里很少去用。

因为要查找滑动窗口内的值是否有在``[nums[i] - t, nums[i] + t]``区间内，为了方便查找，数据结构应该是有序的，考虑到窗口滑动后会抛弃左侧的值，所以要求数据结构支持删除指定元素。

因此set是一个比较好的选择，set本身不允许重复，但在本题目条件下，如果存在重复元素则可以直接返回结果，故不需要考虑。

另外一点是查找区间可能存在越界情况，需要特殊处理。

```cpp
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if(k == 0)  return false;

        set<int> s;
        int len = 0;
        int left = 0;
        for(int i = 0; i < nums.size(); i++){
            if(len > k){
                s.erase(nums[left]);
                left++;
                len -= 1;
            }

            auto it = s.lower_bound(max(nums[i], INT_MIN + t) - t);
            if(it != s.end() && *it <= min(nums[i], INT_MAX - t) + t){
                return true;
            }
            else{
                s.insert(nums[i]);
                len += 1;
            }
        }
        return false;
    }
};
```

实际上不需要额外的变量来统计窗口长度，当索引大于等于k后，每次都要删除左侧元素。

另外一种方法是桶排序，令 $x = (t + 1) \times a + b(0 \leq b \leq t)$，则代表x位于编号为a的桶，这样需要检查a及其左右两侧的桶是否有其它元素即可判断是否有满足要求的数。