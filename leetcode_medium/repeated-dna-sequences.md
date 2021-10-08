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

2021年10月8日

状态压缩做法，参考官方题解，执行起来快了一些。感觉做题还是不够系统，虽然已经做过了但还是不能很快想起来解决方案。

```cpp
class Solution {
public:
    int char2int(char a){
        if(a == 'A')    return 0;
        else if(a == 'C')   return 1;
        else if(a == 'G')   return 2;
        else    return 3;
    }
    char int2char(int n){
        if(n == 0)  return 'A';
        else if(n == 1) return 'C';
        else if(n == 2) return 'G';
        else    return 'T';
    }
    string int2str(int a){
        string res(10, '0');
        for(int i = 9; i >= 0; i--){
            int cur = a & 3;
            a >>= 2;

            res[i] = int2char(cur);
        }
        return res;
    }
    vector<string> findRepeatedDnaSequences(string s) {
        int cur = 0;
        int mask = 1048575;
        unordered_map<int, int> hash;
        for(int i = 0; i < s.size(); i++){
            int c = char2int(s[i]);

            if(i < 9){
                cur <<= 2;
                cur += c;
            }
            else{
                cur <<= 2;
                cur &= mask;
                cur += c;

                hash[cur]++;
            }
        }

        vector<string> res;
        for(auto it = hash.begin(); it != hash.end(); it++){
            if(it->second > 1){
                res.push_back(int2str(it->first));
            }
        }
        return res;
    }
};
```
