## 926. 将字符串翻转到单调递增

2022-06-11 08:52:38

### 题目

如果一个二进制字符串，是以一些 ``0``（可能没有 ``0``）后面跟着一些 ``1``（也可能没有 ``1``）的形式组成的，那么该字符串是 **单调递增** 的。

给你一个二进制字符串 ``s``，你可以将任何 ``0`` 翻转为 ``1`` 或者将 ``1`` 翻转为 ``0`` 。

返回使 ``s`` 单调递增的最小翻转次数。



**示例 1：**

```
输入：s = "00110"
输出：1
解释：翻转最后一位得到 00111.
```

**示例 2：**

```
输入：s = "010110"
输出：2
解释：翻转得到 011111，或者是 000111。
```

**示例 3：**

```
输入：s = "00011000"
输出：2
解释：翻转得到 00000000。
```



**提示：**


- ``1 <= s.length <= 10<sup>5</sup>``
- ``s[i]`` 为 ``'0'`` 或 ``'1'``



[LeetCode链接](https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/)

### 思路及代码

采用动态规划思路，找到使某个位置左侧全为0和右侧全为1的最小翻转次数。

```cpp
class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int n = s.size();
        vector<int> dp_left(n, 0);
        vector<int> dp_right(n, 0);

        int count = 0;
        for(int i = 0; i < n; i++){
            if(s[i] == '1'){
                count++;
            }
            dp_left[i] = count;
        }

        count = 0;
        for(int i = n - 1; i >= 0; i--){
            if(s[i] == '0'){
                count++;
            }
            dp_right[i] = count;
        }

        int res = INT_MAX;
        for(int i = 0; i < n-1; i++){
            res = min(res, dp_left[i] + dp_right[i+1]);
        }
        
        // 边界
        res = min(res, dp_left[n - 1]);
        res = min(res, dp_right[0]);
        return res;
    }
};
```