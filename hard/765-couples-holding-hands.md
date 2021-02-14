## 770. 情侣牵手

2021-02-14 12:16:04

### 题目

N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。一次交换可选择任意两人，让他们站起来交换座位。

人和座位用 ``0`` 到 ``2N-1`` 的整数表示，情侣们按顺序编号，第一对是 ``(0, 1)``，第二对是 ``(2, 3)``，以此类推，最后一对是 ``(2N-2, 2N-1)``。

这些情侣的初始座位  ``row[i]`` 是由最初始坐在第 i 个座位上的人决定的。

**示例 1:**

```
输入: row = [0, 2, 1, 3]
输出: 1
解释: 我们只需要交换row[1]和row[2]的位置即可。
```

**示例 2:**

```
输入: row = [3, 2, 0, 1]
输出: 0
解释: 无需交换座位，所有的情侣都已经可以手牵手了。
```

**说明:**


- ``len(row)`` 是偶数且数值在 ``[4, 60]``范围内。
- 可以保证``row`` 是序列 ``0...len(row)-1`` 的一个全排列。



[LeetCode链接](https://leetcode-cn.com/problems/couples-holding-hands/)

### 思路及代码

每个人的编号除以2并向下取整代表真正对应的组号，当连续两个人组号相同时不需要调整，组号不同时需要调整。当组号不同时，至少有一组连续的两个人同样满足组号不同的条件，此时不同组号之间便建立起了联系，假设参与到该联系当中的数对数为n，则需要n-1次调整。照此思路用并查集来统计需要调整的次数。

```cpp
class Solution {
public:
    int findx(vector<int>& parent, int x){
        if(parent[x] != x){
            parent[x] = findx(parent, parent[x]);
        }
        return parent[x];
    }

    void merge_node(vector<int>& parent, int x, int y){
        int a = findx(parent, x);
        int b = findx(parent, y);
        if(a != b){
            parent[b] = a;
        }
    }

    int minSwapsCouples(vector<int>& row) {
        int res = 0;
        int len = row.size();
        vector<int> parent(len / 2, 0);
        for(int i = 0; i < parent.size(); i++){
            parent[i] = i;
        }

        for(int i = 0; i < len; i+=2){
            int x = row[i] / 2;
            int y = row[i+1] / 2;
            merge_node(parent, x, y);
        }

        unordered_map<int, int> count;
        for(int i = 0; i < parent.size(); i++){
            count[findx(parent, parent[i])]++;  // 注意并查集可能有两层
        }
        for(auto i : count){
            res += i.second - 1;
        }
        return res;
    }
};
```