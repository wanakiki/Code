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

*** 

2020年3月13日

#### 排序后遍历

先对数组进行排序，之后遍历数组，找到连续出现次数大于数组长度一半的数。

时间复杂度O(nlogn)（排序）,执行用时:24ms,在所有C++提交中击败了61.00%的用户，内存消耗:20.6MB,在所有C++提交中击败了5.28%的用户

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int cur = nums[0], sum = 0, len = nums.size();
        int aim = len / 2;  //整型自动向下取整
        for(int i = 0; i < len; i++){
            if(cur == nums[i]){
                sum++;
            }
            else{
                if(sum > aim)
                    return cur;
                sum = 1;
                cur = nums[i];
            }
        }
        return cur;     //由于一定存在，遍历结束后的值一定为最终结果
    }
};
```

#### 哈希表

``unordered_map``作哈希表，统计变量的出现次数，之后遍历哈希表找到出现次数大于长度一半的元素。

``unoredered_map``插入、查找元素的时间复杂度为O(1)，在最坏的情况下为O(n)。因此算法的时间复杂度在O(n)与O(n^2)之间。

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int aim = nums.size()/2;
        unordered_map<int, int> hash;
        for(auto n : nums)
            hash[n]++;
        for(auto i = hash.begin(); i != hash.end(); i++){
            if(i->second > aim)
                return i->first;
        }
        return 0;
    }
};
```

#### 计数算法

写完排序之后发现这个题目在学校的比赛里面曾经见到过，因为我们要找的数出现的次数超过了其他所有数出现次数的和，所以我们可以遍历一次数组，选定第一个数作为出发点，如果新遇到的数和它相同，则数量加一，否则减一，当数量减为0之后更换记录的数。看代码更容易理解。

算法复杂度O(n)，执行用时:16ms,在所有C++提交中击败了94.70%的用户，内存消耗:20.6MB,在所有C++提交中击败了5.28%的用户

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cur = nums[0], cnt = 1;  //已知数组非空
        for(int i = 1; i < nums.size(); i++){
            if(cur == nums[i])
                cnt++;
            else
                cnt--;
            if(cnt == 0){
                cur = nums[i];
                cnt = 1;
            }
        }
        return cur;
    }
};
```

看了官方的题解之后发现这就是所谓的投票算法，官方CPP代码如下：

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = -1;
        int count = 0;
        for (int num : nums) {
            if (num == candidate)
                ++count;
            else if (--count < 0) {
                candidate = num;
                count = 1;
            }
        }
        return candidate;
    }
};
```