## 239. 滑动窗口最大值

2020年2月12日

### 题目

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例:
```no
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum

### 分析

一种使用``multiset``解题的方法，思路很简单，但效率也不高。

执行用时 : 44 ms , 在所有 C++ 提交中击败了 73.49% 的用户,内存消耗 : 19.2 MB，在所有 C++ 提交中击败了 5.01% 的用户

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        multiset<int> window;
        multiset<int>::iterator it;
        vector<int> res;

        if(nums.size() == 0)
            return res;

        for(int i = 0; i < k; i++){
            window.insert(nums[i]);
        }

        int count = k;
        res.push_back(*(--window.end()));
        
        while(count < nums.size()){
            window.erase(window.find(nums[count - k]));
            window.insert(nums[count++]);
            it = window.end();
            res.push_back(*(--it));
        }
        return res;
    }
};
```

比较容易想到的是用堆来维护一个窗，确保能够快速获取最大值，但是如果只保存数组的数值，在窗口移动后不能确定当前栈顶元素是否还位于窗口内。为了解决这个问题，可以在保存数据时同时保存数据的索引，或者重写比较规则。

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        priority_queue<pair<int, int>> q;
        for(int i = 0;  i < k; i++){
            q.emplace(nums[i], i);
        }
        vector<int> res = {q.top().first};
        for(int i = k; i < n; i++){
            q.emplace(nums[i], i);
            while(q.top().second <= i - k){
                q.pop();
            }
            res.push_back(q.top().first);
        }
        return res;
    }
};
```