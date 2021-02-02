## 424. 替换后的最长重复字符

2021-02-02 11:40:15

### 题目

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换*k*次。在执行上述操作后，找到包含重复字母的最长子串的长度。

**注意：**字符串长度 和*k*不会超过 10<sup>4</sup>。

**示例 1：**

```

输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
```

**示例 2：**

```

输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
```


[LeetCode链接](https://leetcode-cn.com/problems/longest-repeating-character-replacement/)

### 思路及代码

首先需要明确的是目标字符串需要满足：``字符串长度 - 字母的最大出现频率 >= k``。在此基础上容易想到滑动窗口的做法，不断增加窗口长度，在不满足条件后更新窗口的左端点，过程中保留窗口长度的最大值。

需要注意的是，该方法每次更新窗口长度后都需要遍历一次频率数组，得到当前字母的最高出现频率。官方题解给了一种很巧妙的解答方式，使得维护频率的最大值并不需要遍历数组，提升了速度。

具体做法是，不管当前字符串是否满足要求，右端点始终向右移动一格，而左端点只在不满足要求时进行移动，且只移动一格。在这样的条件下，每次循环，窗口的长度或者加一，或者保持不变。

在窗长保持不变时，对于任何新加入的节点，只要该节点的出现频率不大于之前的最大频率，该情况必然不满足条件；若出现频率大于之前的最大频率，则可继续进行扩张。

所以最后窗口的长度必然是过程中能够取得的最大长度。

```cpp
class Solution {
public:
    int get_max(vector<int> count){
        int res = -1;
        for(int i = 0; i < count.size(); i++){
            res = max(res, count[i]);
        }
        return res;
    }
    int characterReplacement(string s, int k) {
        vector<int> count(26, 0);
        int len = s.size();
        int left = 0, right = 0;
        int maxn = 0;
        while(right < len){
            count[s[right] - 'A']++;
            // 窗口长度增加或者保持不变
            // 若保持不变，对于任何新加入的节点，只要该节点的出现频率不大于之前的最大频率，该情况必然不满足条件；若出现频率大于之前的最大频率，则可继续进行扩张
            
            maxn = max(maxn, count[s[right] - 'A']);
            // maxn = get_max(count);
            // 满足题意的字符串应该符合
            // 字符串长度 - 所出现字母的最大频率 <= k
            if(right - left + 1 - maxn > k){
                count[s[left] - 'A']--;
                left++;
            }
            right++;
        }
        return right - left;
    }
};
```