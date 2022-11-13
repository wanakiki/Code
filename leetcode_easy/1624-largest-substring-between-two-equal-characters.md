## 1746. 两个相同字符之间的最长子字符串

2022-09-17 09:43:06

### 题目

给你一个字符串 ``s``，请你返回 **两个相同字符之间的最长子字符串的长度**，计算长度时不含这两个字符。如果不存在这样的子字符串，返回 ``-1`` 。

**子字符串** 是字符串中的一个连续字符序列。

 

**示例 1：**

```
输入：s = "aa"
输出：0
解释：最优的子字符串是两个 'a' 之间的空子字符串。
```

**示例 2：**

```
输入：s = "abca"
输出：2
解释：最优的子字符串是 "bc" 。
```

**示例 3：**

```
输入：s = "cbzxy"
输出：-1
解释：s 中不存在出现出现两次的字符，所以返回 -1 。
```

**示例 4：**

```
输入：s = "cabbac"
输出：4
解释：最优的子字符串是 "abba" ，其他的非最优解包括 "bb" 和 "" 。
```

 

**提示：**


- ``1 <= s.length <= 300``
- ``s`` 只含小写英文字母



[LeetCode链接](https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters/)

### 思路及代码

统计每个字符第一次和最后一次出现的位置，返回最大长度。

```cpp
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        vector<int> last_pos(128, -1);
        int res = -1;
        for(int i = 0; i < s.size(); i++){
            char c = s[i];
            if(last_pos[c] != -1){
                res = max(res, i - last_pos[c] - 1);
            }
            else{
                last_pos[c] = i;
            }
            
        }
        return res;
    }
};
```