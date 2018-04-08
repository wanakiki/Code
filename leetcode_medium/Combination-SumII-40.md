## 40. Combination Sum II
##### 2018-04-08 23:07:51
##### 回溯
***
## 1.题目
> Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
>
>Each number in C may only be used once in the combination.  
>Note:  
>All numbers (including target) will be positive integers.  
The solution set must not contain duplicate combinations.

>给定候选号码（C）和目标号码（T）的集合，找出C中候选号码与T相加的所有唯一组合。  
C中的每个数字只能在组合中使用一次。  
注意：  
所有数字（包括目标）都是正整数。  
该解决方案集不能包含重复的组合

## 2.分析
与组合数组原版相同的思路（加上排序），不过难点在于如何排除重复。  
要注意，因为多个相同元素可以同时存在一种情况内，所以并不能简单的通过下面的语句排除
```
if(now==0 &&i&& candidates[i]==candidates[i-1]) return;
```
这种语句只是排除了添加首位的情况，并不能有效去重，但其实修改也很简单（见代码部分），  

sort语句稍微比qsort方便些
## 3.代码
```cpp
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> temp;
        int len=candidates.size();
        sort(candidates.begin(),candidates.end());
        combination(res,candidates,temp,target,0,len);
        return res;
    }
    void combination(vector<vector<int>> &res,vector<int> &candidates,vector<int> &temp,int target,int now,int len){
      //if(now && candidates[now]==candidates[now-1]) return;
      if(now>len|| target<0)  return;
      if(target==0){
        res.push_back(temp);
        return;
      }
      for(int i=now;i<len;i++){
        if(i&& candidates[i]==candidates[i-1]&&i>now)    continue;    //有效的去重
        temp.push_back(candidates[i]);
        combination(res,candidates,temp,target-candidates[i],i+1,len);
        temp.pop_back();
      }
    }
};
```
