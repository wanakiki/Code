## 295. 数据流的中位数

2021-08-27 16:48:29

### 题目

中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：


- void addNum(int num) - 从数据流中添加一个整数到数据结构中。
- double findMedian() - 返回目前所有元素的中位数。


**示例：**

```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
```

**进阶:**


- 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
- 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？



[LeetCode链接](https://leetcode-cn.com/problems/find-median-from-data-stream/)

### 思路及代码

使用大顶堆和小顶堆维护中位数两侧的数据，数据流输入过程中注意保持两个堆内元素数量之差不超过一。为了方便计算中位数数值，针对于数字个数为奇数情况，可以令大顶堆或者小顶堆中的一个拥有额外一个元素，堆顶元素便是当前的中位数。

方法很巧妙，但是执行效率较低。

```cpp
class MedianFinder {
public:
    priority_queue<int, vector<int>, less<int>> maxQ;   // 小顶堆
    priority_queue<int, vector<int>, greater<int>> minQ;    // 大顶堆
    int count;
    /** initialize your data structure here. */
    MedianFinder() {
        count = 0;
    }
    
    void addNum(int num) {
        if(count == 0){
            maxQ.push(num);
        }
        else{
            if(num >= maxQ.top()){
                if(maxQ.size() == minQ.size()){
                    minQ.push(num);
                    maxQ.push(minQ.top());
                    minQ.pop();
                }
                else{
                    minQ.push(num);
                }
            }
            else{
                if(maxQ.size() == minQ.size()){
                    maxQ.push(num);
                }
                else{
                    maxQ.push(num);
                    minQ.push(maxQ.top());
                    maxQ.pop();
                }
            }
        }
        count++;
    }
    
    double findMedian() {
        if(count & 1){
            return maxQ.top();
        }
        else{
            return (maxQ.top() + minQ.top()) / 2.0;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```