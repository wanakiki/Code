## 剑指 Offer II 041. 滑动窗口的平均值

2022-07-16 18:39:58

### 题目

给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。

实现 ``MovingAverage`` 类：


- ``MovingAverage(int size)`` 用窗口大小 ``size`` 初始化对象。
- ``double next(int val)`` 成员函数 ``next`` 每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数
据流中最后 ``size`` 个值的移动平均值，即滑动窗口里所有数字的平均值。




**示例：**

```

输入：
inputs = ["MovingAverage", "next", "next", "next", "next"]
inputs = [[3], [1], [10], [3], [5]]
输出：
[null, 1.0, 5.5, 4.66667, 6.0]

解释：
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // 返回 1.0 = 1 / 1
movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3
```



**提示：**


- ``1 <= size <= 1000``
- ``-10<sup>5</sup> <= val <= 10<sup>5</sup>``
- 最多调用 ``next`` 方法 ``10<sup>4</sup>`` 次




<meta charset="UTF-8" />注意：本题与主站 346 题相同： <a href="https://leetcode-cn.com/problems/moving-average-from-data-stream/">https://leetcode-cn.com/problems/moving-average-from-data-stream/</a>   


[LeetCode链接](https://leetcode-cn.com/problems/qIsx9U/)

### 思路及代码

使用队列保存滑动窗口中的数值，维护变量curSum代表滑动窗口中的元素之和。新增元素时，如果窗口已满则先在curSum中减去队列最前端的值，再累加新值。最后计算平均值并返回。

```cpp
class MovingAverage {
public:
    int maxSize, curSize;
    queue<int> q;
    long long curSum;
    /** Initialize your data structure here. */
    MovingAverage(int _size) {
        maxSize = _size;
        curSize = 0;
        curSum = 0;
    }
    
    double next(int val) {
        if(curSize == maxSize){
            curSum -= q.front();
            q.pop();
        }
        else{
            curSize++;
        }
        q.push(val);
        curSum += val;
        return curSum * 1.0 / curSize;
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
```