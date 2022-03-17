## 720. 词典中最长的单词

2022-03-17 08:59:49

### 题目

给出一个字符串数组 ``words`` 组成的一本英语词典。返回 ``words`` 中最长的一个单词，该单词是由 ``words`` 词典中其他单词逐步
添加一个字母组成。

若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。



**示例 1：**

```
输入：words = ["w","wo","wor","worl", "world"]
输出："world"
解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。
```

**示例 2：**

```
输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply"
```



**提示：**


- ``1 <= words.length <= 1000``
- ``1 <= words[i].length <= 30``
- 所有输入的字符串 ``words[i]`` 都只包含小写字母。



[LeetCode链接](https://leetcode-cn.com/problems/longest-word-in-dictionary/)

### 思路及代码

哈希表存储满足条件的字符串，对于每个新遍历到的字符串，检查去掉最后一个字母后的字符串是否在哈希表中存在，如果存在则更新最大长度并将当前字符串存入哈希表。题目要求的序列必须从空字符串开始，因此在初始化哈希表后需要放入空字符串对应的索引。

另外，在更新最大值时，注意不要将最大值初始化为负数，模板类的 size 函数的返回值是无符号类型，与负数进行比较时需要特别考虑。对于本问题，直接初始化最大长度为0即可。


```cpp
class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());
        unordered_map<string, int> hash;
        int max_len = 0;
        string res = "";
        hash[""] = 1;
        for(auto s : words){
            //cout << s << endl;
            if(hash.find(s.substr(0, s.size() - 1)) != hash.end()){
                if(s.size() > max_len){
                    max_len = s.size();
                    res = s;
                }
                hash[s] = 1;
            }
            
        }
        return res;
    }
};
```