## 1930. 长度为 3 的不同回文子序列

2021-09-04 16:21:32

### 题目

给你一个字符串 ``s`` ，返回 ``s`` 中 **长度为 3 **的**不同回文子序列** 的个数。

即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。

**回文** 是正着读和反着读一样的字符串。

**子序列** 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。


- 例如，``"ace"`` 是 "**<em>a</em>**b**<em>c</em>**d**<em>e</em>**" 的一个子序列。


 

**示例 1：**

```
输入：s = "aabca"
输出：3
解释：长度为 3 的 3 个回文子序列分别是：
- "aba" ("aabca" 的子序列)
- "aaa" ("aabca" 的子序列)
- "aca" ("aabca" 的子序列)
```

**示例 2：**

```
输入：s = "adc"
输出：0
解释："adc" 不存在长度为 3 的回文子序列。
```

**示例 3：**

```
输入：s = "bbcbaba"
输出：4
解释：长度为 3 的 4 个回文子序列分别是：
- "bbb" ("bbcbaba" 的子序列)
- "bcb" ("bbcbaba" 的子序列)
- "bab" ("bbcbaba" 的子序列)
- "aba" ("bbcbaba" 的子序列)
```

 
**提示：**


- ``3 <= s.length <= 10<sup>5</sup>``
- ``s`` 仅由小写英文字母组成



[LeetCode链接](https://leetcode-cn.com/problems/unique-length-3-palindromic-subsequences/)

### 思路及代码

采用了一种几乎是暴力的做法来实现的，没想到竟然击败了60%。思路比较简单，首先遍历字符串获取每个字母出现的第一个位置和最后一个位置，之后针对每种字母左右边界确定的区间，查找出现过的所有字母，累加结果。回文子串的长度为3，两侧元素必定相同，中间元素可以是任意字母。


```cpp
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int res = 0;
        vector<int> left_index(26, -1);
        vector<int> right_index(26);
        for(int i = 0; i < s.size(); i++){
            int cur = s[i] - 'a';
            if(left_index[cur] == -1){
                left_index[cur] = i; 
            }
            right_index[cur] = i;
        }

        for(int i = 0; i < 26; i++){
            vector<int> flag(26, 0);
            int count = 0;
            if(left_index[i] != right_index[i]){
                for(int j = left_index[i] + 1; j < right_index[i]; j++){
                    int cur = s[j] - 'a';
                    if(flag[cur] == 0){
                        count++;
                        flag[cur] = 1;
                    }
                }
            }
            res += count;
        }
        return res;
    }
};
```