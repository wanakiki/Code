## 524. 通过删除字母匹配到字典里最长单词

2021-09-15 16:22:56

### 题目

给你一个字符串 ``s`` 和一个字符串数组 ``dictionary`` ，找出并返回 ``dictionary`` 中最长的字符串，该字符串可以通过删除 ``s`` 中的某些字符得到。

如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。



**示例 1：**

```
输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"
```

**示例 2：**

```
输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"
```



**提示：**

- ``1 <= s.length <= 1000``
- ``1 <= dictionary.length <= 1000``
- ``1 <= dictionary[i].length <= 1000``
- ``s`` 和 ``dictionary[i]`` 仅由小写英文字母组成



[LeetCode链接](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/)

### 思路及代码

朴素解法，将所有字符串与s进行比较，判断能否通过s删减元素得到，保留长度最长且字典序最小的字符串。

```cpp
class Solution {
public:
    bool helper(string s, string word){
        if(word.size() > s.size()) return false;   // s无法删减

        // 贪心匹配
        int index_s = 0, index_word = 0;
        while(index_s < s.size() && index_word < word.size()){
            if(word[index_word] == s[index_s]){
                index_word++;
                index_s++;
            }
            else{
                index_s++;
            }
        }
        if(index_word == word.size())   return true;
        else    return false;
    }

    string findLongestWord(string s, vector<string>& dictionary) {
        string res = "";
        for(auto word : dictionary){
            if(helper(s, word)){
                if(res == ""){
                    res = word;
                }
                else{
                    if(word.size() > res.size() || (word.size() == res.size() && word < res)){
                        res = word;
                    }
                }
            }
        }
        return res;
    }
};
```

关于如何判断能否通过s删除元素得到目标字符串target，可以通过贪心算法进行求解。

假设目前要匹配的字符是t,该字符在s中的位置是x1和x2，且x1 < x2，则应取x1作为匹配字符，因为对于目标字符串中剩余元素，若从x2之后能完成匹配，则x1之后同样能够完成匹配，若必须要用到x1 x2之间的元素，选择x2则无法取到，抛弃了实现的可能。