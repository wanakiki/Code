## 49. 字母异位词分组

2020-12-14 22:32:50

### 题目

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

**示例:**

```
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

**说明：**


- 所有输入均为小写字母。
- 不考虑答案输出的顺序。



### 思路及代码

由于异位词排序之后都是相同的，可以将排序之后的字符串进行哈希，保存异位词。

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash;
        for(auto str : strs){
            string cur = str;
            sort(cur.begin(), cur.end());
            hash[cur].push_back(str);
        }

        vector<vector<string>> res;
        for(auto it = hash.begin(); it != hash.end(); it++){
            res.push_back(it->second);
        }
        return res;
    }
};
```