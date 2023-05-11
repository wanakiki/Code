## 1016. 子串能表示从 1 到 N 数字的二进制串

2023-05-11 09:19:48

### 题目

给定一个二进制字符串 ``s`` 和一个正整数 ``n``，如果对于 ``[1, n]`` 范围内的每个整数，其二进制表示都是 ``s`` 的 **子字符串** ，就返回 ``true``，否则返回 ``false``。

**子字符串** 是字符串中连续的字符序列。

 

**示例 1：**

```

输入：s = "0110", n = 3
输出：true
```

**示例 2：**

```

输入：s = "0110", n = 4
输出：false
```

 

**提示：**


- ``1 <= s.length <= 1000``
- ``s[i]`` 不是 ``'0'`` 就是 ``'1'``
- ``1 <= n <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/binary-string-with-substrings-representing-1-to-n/)

### 思路及代码

暴力枚举所有子字符串，判断其能构成的整数集合大小。

```cpp
class Solution {
public:
    bool queryString(string s, int n) {
        unordered_set<int> myset;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '0') continue;
            int cur = 0;
            for(int j = i; j < s.size(); j++){
                cur <<= 1;
                cur += s[j] - '0';
                if(cur > n) break;
                myset.insert(cur);
            }
        }

        return myset.size() == n;
    }
};
```