## 907. 子数组的最小值之和

2022-10-28 10:52:36

### 题目

给定一个整数数组 ``arr``，找到 ``min(b)`` 的总和，其中 ``b`` 的范围为 ``arr`` 的每个（连续）子数组。

由于答案可能很大，因此**返回答案模 ``10^9 + 7``** 。

 

**示例 1：**

```
输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
```

**示例 2：**

```
输入：arr = [11,81,94,43,3]
输出：444
```

 

**提示：**


- ``1 <= arr.length <= 3 * 10<sup>4</sup>``
- ``1 <= arr[i] <= 3 * 10<sup>4</sup>``


 


[LeetCode链接](https://leetcode-cn.com/problems/sum-of-subarray-minimums/)

### 思路及代码

直观思路是对于每个数据 n 向两侧查找以 n 为最小元素的子数组个数，但是这样搜索量较大，因此可以更改为维护递增单调栈。

代码写的很臭，因为调 bug 时很难找问题，做了个简单的封装。

```cpp
class HelperStack {
public:
    stack<pair<int,int>> stk;

    int topIndex(){
        if(stk.empty()){
            return -1;
        }
        else{
            return stk.top().second;
        }
    }

    int topVal(){
        if(stk.empty()){
            return 0;       // 题目保证零为最小
        }
        else{
            return stk.top().first;
        }
    }

    void push(int val, int index){
        stk.push(make_pair(val,index));
    }

    void pop(){
        stk.pop();
    }
};
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        HelperStack stk;
        int res = 0;
        int mask = 1000000007;
        // 维护递增栈

        for(int i = 0; i < arr.size(); i++){
            while(stk.topVal() >= arr[i]){
                long long cur_val = stk.topVal();
                int cur_index = stk.topIndex();
                stk.pop();
                int right = i;
                int left = stk.topIndex();

                res += (cur_val * ((long long)(right - cur_index) * (cur_index - left))) % mask;
                res %= mask;
            }

            stk.push(arr[i],i);
        }

        // 栈顶为0代表空
        while(stk.topVal()){
            long long cur_val = stk.topVal();
            int cur_index = stk.topIndex();
            stk.pop();
            int right = arr.size();
            int left = stk.topIndex();

            res += (cur_val * ((long long)(right - cur_index) * (cur_index - left))) % mask;
            res %= mask;

        }
        return res;
    }
};
```