## 503. 下一个更大元素 II

2021-03-06 12:12:53

### 题目

给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

**示例 1:**

```

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
```

**注意:** 输入数组的长度不会超过 10000。


[LeetCode链接](https://leetcode-cn.com/problems/next-greater-element-ii/)

### 思路及代码

考虑朴素解法，需要对于每个元素向后遍历到第一个大于它的元素，时间复杂度为O(n^2)，但实际上这一过程可能存在多次重复遍历，可以先从数组的最大元素开始，逆向遍历数组，并在过程中维护单调栈，确保栈顶到栈底元素递增，对于过程中遍历到的任何一个元素，栈中第一个大于该元素的值便是“下一个更大元素”。

```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        if(nums.size()==0){return {};} 
        // 找到数组中的最后一个最大值，令其作为数组的末尾（实际上不是必须的，只要是最大值即可）
        int max_index = -1, tmp = INT_MIN;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] >= tmp){
                tmp = nums[i];
                max_index = i;
            }
        }

        // 从数组末尾逆向遍历 构建单调栈，确保栈中元素递增
        int cur = max_index-1, n = nums.size();
        stack<int> stk;
        stk.push(nums[max_index]);
        vector<int> res(n);
        res[max_index] = -1;
        if(max_index == 0){
            cur += n;
        }

        while(cur != max_index){
            while(!stk.empty() && nums[cur] >= stk.top()){
                stk.pop();
            }
            if(stk.empty()){
                res[cur] = -1;
            }
            else{
                res[cur] = stk.top();
            }
            stk.push(nums[cur]);
            cur--;
            // 避免出现负坐标
            if(cur < 0){
                cur += n;
            }
        }
        return res;
    }
};
```