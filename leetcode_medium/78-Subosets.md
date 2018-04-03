## 78. Subsets
##### 2018-04-03 20:33:01
***
## 1.题目
>Given a set of distinct integers, nums, return all possible subsets (the power set).
>
>Note: The solution set must not contain duplicate subsets.   
>给定一个不含重复元素的整形数组，返回数组的全部子集。（注意：解决方案不能含有重复子集）

## 2.分析
C++里面的vector真的是个好东西，省去了申请空间的麻烦而且还能够自己扩充。  
想到的是迭代解决方案，新建一个vector含有一个空，之后开始遍历传入的数组，对于每一个遍历到的对象，根据当前的子集数量，对于每一个子集复制一次并将当前遍历到的数字加到这个子集的尾部。
遍历结束之后返回。
## 3.代码
```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> res(1,vector<int>() );
        int n=0;
        for(int i=0;i<nums.size();i++){
            n=res.size();
            for(int j=0;j<n;j++){
                res.push_back(res[j]);
                res.back().push_back(nums[i]);
            }
        }
        return res;
    }
};
```
