# 290. Word Pattern

2018年8月12日

## 题目

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

```no
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```

Example 2:

```no
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
```

Example 3:

```no
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
```

Example 4:

```no
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
```

Notes:

You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

## 分析

这道题是之前面向对象考试的一个变种，最好的办法还是用Map来解决。题目给的例子很清楚，如果算法能够解决这几种情况应该就能够AC🎈了。

因为要判断的字符串str含有多个由空格分割的要比对的元素，所以第一个要解决的问题是如何有效的分割string。我这里使用了istringstream达到了上述目的。

```cpp
istringstream iss(str);
istream_iterator<string> Itbegin = istream_iterator<string>(iss);
istream_iterator<string> Itend = istream_iterator<string>();
vector<string> strs(Itbegin, Itend);
```

原帖地址，还有更多种分割的方式：`https://segmentfault.com/a/1190000009416224`

为了将两部分对比，我开始使用了一个Map，遍历pattern中的每个字符，添加到map中，同时更新对应的值(也就是得到的strs中的元素)。但实际上这种做法并不能解决"abba"对应于"cat cat cat cat"的情况，另外采取了多种做法均失败之后，我想到了两边同时做对比。

新建两个map（map<char, string>，map<string char>)，然后遍历pattern和strs，更新的同时将二者做对比，根据对比结果进行判断。尽管我觉得很麻烦，但是打败了100%的cpp提交，大部分人都是双向对比的做法。

## 代码

C++

```cpp
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        istringstream iss(str);
        istream_iterator<string> Itbegin = istream_iterator<string>(iss);
        istream_iterator<string> Itend = istream_iterator<string>();
        vector<string> strs(Itbegin, Itend);

        int len1 = pattern.size(), len2 = strs.size();
        
        if(len1 != len2)
            return false;
        
        map<char, string> mp1;
        map<string, char> mp2;
        for(int i = 0; i < len1; i++){
            auto it1 = mp1.find(pattern[i]);
            auto it2 = mp2.find(strs[i]);
            if(it1 == mp1.end() && it2 == mp2.end()){
                mp1[pattern[i]] = strs[i];
                mp2[strs[i]] = pattern[i];
            }
            else if(it1 != mp1.end() && it2 != mp2.end()){
                if(mp1[pattern[i]] != strs[i] || mp2[strs[i]] != pattern[i])
                    return false;
            }
            else
                return false;
        }
        return true;
    }
};
```

其他人的cpp解法：

```cpp
#include <unordered_map>

using namespace std;

class Solution {
public:
    static bool wordPattern(string pattern, string str) {
        if (pattern.empty() || str.empty()) {
            return false;
        }

        int i = 0;

        unordered_map<string, char> wordList = {};
        unordered_map<char, string> patternMap = {};

        istringstream stream(str);
        for (string tok; std::getline(stream, tok, ' '); ) {
            if (i >= pattern.size()) {
                return false;
            }

            if (wordList.find(tok) == wordList.end()) {
                wordList[tok] = pattern[i];
            }
            else if (wordList[tok] != pattern[i]) {
                return false;
            }
            
            if (patternMap.find(pattern[i]) == patternMap.end()) {
                patternMap[pattern[i]] = tok;   
            }
            else if (patternMap[pattern[i]] != tok) {
                return false;
            }

            ++i;
        }

        return i == pattern.size();
    }
};
```