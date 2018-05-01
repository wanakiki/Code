## 131. Palindrome Partitioning
##### 2018年05月01日13:57:04
##### 回文分区 回溯
****
## 题目
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:
```
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```
## 分析
题目要求将字符串s拆分为由回文构成的多个部分，并返回所有的可能。
因为题目要求列出所有的情况，鉴于以往的经验，采取回溯方法可以更好地解决问题。先写一个函数用于判断一段字符是否为回文序列，接着对s进行遍历，从长度为1开始，直到为整个字符串。
若当前情况对应的字符串为回文，则对其之后的部分接着判断，直到判断完整个字符串。注意进行下一次判断时**要先``push_back``再``pop_back()``。**
## 示例代码
```cpp
class Solution {
public:
    bool ispalindrome(const string& s,int l,int r){
        while(l<r){
            if(s[l]!=s[r])
                return false;
            l++;
            r--;
        }
        return true;
    }
    void helper(vector<vector<string>>& res,vector<string>& temp,string s,int start){
        if(start==s.size())
            res.push_back(temp);
        for(int i=start;i<s.size();i++){
            if(ispalindrome(s,start,i)){
                temp.push_back(s.substr(start,i-start+1));  //substr字符串复制
                helper(res,temp,s,i+1);
                temp.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s) {
        vector<string> temp;
        vector<vector<string>> res;
        helper(res,temp,s,0);
        return res;
    }
};
```
![dsa](../../photo/2018-05-01.png)
