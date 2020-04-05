## 460. LFU缓存

2020年4月5日

### 题目

请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。

- get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
- put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近 最少使用的键。

「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

 
进阶:  
你是否可以在 O(1) 时间复杂度内执行两项操作？


示例：
```cpp
LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4
```
来源：力扣（LeetCode）  
链接：https://leetcode-cn.com/problems/lfu-cache

### 代码

接触到这个题目之后想到了要使用哈希表，但是像官方题解那样使用``unordered_map<int, list<Node>>``的思路我并没有想到，于是最后借鉴了官方的做法，自己也有所收获。复现一遍代码之后，发现自己对stl的掌握还不够，需要多加练习。

代码有以下比较精巧的点：

在向list中插入元素时，可以选择在最前面和最后面插入，但前面的效果优于后面，因为在头部插入后可以直接用begin()获取迭代器，在尾部则需要移动一次。

缓存中最小频率的更新有三种情况：
1. 插入新元素，此种情况下最小频率一定为1。
2. 修改元素，此种情况只有在被修改的元素的频率与最小频率相同并且删除元素对应的节点后链表为空时才需要更新最小频率。
3. 访问元素，此种情况最小频率的变化与第二种情况相同。

```cpp
// 定义节点 注意为public属性
class Node{
public:
    int key, value, freq;
    Node(int a, int b, int c):key(a),value(b),freq(c){}
};

class LFUCache {
    int capacity, min_freq; // 容量、最小频率
    // 两个哈希表
    unordered_map<int, list<Node>::iterator> key_table;     // 查找结点信息
    unordered_map<int, list<Node>> freq_table;      // 查找频率信息
public:
    LFUCache(int _capacity) {
        capacity = _capacity;
        min_freq = 0;
        
        // 下面两个清空不是很理解，感觉不是很必要
        key_table.clear();
        freq_table.clear();
    }
    
    int get(int key) {
        if(capacity == 0)   return -1;
        auto it = key_table.find(key);

        // 不在表内，返回-1
        if(it == key_table.end())
            return -1;
        list<Node>::iterator node = it->second;
        int value = node->value;
        int freq = node->freq;
        freq_table[freq].erase(node);     // 频率表删除节点

        // 若对应频率没有值，则释放，并根据频率与最小频率是否相同决定min_freq的值
        if(freq_table[freq].size() == 0){
            freq_table.erase(freq);
            if(min_freq == freq)
                min_freq ++;
        }
        
        // 插入到freq_table更高频率中，并更新key_table
        freq++;
        freq_table[freq].push_front(Node(key, value, freq));
        key_table[key] = freq_table[freq].begin();
        return value;
    }
    
    void put(int key, int value) {
        if(capacity == 0)   return;
        auto it = key_table.find(key);
        if(it == key_table.end()){  // 若无此键则进行插入

            // 若容量已满，删除元素后插入
            if(capacity == key_table.size()){   
                auto i = freq_table[min_freq].back();   // 链表的最后一个节点
                key_table.erase(i.key);     // 查找表删除键值对
                freq_table[min_freq].pop_back();    // 频率表对应频率删除该节点
                
                // 若删除后该频率对应链表为空，则频率表删除键值对
                if(freq_table[min_freq].size() == 0){
                    freq_table.erase(min_freq);
                }
            }

            // 进行插入，下面两步利用了list map的特性，需要理解
            freq_table[1].push_front(Node(key, value, 1));  // 键1对应的空间创建list，并将节点插入到list头部
            key_table[key] = freq_table[1].begin();         // 获取该节点对应迭代器，迭代器不因后续元素插入变化
            min_freq = 1;
        }
        else{   // 对此键对应的值进行修改
            list<Node>::iterator node = it->second;  // it为map的迭代器
            int freq = node->freq;
            freq_table[freq].erase(node);   // 删除对应节点

            // list为空，释放空间
            if(freq_table[freq].size() == 0){
                freq_table.erase(freq);

                // 只有当list被删除之后才需要判断min_freq是否需要更新，很精巧
                if(min_freq == freq)
                    min_freq++;
            }
            freq += 1;
            freq_table[freq].push_front(Node(key, value, freq));
            key_table[key] = freq_table[freq].begin();
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
 ```