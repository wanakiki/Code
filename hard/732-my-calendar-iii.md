## 732. 我的日程安排表 III

2022-06-07 09:19:27

### 题目

当 ``k`` 个日程安排有一些时间上的交叉时（例如 ``k`` 个日程安排都在同一时间内），就会产生 ``k`` 次预订。

给你一些日程安排 ``[start, end)`` ，请你在每个日程安排添加后，返回一个整数 ``k`` ，表示所有先前日程安排会产生的最大 ``k`` 次预订。

实现一个 ``MyCalendarThree`` 类来存放你的日程安排，你可以一直添加新的日程安排。


- ``MyCalendarThree()`` 初始化对象。
- ``int book(int start, int end)`` 返回一个整数 ``k`` ，表示日历中存在的 ``k`` 次预订的最大值。


 

**示例：**

```
输入：
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
输出：
[null, 1, 1, 2, 3, 3, 3]

解释：
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
myCalendarThree.book(5, 10); // 返回 3
myCalendarThree.book(25, 55); // 返回 3
```

 

**提示：**


- ``0 <= start < end <= 10<sup>9</sup>``
- 每个测试用例，调用 ``book`` 函数最多不超过 ``400``次



[LeetCode链接](https://leetcode-cn.com/problems/my-calendar-iii/)

### 思路及代码

看完题目之后就感觉是一个线段树的经典应用题，但无奈到现在了动态开点还不熟练，于是乎参照了官方题解实现了线段树动态开点的做法，使用哈希表存储每个点的索引，不使用数组或者指针方式，实现起来比较简单。

```cpp
class MyCalendarThree {
public:
    unordered_map<int, pair<int,int>> tree; // 使用哈希表动态开点   second 对应懒惰标记
    MyCalendarThree() {

    }
    
    int book(int start, int end) {
        update(0, 1e9, start, end - 1, 1);
        return tree[1].first;
    }
    void update(int left, int right, int start, int end, int index){
        if(start > right || end < left) return ;
        if(left >= start && right <= end){
            tree[index].first++;
            tree[index].second++;
        }
        else{
            int mid = (left + right) >> 1;
            update(left, mid, start, end, 2 * index);
            update(mid + 1, right, start, end, 2*index+1);

            tree[index].first = tree[index].second + max(tree[2 * index].first, tree[2 * index + 1].first);
        }
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */
```

但实际上考虑到数据长度只有四百，直接用差分数组保存数值，查询结果时对数组累加并取最大也可以完成题目要求。

```cpp
class MyCalendarThree {
public:
    map<int,int> hash;
    MyCalendarThree() {

    }
    
    int book(int start, int end) {
        hash[start]++;
        hash[end]--;
        int res = 0;
        int cur = 0;
        for(auto it = hash.begin(); it != hash.end(); it++){
            cur += it->second;
            res = max(res, cur);
        }
        return res;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */
```

为进一步减少空间利用，使用了 map 对插入点索引进行保存。
