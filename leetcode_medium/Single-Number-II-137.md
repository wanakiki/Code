## 137. Single Number II
##### 2018-05-04 19:25:02
##### 查找单个数字
****
## 题目
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
```
Input: [2,2,3,2]
Output: 3
```
Example 2:
```
Input: [0,1,0,1,0,1,99]
Output: 99
```
## 分析
如果不考虑运行时间的话，先将数组排序，排序后位于开始或结尾的数据如果与其相邻的元素不同，则返回该元素，对于数组中间的部分，如果两侧的元素都不与之相同，返回该元素。

不过自己还是不大懂按位与或的操作。
## 示例代码
```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++){
            if(i==0 && nums[1]!=nums[0])
                return nums[i];
            if(i==nums.size()-1 && nums[i]!=nums[i-1])
                return nums[i];
            if(nums[i-1]!=nums[i] && nums[i+1]!=nums[i])
                return nums[i];
        }
    }
};
```

昂，最快的
```cpp
static int any = []() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	return 0;
}();

class Solution {
public:
	int singleNumber(vector<int> &nums) {
		int a = 0, b = 0;
		for (int i : nums) {
			b = (b ^ i) & ~a;
			a = (a ^ i) & ~b;
		}
		return b;
	}
};
```
