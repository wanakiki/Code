## 901. 股票价格跨度

2022-10-21 09:59:18

### 题目

编写一个 ``StockSpanner`` 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。

今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

例如，如果未来7天股票的价格是 ``[100, 80, 60, 70, 60, 75, 85]``，那么股票跨度将是 ``[1, 1, 1, 2, 1, 4, 6]``。



**示例：**

```
输入：["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
输出：[null,1,1,1,2,1,4,6]
解释：
首先，初始化 S = StockSpanner()，然后：
S.next(100) 被调用并返回 1，
S.next(80) 被调用并返回 1，
S.next(60) 被调用并返回 1，
S.next(70) 被调用并返回 2，
S.next(60) 被调用并返回 1，
S.next(75) 被调用并返回 4，
S.next(85) 被调用并返回 6。

注意 (例如) S.next(75) 返回 4，因为截至今天的最后 4 个价格
(包括今天的价格 75) 小于或等于今天的价格。
```



**提示：**


- 调用 ``StockSpanner.next(int price)`` 时，将有 ``1 <= price <= 10^5``。
- 每个测试用例最多可以调用  ``10000`` 次 ``StockSpanner.next``。
- 在所有测试用例中，最多调用 ``150000`` 次 ``StockSpanner.next``。
- 此问题的总时间限制减少了 50%。



[LeetCode链接](https://leetcode-cn.com/problems/online-stock-span/)

### 思路及代码

单调栈

```cpp
class Node {
public:
    int val;
    int index;
    Node(int v, int i) : val(v), index(i) {};
};
class StockSpanner {
public:
    stack<Node> stk;
    int index;
    StockSpanner() {
        index = 0;
    }
    
    int next(int price) {
        Node cur_node(price, index++);

        while(!stk.empty() && stk.top().val <= price){
            stk.pop();
        }

        if(stk.empty()){
            stk.push(cur_node);
            return index;
        }
        else{
            int res = index - stk.top().index - 1;
            stk.push(cur_node);
            return res;
        }
        return 1;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
```