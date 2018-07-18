##  169. Majority Element
##### 2018-05-25 22:23:57
##### 简单题
***
## 题目
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
```
Input: [3,2,3]
Output: 3
```
Example 2:
```
Input: [2,2,1,1,1,2,2]
Output: 2
```
## 分析
一道简单题，但是我却没有什么思路.....
可能是之前考试的时候没用出来map，这次采取了比较麻烦的方法，用map写了出来（不愿意用这么麻烦的写法）

## 示例代码
```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int len=nums.size();
        unordered_map<int,int> mp;
        for(int i=0; i<len;i++){
            mp[nums[i]]+=1;
            if(i>len/2 && mp[nums[i]]>len/2)
                return nums[i];
        }	//题目已经说明一定存在解，所以循环结束的情况只能是长度为1或2
	//针对这两种特殊情况，统一返回首个元素就好
        return nums[0];
    }
};
```

```cpp
static int x = []() {
	std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	return 0;
}();
/*
class Solution {
public:
	int majorityElement(vector<int>& nums) {
		std::sort(nums.begin(), nums.end());
		int len = nums.size();
		return nums[len / 2];

	}
};
*/
class Solution {
public:
	int majorityElement(vector<int>& nums) {
		int majorIndex = 0, cnt = 1;
        for(int i=0; i<nums.size(); ++i) {
            if(nums[majorIndex] == nums[i])
                cnt++;
            else
                cnt--;
            
            if(cnt==0) {
                majorIndex = i;
                cnt = 1;
            }
        }
        return nums[majorIndex];

	}
};
```
