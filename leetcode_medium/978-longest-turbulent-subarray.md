## 1020. 最长湍流子数组

2021-02-08 14:05:18

### 题目

当 ``A`` 的子数组 ``A[i], A[i+1], ..., A[j]`` 满足下列条件时，我们称其为<em>湍流子数组</em>：


- 若 ``i <= k < j``，当 ``k`` 为奇数时， ``A[k] > A[k+1]``，且当 ``k`` 为偶数时，``A[k] < A[k+1]``；
- **或**若 ``i <= k < j``，当 ``k`` 为偶数时，``A[k] > A[k+1]`` ，且当 ``k`` 为奇数时， ``A[k] < A[k+1]``。


也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 ``A`` 的最大湍流子数组的**长度**。

 

**示例 1：**

```
输入：[9,4,2,10,7,8,8,1,9]
输出：5
解释：(A[1] > A[2] < A[3] > A[4] < A[5])
```

**示例 2：**

```
输入：[4,8,12,16]
输出：2
```

**示例 3：**

```
输入：[100]
输出：1
```

 

**提示：**


- ``1 <= A.length <= 40000``
- ``0 <= A[i] <= 10^9``



[LeetCode链接](https://leetcode-cn.com/problems/longest-turbulent-subarray/)

### 思路及代码

直接按照湍流数组的定义在字符串中进行查找，查找过程中注意相邻两个元素相等时需要进行特殊判断。

```cpp
class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int len = arr.size();
        // 等于二时需要注意两个元素相等
        if(len < 2){
            return len;
        }

        int flag = 0;
        int cur_len = 1;
        int res = 1;
        for(int i = 1; i < len; i++){
            int cur_flag = 0;
            if(arr[i] > arr[i-1]){
                cur_flag = 1;
            }
            if(arr[i] < arr[i-1]){
                cur_flag = -1;
            }

            if(cur_flag == 0 || cur_flag == flag){
                res = max(res, cur_len);
                if(cur_flag != 0){
                    cur_len = 2;
                }
                else{
                    cur_len = 1;    // 当之前的符号是等号时 长度需要记为1
                }
                cout << i << ' ' << res << endl;
            }
            else{
                cur_len++;
            }
            flag = cur_flag;
        }
        return max(res, cur_len);
    }
};
```

上面的代码是按照规则硬写出来的，逻辑感觉不是很清晰，下面这段代是看到提交记录里执行速度较快的，思路也很清晰，应该是对dp进行优化得到的。

```cpp
class Solution {
public:
    int maxTurbulenceSize(vector<int>& A) {
        vector<int> dp(2,1);
        int ans = 1;
        for(int i = 1; i < A.size(); ++i){
            if(A[i] > A[i-1]){
                dp[0] = dp[1] + 1;
                dp[1] = 1;
            }else if(A[i] < A[i-1]){
                dp[1] = dp[0] + 1;
                dp[0] = 1;
            }else{
                dp[0] = 1;
                dp[1] = 1;
                continue;
            }
            ans = max(ans, max(dp[1], dp[0]));
        }
        return ans;
    }
};
```