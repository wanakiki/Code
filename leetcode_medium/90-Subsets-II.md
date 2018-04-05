## 90. Subsets II
##### 2018-04-05 23:45:07
***
## 1.题目
> Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
>
>Note: The solution set must not contain duplicate subsets. 
>
>给定可能包含重复，整数的整数，返回所有可能的子集（功率集）。  
>注意：解决方案集不能包含重复的子集。

For example,
If nums = [1,2,2], a solution is:
```
[
 [2],
 [1],
 [1,2,2],
 [2,2],
 [1,2],
 []
]
```

## 2.分析
与subsets相比，这道题目只是在原有的情况下让原始数组出现了重复数据。  
做法仍旧是迭代，不过当发现当前遍历到的数组元素与前一个元素相同时，复制数组的位置不从0，而是继续上一次的j，当不同时才从0开始复制。  

不过迭代的速度好慢啊..........4.85%
## 3.代码
```cpp
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums){
        sort(nums.begin(),nums.end());
        vector<vector<int>> res(1,vector<int>());
        int n=0,j=0;
        for(int i=0;i<nums.size();i++){
                n=res.size();
                if(i && nums[i]!=nums[i-1])  
                        j=0;    //与前一个元素不等时才从零开始复制
                for(;j<n;j++){                                                 
                        res.push_back(res[j]);
                        res.back().push_back(nums[i]);
                }
        }
        return res;
    }
};
```
