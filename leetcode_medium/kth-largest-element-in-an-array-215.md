## 215. Kth Largest Element in an Array
##### 2018年07月18日
****
### 题目
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```
Example 2:
```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```
Note:

You may assume k is always valid, 1 ≤ k ≤ array's length.
### 分析
要找到第k大的数，因为C++已经有sort了，大部分人都是直接排序然后输出的，讨论区看到了分治的做法，因为对快速排序不够了解，也没有搞明白。最后写的是用优先级队列的做法。
### 示例代码
C++：

优先级队列：
```cpp
class Solution {
public:
int findKthLargest(vector<int>& nums, int k) {
	priority_queue<int, vector<int>, less<int>> q;
	for(int i = 0; i < nums.size(); i++){
		q.push(nums[i]);
	}
	for(int i = 0; i < k; i++){
		q.pop();
	}
	return q.front();
  }
};
```
直接排序：
```cpp
class Solution {
public:
int findKthLargest(vector<int>& nums, int k) {
	sort(nums.begin(), nums.end(), greater<int>() );
    return nums[k-1];
  }
};
```
