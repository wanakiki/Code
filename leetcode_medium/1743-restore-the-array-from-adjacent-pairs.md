## 1743. 从相邻元素对还原数组

2021-07-25 09:45:23

### 题目

存在一个由 ``n`` 个不同元素组成的整数数组 ``nums`` ，但你已经记不清具体内容。好在你还记得 ``nums`` 中的每一对相邻元素。   

给你一个二维整数数组 ``adjacentPairs`` ，大小为 ``n - 1`` ，其中每个 adjacentPairs[i] = [u<sub>i</sub>, v<sub>i</sub>] 表示元素 u<sub>i</sub> 和 v<sub>i</sub> 在 ``nums`` 中相邻。

题目数据保证所有由元素 ``nums[i]`` 和 ``nums[i+1]`` 组成的相邻元素对都存在于 ``adjacentPairs`` 中，存在形式可能是 ``[nums[i], nums[i+1]]`` ，也可能是 ``[nums[i+1], nums[i]]`` 。这些相邻元素对可以 **按任意顺序** 出现。

返回 **原始数组**``nums``。如果存在多种解答，返回 **其中任意一个** 即可。

 

**示例 1：**

```
输入：adjacentPairs = [[2,1],[3,4],[3,2]]
输出：[1,2,3,4]
解释：数组的所有相邻元素对都在 adjacentPairs 中。
特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。
```

**示例 2：**

```
输入：adjacentPairs = [[4,-2],[1,4],[-3,1]]
输出：[-2,4,1,-3]
解释：数组中可能存在负数。
另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。
```

**示例 3：**

```
输入：adjacentPairs = [[100000,-100000]]
输出：[100000,-100000]
```

 

**提示：**


- ``nums.length == n``
- ``adjacentPairs.length == n - 1``
- ``adjacentPairs[i].length == 2``
- ``2 <= n <= 10<sup>5</sup>``
- -10<sup>5</sup> <= nums[i], u<sub>i</sub>, v<sub>i</sub> <= 10<sup>5</sup>
- 题目数据保证存在一些以 ``adjacentPairs`` 作为元素对的数组 ``nums``



[LeetCode链接](https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/)

### 思路及代码

题目给定的限制是数组元素不重复，并且保证能够构成满足要求的数组，在进行拼接时不需要考虑其他特殊情况，找到数组的一个边界（只出现一次的数据）查找其相邻元素进行拼接即可。

首先使用了哈希表统计每个元素的相邻元素，之后使用set记录已经使用过的元素，对数组进行拼接。

```cpp
class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        unordered_map<int, vector<int>> hash;
        int len = adjacentPairs.size() + 1;

        int edge = 0;       // 边缘数据只会出现一次
        for(auto p : adjacentPairs){
            hash[p[0]].push_back(p[1]);
            hash[p[1]].push_back(p[0]);
        }

        for(auto h : hash){
            if(h.second.size() == 1){
                edge = h.first;
                break;
            }
        }

        // 从边缘开始拼接
        vector<int> res(len);
        set<int> s;     // 存储使用过的元素

        int index = 0;
        res[index++] = edge;
        s.emplace(edge);

        while(index < len){
            // 根据当前边缘找到下一个元素
            int next = 0;
            if(hash[edge].size() == 1){
                next = hash[edge][0];
            }
            else{
                if(s.find(hash[edge][0]) == s.end()){
                    next = hash[edge][0];
                }
                else{
                    next = hash[edge][1];
                }
            }

            edge = next;
            res[index++] = edge;
            s.emplace(edge);
        }
        return res;
    }
};
```

上述做法中使用set的目的是判断查找到的数据是否已经使用过，查看官方题解之后发现没有必要使用set进行判断。例如``[[2,1],[3,4],[3,2]]``当使用1作为边界构建数据，可以直接查找到下一个元素为2，对于2而言，与其相邻的两个元素中，一定有一个是上一次访问到的元素，只需要将新元素添加到结果数组当中即可。

```cpp
class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        unordered_map<int, vector<int>> hash;
        int len = adjacentPairs.size() + 1;

        int edge = 0;       // 边缘数据只会出现一次
        for(auto p : adjacentPairs){
            hash[p[0]].push_back(p[1]);
            hash[p[1]].push_back(p[0]);
        }

        for(auto h : hash){
            if(h.second.size() == 1){
                edge = h.first;
                break;
            }
        }

        // 从边缘开始拼接
        vector<int> res(len);
        int index = 0;
        res[index++] = edge;
        res[index++] = hash[edge][0];
        edge = hash[edge][0];

        while(index < len){
            // 根据当前边缘找到下一个元素
            int next = hash[edge][0] == res[index-2] ? hash[edge][1] : hash[edge][0];
            res[index++] = next;
            edge = next;
        }
        return res;
    }
};
```