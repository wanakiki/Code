## 1790. 仅执行一次字符串交换能否使两个字符串相等

2022-10-11 11:40:31

### 题目

给你长度相等的两个字符串 ``s1`` 和 ``s2`` 。一次 **字符串交换** 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。

如果对 **其中一个字符串** 执行 **最多一次字符串交换** 就可以使两个字符串相等，返回 ``true`` ；否则，返回 ``false`` 。

 

**示例 1：**

```
输入：s1 = "bank", s2 = "kanb"
输出：true
解释：例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"
```

**示例 2：**

```
输入：s1 = "attack", s2 = "defend"
输出：false
解释：一次字符串交换无法使两个字符串相等
```

**示例 3：**

```
输入：s1 = "kelb", s2 = "kelb"
输出：true
解释：两个字符串已经相等，所以不需要进行字符串交换
```

**示例 4：**

```
输入：s1 = "abcd", s2 = "dcba"
输出：false
```

 

**提示：**


- ``1 <= s1.length, s2.length <= 100``
- ``s1.length == s2.length``
- ``s1`` 和 ``s2`` 仅由小写英文字母组成



[LeetCode链接](https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal/)

### 思路及代码

返回true需要满足以下条件：字符串中字符不等的位置只有0或2个，且在有2个不同的位置时，这2个位置满足交换条件。

```cpp
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        vector<int> count;
        for(int i = 0; i < s1.size(); i++){
            if(s1[i] != s2[i]){
                count.push_back(i);
            }
        }

        if(count.size() == 0 || count.size() == 2){
            if(count.size() == 0)   return true;
            else{
                return s1[count[0]] == s2[count[1]] && s1[count[1]] == s2[count[0]];
            }
        }
        else{
            return false;
        }
    }
};
```