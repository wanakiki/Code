# Median of Two Sorted Arrays

2019年4月3日21点21分

高级二分法应用

## 题目

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be **O(log (m+n))**.

You may assume nums1 and nums2 cannot be both empty.

```
Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

## 分析

查找两个有序数组的中位数，要求对数复杂度。实际上看到对数复杂度的要求就很容易联想到二分法，但是如何将二分法应用到这种问题上是刚接触二分法的人比较难想到的点。（万能的二分法）

初次看到题目我也没有什么思路，看了网上的解答之后才写出了自己的代码，根据下面的代码很容易理清思路。重点在于两个数组元素比较的部分，要清楚只有相等的时候才找到了目的值，不等的情况都要继续讨论。另外个人感觉下面方法的复杂度应该不是$O(log (m+n))$

```cpp
class Solution {
public:
    double helper(vector<int>& nums1, int m_start, vector<int>& nums2, int n_start, int k){
        int m = nums1.size() - m_start, n = nums2.size() - n_start;
        if (m > n) return helper(nums2, n_start, nums1, m_start, k);    //常用处理方式，确保m始终小于等于n
        if(m == 0)  return nums2[k-1];                                  //查找完一个数组之后
        if(k == 1)  return min(nums1[m_start], nums2[n_start]);                     //递归基

        int pm, pn;
        pm = min(k/2, m);   //确保下标不会越界
        pn = k - pm;

        if(nums1[m_start + pm - 1] > nums2[n_start + pn - 1])
            return helper(nums1, m_start, nums2, n_start+pn, k - pn);
        else if (nums1[m_start + pm - 1] < nums2[n_start + pn - 1])
            return helper(nums1, m_start+pm, nums2, n_start, k - pm);
        else
            return nums1[pm-1];
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        int total = m + n;
        if(total & 1)
            return  helper(nums1, 0, nums2, 0, total/2+1);
        else
            return (helper(nums1, 0, nums2, 0, total/2) + helper(nums1, 0, nums2, 0, total/2+1)) / 2.0;
    }
};
```