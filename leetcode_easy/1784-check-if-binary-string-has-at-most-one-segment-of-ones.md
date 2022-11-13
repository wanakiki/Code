## 1784. 检查二进制字符串字段

2022-10-03 19:01:11

### 题目

给你一个二进制字符串 ``s`` ，该字符串 **不含前导零** 。

如果 ``s`` 包含 **零个或一个由连续的 ``'1'`` 组成的字段** ，返回 ``true``​​​ 。否则，返回 ``false`` 
。

如果 ``s`` 中 **由连续若干个 ``'1'`` 组成的字段** 数量不超过 ``1``，返回 ``true``​​​ 。否则，返回 ``false`` 。



**示例 1：**

```
输入：s = "1001"
输出：false
解释：由连续若干个 '1' 组成的字段数量为 2，返回 false
```

**示例 2：**

```
输入：s = "110"
输出：true
```



**提示：**


- ``1 <= s.length <= 100``
- ``s[i]``​​​​ 为 ``'0'`` 或 ``'1'``
- ``s[0]`` 为 ``'1'``



[LeetCode链接](https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/)

### 思路及代码

统计连续1出现的次数，如果超过一次则返回false。

```cpp
class Solution {
public:
    bool checkOnesSegment(string s) {
        int count = 0;
        if(s[0] == '1') count++;
        
        for(int i = 1; i < s.size(); i++){
            if(s[i] == '1' && s[i-1] == '0'){
                count++;

                if(count > 1)   return false;
            }
        }
        return true;
    }
};
```