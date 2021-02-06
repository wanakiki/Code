## 1538. 可获得的最大点数

2021-02-06 11:54:02

### 题目

几张卡牌** 排成一行**，每张卡牌都有一个对应的点数。点数由整数数组 ``cardPoints`` 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 ``k`` 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 ``cardPoints`` 和整数 ``k``，请你返回可以获得的最大点数。

 

**示例 1：**

```
输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
```

**示例 2：**

```
输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。
```

**示例 3：**

```
输入：cardPoints = [9,7,7,9,7,7,9], k = 7
输出：55
解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
```

**示例 4：**

```
输入：cardPoints = [1,1000,1], k = 1
输出：1
解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。 
```

**示例 5：**

```
输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
输出：202
```

 

**提示：**


- ``1 <= cardPoints.length <= 10^5``
- ``1 <= cardPoints[i] <= 10^4``
- ``1 <= k <= cardPoints.length``



[LeetCode链接](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/)

### 思路及代码

滑动窗口记录最小值，该区间不取，剩余区间便有最大值。

```cpp
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int len = cardPoints.size();
        int windowSize = len - k;
        int left = 0, right = windowSize-1;
        int windowCount = 0, sumPoint = 0;
        for(int i = 0; i < windowSize; i++){
            windowCount += cardPoints[i];
        }
        sumPoint = windowCount;
        int res = windowCount;
        // 窗口滑动
        for(int i = right+1; i < len; i++){
            sumPoint += cardPoints[i];
            windowCount += cardPoints[i] - cardPoints[left++];
            res = min(res, windowCount);
        }
        return sumPoint - res;
    }
};

//求连续len-k个数的最小值
```

也可以分别计算左右两个方向可能的累加和，之后遍历左右两侧个数相加为k的所有可能，取最大值。

```cpp
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int len = cardPoints.size();
        vector<int> left_count(len, 0);
        vector<int> right_count(len, 0);
        for(int i = 0; i < len; i++){
            if(i == 0){
                left_count[i] = cardPoints[i];
            }
            else{
                left_count[i] = cardPoints[i] + left_count[i-1];
            }
        }

        for(int i = len - 1; i >= 0; i--){
            if(i == len - 1){
                right_count[i] = cardPoints[i];
            }
            else{
                right_count[i] = right_count[i+1] + cardPoints[i];
            }
        }

        int res = 0;
        int left = -1, right = len - k;
        while(right <= len){
            int tmp = 0;
            if(left >= 0){
                tmp += left_count[left];
            }
            if(right < len){
                tmp += right_count[right];
            }
            right++;
            left++;
            res = max(res, tmp);
        }
        return res;
    }
};
```