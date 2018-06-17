## 187. Repeated DNA Sequences
##### 2018-05-16 18:47:01
##### 重复的DNA序列
***
## 题目
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```
## 分析
按照分类来，这道题好像属于位运算，在不知情的情况下尝试了自己的方法之后果断投靠哈希表了，真的炒鸡简单....

还要注意一点，如果有11个A的话，10个A也算作一种结果。
## 示例代码
```cpp
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        if(s.size()<=10)
            return res;
        unordered_map<string,int> hash;
        for(int i=0;i<=s.size()-10;i++){
            hash[s.substr(i,10)]++;
        }
        for(auto i=hash.begin();i!=hash.end();i++){
            if(i->second > 1)
                res.push_back(i->first);
        }
        return res;
    }
};
```
然后再来看看我的....数据少的时候还可以成立，但是够长了就该超时了，而且还有个麻烦的去重
```cpp
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        if(s.size()<10)
            return res;
        string temp1,temp2;
        for(int i=0;i<=s.size()-10;i++){
            temp1=s.substr(i,10);
            for(int j=i+1;j<=s.size()-10;j++){
                temp2=s.substr(j,10);
                if(temp1==temp2){
                    res.push_back(temp1);
                    break;
                }
            }
        }
        sort(res.begin(),res.end());
        vector<string> :: iterator new_end = unique(res.begin(),res.end());
        res.erase(new_end,res.end());
        return res;
    }
};
```
