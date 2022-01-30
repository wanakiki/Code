## 920. 两句话中的不常见单词

2022-01-30 09:42:05

### 题目

**句子** 是一串由空格分隔的单词。每个 **单词** 仅由小写字母组成。

如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 **没有出现** ，那么这个单词就是 **不常见的**。

给你两个 **句子** ``s1`` 和 ``s2`` ，返回所有 **不常用单词** 的列表。返回列表中单词可以按 **任意顺序**  
组织。






**示例 1：**

```
输入：s1 = "this apple is sweet", s2 = "this apple is sour"
输出：["sweet","sour"]
```

**示例 2：**

```
输入：s1 = "apple apple", s2 = "banana"
输出：["banana"]
```



**提示：**


- ``1 <= s1.length, s2.length <= 200``
- ``s1`` 和 ``s2`` 由小写英文字母和空格组成
- ``s1`` 和 ``s2`` 都不含前导或尾随空格
- ``s1`` 和 ``s2`` 中的所有单词间均由单个空格分隔



[LeetCode链接](https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/)

### 思路及代码

用两个哈希表分别统计两个句子中各个单词的出现次数，统计结束后遍历哈希表，查找出现次数为1的单词是否在另一个句子中出现。

```cpp
class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> hash1;
        unordered_map<string, int> hash2;
        vector<string> res;

        int last_pos = 0;
        int index = 0;
        while(index <= s1.size()){
            if(index == s1.size() || s1[index] == ' '){
                hash1[s1.substr(last_pos, index - last_pos)]++;
                index++;
                last_pos = index;
            }
            else{
                index++;
            }
        }

        last_pos = 0;
        index = 0;
        while(index <= s2.size()){
            if(index == s2.size() || s2[index] == ' '){
                hash1[s2.substr(last_pos, index - last_pos)]++;
                index++;
                last_pos = index;
            }
            else{
                index++;
            }
        }

        for(auto it = hash1.begin(); it != hash1.end(); it++){
            if(it->second == 1 && hash2.find(it->first) == hash2.end()) res.push_back(it->first);
        }
        for(auto it = hash2.begin(); it != hash2.end(); it++){
            if(it->second == 1 && hash1.find(it->first) == hash1.end()) res.push_back(it->first);
        }
        return res;
    }
};
```