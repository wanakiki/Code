## 49. Group Anagrams
##### 2018-04-09 19:32:05
##### 新的遗留问题
***
## 1.题目
>Given an array of strings, group anagrams together.   
>For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
>```
>[
>  ["ate", "eat","tea"],
>  ["nat","tan"],
>  ["bat"]
>]
>```
>Note: All inputs will be in lower-case.  
>给定一组字符串，将相同的字谜组合在一起

## 2.分析
讲道理，这道题目应该是用哈希表才能做出来的，但毕竟还在学C++的阶段，暂时不花很多时间去完全了解新的知识。  
（C++里面没有哈希表对应的hash容器，网上的代码采用map来完成该功能）

尽管没有用哈希表，但写出来遍历做法对于刚接触vector的我也有不少收获。
我将第一个元素存储到返回的vector接着对其余的每个字符串排序，与返回vector现有的字谜排序后对比，不同则添加到返回vector中，如果相同，则添加到对应组。

思路很简单，但是在实现的时候不知道如何返回与添加，因为返回的vector与字符串相比高了两层。
1. 对于返回，当返回为空时可以直接返回定义的vector也可以 vector<T> ();
2. 借鉴网上的思路，当需要跨两层添加返回数据时，设置 vector<string> 用于添加。

## 3.代码（超时）
```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
      vector<vector<string>> res;
      int sum=0;
      for(int i=0;i<strs.size();i++){
        vector<string> save;
        if(i==0){
          save.push_back(strs[i]);
          res.push_back(save);
          sum++;
          continue;
        }
        string temp1=strs[i];
        sort(temp1.begin(),temp1.end());
        for(int j=0;j<sum;j++){
          string temp2=res[j][0];
          sort(temp2.begin(),temp2.end());
          if(temp2==temp1){
            res[j].push_back(strs[i]);
            break;
          }
          if(j==res.size()-1){
            save.push_back(strs[i]);
            res.push_back(save);
            sum++;
            break;
          }
        }
      }
      return res;
    }
};
```
leetcode的测试例很过分，用了很多数据，我的这种写法本来就麻烦，结果当然是超时。  
代码局部还可以简化，但是因为方法局限性也没有多做处理。
