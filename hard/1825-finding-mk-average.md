## 1825. 求出 MK 平均值

2023-01-18 20:21:13

### 题目

给你两个整数 ``m`` 和 ``k`` ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 <b>MK 平均值</b> 。

**MK 平均值** 按照如下步骤计算：


- 如果数据流中的整数少于 ``m`` 个，**MK 平均值** 为 ``-1`` ，否则将数据流中最后 ``m`` 个元素拷贝到一个独立的容器中。
- 从这个容器中删除最小的 ``k`` 个数和最大的 ``k`` 个数。
- 计算剩余元素的平均值，并 **向下取整到最近的整数** 。


请你实现 ``MKAverage`` 类：


- ``MKAverage(int m, int k)`` 用一个空的数据流和两个整数 ``m`` 和 ``k`` 初始化 **MKAverage** 对象。
- ``void addElement(int num)`` 往数据流中插入一个新的元素 ``num`` 。
- ``int calculateMKAverage()`` 对当前的数据流计算并返回 **MK 平均数** ，结果需 **向下取整到最近的整数** 。


 

**示例 1：**

```
输入：
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
输出：
[null, null, null, -1, null, 3, null, null, null, 5]

解释：
MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3);        // 当前元素为 [3]
obj.addElement(1);        // 当前元素为 [3,1]
obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(10);       // 当前元素为 [3,1,10]
obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10]
                          // 删除最小以及最大的 1 个元素后，容器为 [3]
                          // [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(5);        // 当前元素为 [3,1,10,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5]
                          // 删除最小以及最大的 1 个元素后，容器为 [5]
                          // [5] 的平均值等于 5/1 = 5 ，故返回 5
```

 

**提示：**


- ``3 <= m <= 10<sup>5</sup>``
- ``1 <= k*2 < m``
- ``1 <= num <= 10<sup>5</sup>``
- ``addElement`` 与 ``calculateMKAverage`` 总操作次数不超过 ``10<sup>5</sup>`` 次。



[LeetCode链接](https://leetcode-cn.com/problems/finding-mk-average/)

### 思路及代码

题目在以前参加ACM比赛的时候看到过类似的，并不难，核心点在于如何高效维护 m 个数字，并划分出最大值和最小值。题目更多考察对数据结构的了解，对数据结构的要求是在频繁插入删除的情况下保证有序，不难想到 multiset。

```cpp
class MKAverage {
public:
    multiset<int> min_k;
    multiset<int> max_k;
    multiset<int> mid;
    queue<int> q;
    int m, k;
    long long cur_sum;


    MKAverage(int m, int k) :m(m), k(k) {
        cur_sum = 0;
    }
    
    void addElement(int num) {
        q.push(num);
        if(q.size() <= m){
            mid.insert(num);
            cur_sum += num;
            if(q.size() == m){
                // 移动元素
                while(min_k.size() < k){
                    auto cur = *mid.begin();
                    min_k.insert(cur);
                    cur_sum -= cur;
                    mid.erase(mid.begin());
                }

                while(max_k.size() < k){
                    auto cur = *mid.rbegin();
                    max_k.insert(cur);
                    cur_sum -= cur;
                    mid.erase(prev(mid.end()));
                }
            }
            return ;
        }

        // 判断新插入的数值应该位于哪个集合
        // 如果小于最小集合的最大值放在最小集合
        // 如果大于最大集合的最小值放在最大集合
        // 否则放进 mid
        if(num < (*min_k.rbegin())){
            mid.insert(*min_k.rbegin());
            cur_sum += *min_k.rbegin();
            min_k.erase(prev(min_k.end()));
            min_k.insert(num);
        }
        else if(num > (*max_k.begin())){
            mid.insert(*max_k.begin());
            cur_sum += *max_k.begin();
            max_k.erase(max_k.begin());
            max_k.insert(num);
        }
        else{
            cur_sum += num;
            mid.insert(num);
        }

        // 判断该删除的元素位于哪个集合
        int need_delete = q.front();
        q.pop();
        if(min_k.find(need_delete) != min_k.end()){
            min_k.erase(min_k.find(need_delete));
            min_k.insert(*mid.begin());
            cur_sum -= *mid.begin();
            mid.erase(mid.begin());
        }
        else if(max_k.find(need_delete) != max_k.end()){
            max_k.erase(max_k.find(need_delete));
            max_k.insert(*mid.rbegin());
            cur_sum -= *mid.rbegin();
            mid.erase(prev(mid.end()));
        }
        else{
            cur_sum -= need_delete;
            mid.erase(mid.find(need_delete));
        }
        return ;
    }
    
    int calculateMKAverage() {
        if(q.size() < m)    return -1;
        return cur_sum / (m - k -k);
    }
};

/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage* obj = new MKAverage(m, k);
 * obj->addElement(num);
 * int param_2 = obj->calculateMKAverage();
 */
 ```