## 819. 使序列递增的最小交换次数

2022-10-10 17:08:14

### 题目

我们有两个长度相等且不为空的整型数组 ``nums1`` 和 ``nums2`` 。在一次操作中，我们可以交换 ``nums1[i]`` 和 ``nums2[i]``的元素。


- 例如，如果 ``nums1 = [1,2,3,<u>8</u>]`` ， ``nums2 =[5,6,7,<u>4</u>]`` ，你可以交换 ``i = 3`` 处的元素，得到 ``nums1 =[1,2,3,4]`` 和 ``nums2 =[5,6,7,8]`` 。


返回*使 ``nums1`` 和 ``nums2`` **严格递增**所需操作的最小次数。

数组 ``arr`` **严格递增** 且  ``arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1]`` 。

注意：


- 用例保证可以实现操作。




**示例 1:**

```
输入: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
输出: 1
解释:
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。
```

**示例 2:**

```
输入: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
输出: 1
```



**提示:**


- ``2 <= nums1.length <= 10<sup>5</sup>``
- ``nums2.length == nums1.length``
- ``0 <= nums1[i], nums2[i] <= 2 * 10<sup>5</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing/)

### 思路及代码

题目确保可以通过交换生成递增数组，且交换只发生在相同的索引上。则对于每个索引i，至少满足以下两个条件中的一个： $$ nums1[i] > nums1[i]-1 \quad \& \quad  nums2[i] > nums2[i-1] $$ $$ nums1[i] > nums2[i-1] \quad \& \quad nums2[i] > nums1[i-1] $$

采用动态规划进行解题，dp[i][0] 代表不交换，dp[i][1] 代表交换，如果同时满足两个条件则根据 dp[i-1] 中的较小值进行更新。如果只满足1则根据相同的位置进行更新，满足2则根据相反的位置更新。

```cpp
class Solution {
public:
    int minSwap(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> dp(nums1.size(), vector<int>(2, 0));
        dp[0][0] = 0;
        dp[0][1] = 1;
        for(int i = 1; i < nums1.size(); i++){
            bool flag1 = nums1[i] > nums1[i-1] && nums2[i] > nums2[i-1];
            bool flag2 = nums1[i] > nums2[i-1] && nums2[i] > nums1[i-1];

            if(flag1 == true && flag2 == false){
                dp[i][0] = dp[i-1][0];
                dp[i][1] = dp[i-1][1] + 1;
            }
            else if(flag1 == false && flag2 == true){
                dp[i][0] = dp[i-1][1];
                dp[i][1] = dp[i-1][0] + 1;
            }
            else{
                dp[i][0] = min(dp[i-1][0], dp[i-1][1]);
                dp[i][1] = dp[i][0] + 1;
            }
        }
        int n = nums1.size() - 1;
        return min(dp[n][0], dp[n][1]);
    }
};
```