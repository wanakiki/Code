## 84. 柱状图中最大的矩形

2020年5月30日

### 题目

给定*n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram.png">

<small>以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 ``[2,1,5,6,2,3]``。</small>

 

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram_area.png">

<small>图中阴影部分为所能勾勒出的最大矩形面积，其面积为 ``10`` 个单位。</small>

 

**示例:**

```
输入: [2,1,5,6,2,3]
输出: 10
```

### 代码

暴力：最大矩形的高一定和某个柱子的高度相同，需要判断所有柱子的高度构成的矩形面积，返回其最大值，方法复杂度较高，无法通过。

单调栈：在暴力法的基础上进行了改进，使用单调栈维护递增序列来得到每个柱子能构成的最大面积，只需要遍历一次。

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = 0;
        stack<int> stk;
        stk.push(-1);

        for(int i = 0; i < heights.size(); i++){
            if(stk.top() != -1 && heights[i] < heights[stk.top()]){
                int cur = stk.top();
                stk.pop();
                int left = stk.top();

                res = max(res, heights[cur] * (i - left - 1));

                i--;
                continue;   // 继续比较元素
            }
            stk.push(i);
        }

        int len = heights.size() - 1;
        while(stk.top() != -1){
            int cur = stk.top();
            stk.pop();

            res = max(heights[cur] * (len - stk.top()), res);
        }
        return res;
    }
};
```