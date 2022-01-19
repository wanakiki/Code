## 219. Contains Duplicate II
##### 2018-06-10 10:55:36
##### Map
***
## 题目
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
```
Input: nums = [1,2,3,1], k = 3
Output: true
```
Example 2:
```
Input: nums = [1,0,1,1], k = 1
Output: true
```
Example 3:
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```
## 分析
最容易想到的方式是遍历,但是试了下超时,改用map不过要注意数组下表是从零开始的.
## 示例代码
遍历
```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int len = nums.size();
        for(int i=0;i<len;i++){
            for(int j=i+1;j<=i+k && j<len;j++){
                if(nums[i] == nums[j])
                    return true;
            }
        }
        return false;
    }
};
```
map:
```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int> mp;
        nums.insert(nums.begin(),-1);   //插入一个元素之后从1开始查找
        for(int i=1;i<nums.size();i++){
            if(mp[nums[i]] == 0)
                mp[nums[i]] = i;
            else{
                if(i - mp[nums[i]] <=k)
                    return true;
                else
                    mp[nums[i]] = i;
            }
        }
        return false;
    }
};
```
实际上用map速度也不是很快


#### 2022年1月19日

滑动窗口搭配哈希表，哈希表用于标记元素是否出现。由于需要频繁对哈希表进行增删元素，效率反而不如直接存曾经出现过的值对应的最大索引。

```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if(k >= nums.size())    k = nums.size() - 1;
        int left = 0;
        int right = 0;
        unordered_map<int, int> hash;
        for(right = 0; right <= k; right++){
            if(hash.find(nums[right]) != hash.end())    return true;
            else{
                hash[nums[right]] = 1;
            }
        }

        while(right < nums.size()){
            hash.erase(hash.find(nums[left]));
            left++;

            if(hash.find(nums[right]) != hash.end())    return true;
            else{
                hash[nums[right]] = 1;
            }
            right++;
        }
        return false;
    }
};
```
