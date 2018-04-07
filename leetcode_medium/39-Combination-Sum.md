## 39. Combination Sum
##### 回溯
***
## 1.题目
> Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
>
>The same repeated number may be chosen from C unlimited number of times. 
>
>Note:  
>All numbers (including target) will be positive integers.  
>The solution set must not contain duplicate combinations.

>给定一组候选号码（C）（没有重复）和目标号码（T），找出C中所有候选号码与T相加的唯一组合。可以从C无限次数中选择相同的重复数目。 注意：所有数字（包括目标）都是正整数。该解决方案集不能包含重复的组合。

## 2.分析
寒假遇到的一道题目，由于当时c语言不太熟练尝试之后放弃了。现在对C++有了部分认识，用vector很容易解决了这道题目。
## 3.代码
```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> temp;
        int len=candidates.size();
        combination(res,candidates,temp,target,0,len);
        return res;
    }
    void combination(vector<vector<int>> &res,vector<int> &candidates,vector<int> &temp,int target,int now,int len){
      if(now==len|| target<0)  return;
      if(target==0){
        res.push_back(temp);
        return;
      }
      for(int i=now;i<len;i++){
        temp.push_back(candidates[i]);
        combination(res,candidates,temp,target-candidates[i],i,len);
        temp.pop_back();
      }
    }
};
```
