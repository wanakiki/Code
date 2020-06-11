## 739. 每日温度

2020年6月11日

### 题目

请根据每日 ``气温`` 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 ``0`` 来代替。

例如，给定一个列表 ``temperatures = [73, 74, 75, 71, 69, 72, 76, 73]``，你的输出应该是 ``[1, 1, 4, 2, 1, 1, 0, 0]``。

**提示：**``气温`` 列表长度的范围是 ``[1, 30000]``。每个气温的值的均为华氏度，都是在 ``[30, 100]`` 范围内的整数。

### 思路及代码

逆向使用单调栈，因为对于每天的温度，需要查找温度大于当天并且距离最近的一天。......😐

思路比较难描述，可以直接看代码：

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int len = T.size();
        vector<int> res(len, 0);
        stack<int> stk;

        // 逆向遍历
        for(int i = len - 1; i >= 0; i--){
            while(!stk.empty() && T[i] >= T[stk.top()]){
                stk.pop();
            }

            // 栈变为空代表没有更高温度
            if(stk.empty()){
                res[i] = 0;
                stk.push(i);
            }
            else{
                res[i] = stk.top() - i;
                stk.push(i);
            }
        }
        return res;
    }
};
```

看到题解大部分人用的是递减栈搭配正向遍历。