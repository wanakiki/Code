## 146. LRU缓存机制

2020年5月25日

### 题目

运用你所掌握的数据结构，设计和实现一个  <a href="https://baike.baidu.com/item/LRU" target="_blank">LRU (最近最少使用) 缓存机制</a>。它应该支持以下操作： 获取数据 ``get`` 和 写入数据 ``put`` 。

获取数据 ``get(key)`` - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。

写入数据 ``put(key, value)`` - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

**进阶:**

你是否可以在 **O(1)** 时间复杂度内完成这两种操作？

 

**示例:**

```
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
```

### 代码

前不久刚做了LFU缓存机制，现在来做LRU感觉轻松了不少。

因为LRU要求删除的元素是最久未使用的元素，比较合适的维护方式是使用双向链表，最近访问或者插入过的元素放在前面，最后面的元素对应的就是当前状态下最久未使用的元素。

由于缓存要求``get``操作也在常数时间内完成，自然而然想到了使用哈希表存储每一个key，然后用key在哈希表中查找元素。

这里借鉴之前写过的LFU缓存的做法，哈希表的值对应双向列表的迭代器，双向列表中存储key对应的value值。这样读取数据的流程就是先通过哈希表找到对应的迭代器，再通过迭代器获得对应的值。

本以为到这里就结束了，写代码的过程中才发现漏掉了存数据的一环。当缓存装满后，数据的存入需要删掉最久未使用的值，我们可以通过双向列表快速得到键值对中的值，但是没有办法得到需要删除的键。这样哈希表中的元素无法删除，所以需要对双向列表存储的内容进行修改，将原本的值改为键值对，这样就能满足要求。

```cpp
class LRUCache {
public:
    int capacity;
    int cur_num;
    list<pair<int, int>> mylist;    // 删除时需要用链表节点查找key 链表存储结构为<value, key>
    unordered_map<int, list<pair<int, int>>::iterator> myhash;

    void helper(){
        for(auto i = mylist.begin(); i != mylist.end(); i++){
            cout << "value" << i->first << " key" << i->second << ' ';
        }
        cout << endl;

        for(auto i = myhash.begin(); i != myhash.end(); i++){
            cout << "key" << i->first << ' ';
        }
        cout << endl;
    }
    LRUCache(int x) {
        capacity = x;
        cur_num = 0;
    }
    
    int get(int key) {
        auto it = myhash.find(key);
        if(it != myhash.end()){
            auto it_list = it->second;

            int res = it_list->first;
            mylist.erase(it_list);
            mylist.push_front(make_pair(res, key));
            myhash[key] = mylist.begin();

            return res;
        }
        else{
            return -1;
        }
    }
    
    void put(int key, int value) {
        auto it = myhash.find(key);

        // 如果已经存放 需要删掉原有节点
        if(it != myhash.end()){
            mylist.erase(it->second);
            cur_num -= 1;
        }
        else{
            // 没有存放需要根据内部空间情况判断是否需要删除
            if(cur_num == capacity){
                int need_del = mylist.back().second;
                mylist.pop_back();  // 链表尾部删除
                myhash.erase(myhash.find(need_del));
                cur_num -= 1;
            }
        }
        
        // 避免空间小于等于零
        if(cur_num < capacity){
            mylist.emplace_front(value, key);
            myhash[key] = mylist.begin();
            cur_num ++;
        }
    }
};                                                     
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
 ```

 击败了44%的提交，代码应该还可以优化。