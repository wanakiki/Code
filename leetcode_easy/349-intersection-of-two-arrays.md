## 349. 两个数组的交集

2020年11月2日

### 题目

给你一个整数数组 ``arr``，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 ``true``；否则返回 ``false``。



**示例 1：**

```
输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数
的出现次数相同。```

**示例 2：**

```
输入：arr = [1,2]
输出：false
```

**示例 3：**

```
输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
输出：true
```



**提示：**


- ``1 <= arr.length <= 1000``
- ``-1000 <= arr[i] <= 1000``

### 思路及代码

遍历第一个数组，用哈希表存储发现的数字，之后遍历第二个数组，在哈希表中查看该元素是否出现过。由于返回的结果数组不能出现重复的数字，所以在查找到当前元素之和需要把哈希表内的值进行修改。

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> hash;
        vector<int> res;
        for(int i = 0; i < nums1.size(); i++){
            hash[nums1[i]] = 1;
        }
        for(int i = 0; i < nums2.size(); i++){
            if(hash.find(nums2[i]) != hash.end() && hash[nums2[i]] != 0){
                res.push_back(nums2[i]);
                hash[nums2[i]] = 0;
            }
        }
        return res;
    }
};
```