# 383. Ransom Note

2018年8月15日

## 题目

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

```no
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

## 分析

采用了一个比较笨的方法：将两个字符串排序确保作比较时能够遇到。遍历magazine字符串，并且在循环外设置ransomNote的索引，如果遇到了ransomNote的字符，就更新索引，判断ransomNote数组是否全部被匹配。全部匹配返回真。如果遍历完magazine数组ransomNote还没有匹配完毕，返回假。

## 代码

C++

```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        sort(ransomNote.begin(), ransomNote.end());
        sort(magazine.begin(), magazine.end());
        
        int len = ransomNote.size();
        int i = 0;
        if(magazine.size() < len)
            return false;
        for(int j = 0; j < magazine.size(); j++){
            if(magazine[j] == ransomNote[i])
                i++;
        }
        if(i < len)
            return false;
        else
            return true;
    }
};
```

哈希表统计每个字符出现次数。

```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> count_a(26, 0);
        vector<int> count_b(26, 0);

        for(auto s : ransomNote){
            count_a[s - 'a']++;
        }
        for(auto s : magazine){
            count_b[s - 'a']++;
        }

        for(int i = 0; i < count_a.size(); i++){
            if(count_b[i] < count_a[i]) return false;
        }
        return true;
    }
};
```