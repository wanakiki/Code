## 1023. 基于时间的键值存储

2021-07-10 09:43:35

### 题目

创建一个基于时间的键值存储类 ``TimeMap``，它支持下面两个操作：

1. ``set(string key, string value, int timestamp)``


- 存储键 ``key``、值 ``value``，以及给定的时间戳 ``timestamp``。


2. ``get(string key, int timestamp)``


- 返回先前调用 ``set(key, value, timestamp_prev)`` 所存储的值，其中 ``timestamp_prev <= timestamp``。
- 如果有多个这样的值，则返回对应最大的  ``timestamp_prev`` 的那个值。
- 如果没有值，则返回空字符串（``""``）。




**示例 1：**

```
输入：inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
输出：[null,null,"bar","bar",null,"bar2","bar2"]
解释：
TimeMap kv;
kv.set("foo", "bar", 1); // 存储键 "foo" 和值 "bar" 以及时间戳 timestamp = 1
kv.get("foo", 1);  // 输出 "bar"
kv.get("foo", 3); // 输出 "bar" 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"）  

kv.set("foo", "bar2", 4);
kv.get("foo", 4); // 输出 "bar2"
kv.get("foo", 5); // 输出 "bar2"

```

**示例 2：**

```
输入：inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
输出：[null,null,null,"","high","high","low","low"]
```



**提示：**


- 所有的键/值字符串都是小写的。
- 所有的键/值字符串长度都在 ``[1, 100]`` 范围内。
- 所有 ``TimeMap.set`` 操作中的时间戳 ``timestamps`` 都是严格递增的。
- ``1 <= timestamp <= 10^7``
- ``TimeMap.set`` 和 ``TimeMap.get`` 函数在每个测试用例中将（组合）调用总计 ``120000`` 次。



[LeetCode链接](https://leetcode-cn.com/problems/time-based-key-value-store/)

### 思路及代码

由于添加数据时是升序添加的，所以可以直接用数组存储，再二分查找边界数值，不用使用set。

```cpp
struct node{
    int timestamp;
    string value;
    node(int n, string s) : timestamp(n), value(s) {};
};
bool operator<(node a, node b){
    return a.timestamp > b.timestamp;
}

class TimeMap {
    unordered_map<string, set<node>> hash;
public:
    /** Initialize your data structure here. */
    TimeMap() {

    }
    
    // 设置时保持严格升序 读取时并不保证
    void set(string key, string value, int timestamp) {
        hash[key].insert(node(timestamp, value));
    }
    
    string get(string key, int timestamp) {
        if(hash[key].size() == 0){
            return "";
        }
        auto it = hash[key].lower_bound(node(timestamp, ""));
        if(it == hash[key].end()){
            return "";
        }
        else{
            return it->value;
        }
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
 ```