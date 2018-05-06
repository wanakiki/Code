## 139. Word Break
##### 2018-05-06 23:33:08
##### dp 打断字符
***
## 题目
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.
-
Example 1:
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```
Example 2:
```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```
Example 3:
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```
## 分析
给出非空的字符串，以及一个非空的字典，要求判断该字符串是否能够被拆分为字典中的单词。  这道题主要参考了别人的代码，对于sort调用函数的书写以及auto的应用增加了经验。

先将字典按照长度排序，定义一个长度比s多一个的布尔型数组res，res除最后一个元素为真其余全为假，从最后的位置开始查找对应字典单词的长度，找到则将res对应的元素改判为真，遍历结束，返回res[0];
## 示例代码
```cpp
class Solution {
    vector<bool> res;
public:
    bool wordBreak(string s, vector<string>& wordDict) {

        sort(wordDict.begin(),wordDict.end(),[](const string&a,const string&b){
            if(a.size() == b.size())
                return a<b; //长度相等比较数据
            return a.size()<b.size();
        });     //这种排序的手法值得借鉴

        res.resize(s.size() + 1);
        fill(res.begin(), res.end(), false);

        int i=s.size();
        res[i]=true;
        while(i){
            if(res[i])
                for(auto w: wordDict) {
                    int j = i - w.size();

                    if(j < 0)
                        break;

                    if(s.substr(j, w.size()) == w)
                        res[j] = true;
                }
            i--;
        }
        return res[0];
    }
};
```
