## 828. 统计子串中的唯一字符

2022-09-06 11:35:41

### 题目

我们定义了一个函数 ``countUniqueChars(s)`` 来统计字符串 ``s`` 中的唯一字符，并返回唯一字符的个数。

例如：``s = "LEETCODE"`` ，则其中 ``"L"``, ``"T"``,``"C"``,``"O"``,``"D"`` 都是唯一字符，因为它们只出现一次，所以 ``countUniqueChars(s) = 5`` 。        

本题将会给你一个字符串 ``s`` ，我们需要返回 ``countUniqueChars(t)`` 的总和，其中 ``t`` 是 ``s`` 的子字符串。输入用例保证返回值为 32 位整数。

注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 ``s`` 的所有子字符串中的唯一字符）。



**示例 1：**

```
输入: s = "ABC"
输出: 10
解释: 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
     其中，每一个子串都由独特字符构成。
     所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
```

**示例 2：**

```
输入: s = "ABA"
输出: 8
解释: 除了 countUniqueChars("ABA") = 1 之外，其余与示例 1 相同。
```

**示例 3：**

```
输入：s = "LEETCODE"
输出：92
```



**提示：**


- ``1 <= s.length <= 10^5``
- ``s`` 只包含大写英文字符



[LeetCode链接](https://leetcode-cn.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/)

### 思路及代码

题目要求可以等价为对于字符串中的每个字符a，其能够构成的只包含一个元素a的字符串的个数。

因此可以对数组中的每个元素，查找左侧和右侧第一个相邻的相同字符的位置。假设当前元素索引为i，左侧第一个相同元素索引为x，右侧第一个相同元素索引为y，则当前元素能够构成的字符串个数为``(i - x) * (y - i)``。由上式可以发现，左右相同元素不参与计算，因此边缘数值可处理为-1和len。

类似的思路在字符串题目中比较常见。


```cpp
class Solution {
public:
    int uniqueLetterString(string s) {
        int len = s.size();
        vector<int> left_pos(len, -1);
        vector<int> right_pos(len, -1);
        vector<int> char_pos(26, -1);


        // 左侧
        for(int i = 0; i < len; i++){
            left_pos[i] = char_pos[s[i] - 'A'];
            char_pos[s[i] - 'A'] = i;
        }

        // 右侧
        for(int i = 0; i < char_pos.size(); i++){   char_pos[i] = len;   }

        for(int i = len - 1; i >= 0; i--){
            right_pos[i] = char_pos[s[i] - 'A'];
            char_pos[s[i] - 'A'] = i;
        }

        // 计算结果
        int res = 0;
        for(int i = 0; i < len; i++){
            res += (i - left_pos[i]) * (right_pos[i] - i);
        }
        return res;
    }
};
```