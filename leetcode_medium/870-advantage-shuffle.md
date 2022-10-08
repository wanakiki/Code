## 870. 优势洗牌

2022-10-08 16:58:49

### 题目

给定两个大小相等的数组 ``nums1`` 和 ``nums2``，``nums1`` 相对于 ``nums2`` 的<em>优势</em>可以用满足 ``nums1[i] > nums2[i]`` 的索引 ``i`` 的数目来描述。   

返回 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace" size="1"><span style="background-color: rgb(249, 242, 244);">nums1</span></font> 的**任意**排列，使其相对于 ``nums2`` 的优势最大化。



**示例 1：**

```
输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
输出：[2,11,7,15]
```

**示例 2：**

```
输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
输出：[24,32,8,12]
```



**提示：**


- ``1 <= nums1.length <= 10<sup>5</sup>``
- ``nums2.length == nums1.length``
- ``0 <= nums1[i], nums2[i] <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/advantage-shuffle/)

### 思路及代码


```cpp
class Solution {
public:
    vector<int> advantageCount(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        multiset<int> myset;

        for(auto n : nums1){
            myset.insert(n);
        }

        for(auto n : nums2){
            auto it = myset.upper_bound(n);
            if(it == myset.end()){
                res.push_back(*myset.begin());
                myset.erase(myset.begin());
            }
            else{
                res.push_back(*it);
                myset.erase(it);
            }
        }
        return res;
    }
};
```