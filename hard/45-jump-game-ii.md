## 45. 跳跃游戏 II

2020年5月4日

### 题目

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

**示例:**

```
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
    从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。
```

**说明:**

假设你总是可以到达数组的最后一个位置。

### 代码

这个题之前在学校的比赛里面做过，使用的是类似贪心的做法。对于给定的初始节点，可以确定可达的最远距离，然后在这一范围内进行判断，找到可达距离最远的节点作为下一个初始节点，重复这一过程。

算法整个过程相当于对整个数组进行了一次遍历，时间复杂度为O(n)。

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        if(nums.size() == 1)    return 0;
        int left = 0, right = nums[0];
        int res = 1;
        int end = nums.size() - 1;  // 停止位置
        while(right < end){
            res += 1;
            int next_left = 0, next_right = 0;     //用于记录可达最远距离
            for(int i = left + 1; i <= right; i++){
                int tmp = i + nums[i];  // 当前节点可达距离
                if(tmp > next_right){
                    next_right = tmp;
                    next_left = i;
                }
            }
            left = next_left;
            right = next_right;
        }
        return res;
    }
};
```