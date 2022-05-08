## 819. 最常见的单词

2022-04-17 17:10:28

### 题目

给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。

题目保证至少有一个词不在禁用列表中，而且答案唯一。

禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。



**示例：**

```
输入:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
输出: "ball"
解释:
"hit" 出现了3次，但它是一个禁用的单词。
"ball" 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。
注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 "ball,"），
"hit"不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
```



**提示：**


- ``1 <= 段落长度 <= 1000``
- ``0 <= 禁用单词个数 <= 100``
- ``1 <= 禁用单词长度 <= 10``
- 答案是唯一的, 且都是小写字母 (即使在 ``paragraph`` 里是大写的，即使是一些特定的名词，答案都是小写的。)
- ``paragraph`` 只包含字母、空格和下列标点符号``!?',;.``
- 不存在没有连字符或者带有连字符的单词。
- 单词里只包含字母，不会出现省略号或者其他标点符号。



[LeetCode链接](https://leetcode-cn.com/problems/most-common-word/)

### 思路及代码

通过哈希表对原始字符串中的单词进行技术（注意将大写转为小写），并使用另外的哈希表保存禁用单词，之后遍历哈希表保存除禁用单词外出现次数最多的单词。

```cpp
class Solution {
public:
    string helper(string s){
        for(int i = 0; i < s.size(); i++){
            s[i] = tolower(s[i]);
        }
        return s;
    }
    string mostCommonWord(string paragraph, vector<string>& banned) {
        int left = 0, right = 0;
        unordered_map<string, int> hash;

        while(right < paragraph.size()){
            if(!isalpha(paragraph[right])){
                if(right != left){
                    hash[helper(paragraph.substr(left, right - left))]++;
                }
                
                left = right + 1;
            }
            right++;
        }
        if(right != left){
            hash[helper(paragraph.substr(left, right - left))]++;
        }
        

        unordered_map<string, int> banned_hash;
        for(auto s : banned){
            banned_hash[s]++;
        }


        string res = "";
        int count = 0;
        for(auto it = hash.begin(); it != hash.end(); it++){
            if(banned_hash.find(it->first) == banned_hash.end()){
                if(it->second > count){
                    res = it->first;
                    count = it->second;
                }
            }
        }
        return res;
    }
};
```