## 816. 设计哈希集合

2021-03-13 11:53:09

### 题目

不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 ``MyHashSet`` 类：


- ``void add(key)`` 向哈希集合中插入值 ``key`` 。
- ``bool contains(key)`` 返回哈希集合中是否存在这个值 ``key`` 。
- ``void remove(key)`` 将给定值 ``key`` 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

 

**示例：**

```
输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]

解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）
```

 

**提示：**


- ``0 <= key <= 10<sup>6</sup>``
- 最多调用 ``10<sup>4</sup>`` 次 ``add``、``remove`` 和 ``contains`` 。


 

**进阶：** 你可以不使用内建的哈希集合库解决此问题吗？


[LeetCode链接](https://leetcode-cn.com/problems/design-hashset/)

### 思路及代码

```cpp
class MyHashSet {
public:
    /** Initialize your data structure here. */
    vector<list<int>> data;
    static const int base = 769;
    static int hash(int key) {
        return key % base;
    }

    MyHashSet() : data(base){}
    
    void add(int key) {
        int index = hash(key);
        for(auto it = data[index].begin(); it != data[index].end(); it++){
            if(*it == key){
                return ;
            }
        }
        data[index].push_back(key);
    }
    
    void remove(int key) {
        int index = hash(key);
        for(auto it = data[index].begin(); it != data[index].end(); it++){
            if(*it == key){
                data[index].erase(it);
                return;
            }
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int index = hash(key);
        for(auto it = data[index].begin(); it != data[index].end(); it++){
            if(*it == key){
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
 ```


> 为了实现哈希集合这一数据结构，有以下几个关键问题需要解决：  
> - 哈希函数：能够将集合中任意可能的元素映射到一个固定范围的整数值，并将该元素存储到整数值对应的地址上。
> - 冲突处理：由于不同元素可能映射到相同的整数值，因此需要在整数值出现「冲突」时，需要进行冲突处理。总的来说，有以下几种策略解决冲突
>   - 链地址法：为每个哈希值维护一个链表，并将具有相同哈希值的元素都放入这一链表当中。
>   - 开放地址法：当发现哈希值 hh 处产生冲突时，根据某种策略，从 hh 出发找到下一个不冲突的位置。例如，一种最简单的策略是，不断地检查 h+1,h+2,h+3,… 这些整数对应的位置。
>   - 再哈希法：当发现哈希冲突后，使用另一个哈希函数产生一个新的地址。
> - 扩容：当哈希表元素过多时，冲突的概率将越来越大，而在哈希表中查询一个元素的效率也会越来越低。因此，需要开辟一块更大的空间，来缓解哈希表中发生的冲突。
> 
> 作者：LeetCode-Solution
> 
> 链接：https://leetcode-cn.com/problems/design-hashset/solution/she-ji-ha-xi-ji-he-by-leetcode-solution-xp4t/
> 
> 来源：力扣（LeetCode）
