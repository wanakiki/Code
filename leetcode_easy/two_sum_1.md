## 1. Two Sum
##### 2018年7月26日
***
### 题目
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

### 分析
今天才突然发现第一题居然没写解题报告...

第一次采用C语言做，遍历数组，查找两个相加满足题目要求的数字，返回下标，尽管用了两个循环来进行操作最后还是没有超时。

我认为这和C的特点有关，于是今天早上又拿C++写了一下，同样是两次循环遍历，判断加和是否为target，也没有超时，不过C++比较快的做法是引入map。

### 示例代码
C：
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int * zu=(int *)malloc(sizeof(int)*2);
        for(int i=0;i<numsSize-1;i++)
                for(int j=i+1;j<numsSize;j++){
                        if(nums[i]+nums[j]==target){
                                zu[0]=i;
                                zu[1]=j;
                                break;
                        }
                }
    return zu;
}
```
C++:
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        for(int i = 0; i < nums.size() - 1 ; i++)
            for(int j = i + 1; j < nums.size(); j++){
                if(nums[i] + nums[j] == target){
                    res.push_back(i);
                    res.push_back(j);
                    return res;
                }
            }
        return res;
    }
};
```
引入map之后从124ms提升到了4ms
```cpp
class Solution
{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_map<int, int> table;
        for(int i = 0; i < nums.size(); ++i) table[nums[i]] = i;
        for(int i = 0; i < nums.size(); ++i)
        {
            if(table.find(target - nums[i]) != table.end() && i != table[target - nums[i]]) 
                return {i, table[target - nums[i]]};
        }
        return vector<int>();
    }
};
```
