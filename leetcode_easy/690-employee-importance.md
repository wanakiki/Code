## 690. 员工的重要性

2021-05-01 21:45:52

### 题目

给定一个保存员工信息的数据结构，它包含了员工 **唯一的 id**，**重要度** 和 **直系下属的 id**。

比如，员工 1 是员工 2 的领导，员工 2 是员工 3 的领导。他们相应的重要度为 15 , 10 , 5 。那么员工 1 的数据结构是 [1, 15, [2]] ，员工 2的 数据结构是 [2, 10, [3]] ，员工 3 的数据结构是 [3, 5, []] 。注意虽然员工 3 也是员工 1 的一个下属，但是由于 **并不是直系** 下属，因此没有体现在员工 1 的数据结构中。

现在输入一个公司的所有员工信息，以及单个员工 id ，返回这个员工和他所有下属的重要度之和。

 

**示例：**

```
输入：[[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
输出：11
解释：
员工 1 自身的重要度是 5 ，他有两个直系下属 2 和 3 ，而且 2 和 3 的重要度均为 3 。因此员工 1 的总重要度是 5 + 3 + 3 = 11 。
```

 

**提示：**


- 一个员工最多有一个**直系**领导，但是可以有多个 **直系**下属
- 员工数量不超过 2000 。



[LeetCode链接](https://leetcode-cn.com/problems/employee-importance/)

### 思路及代码

用哈希表存储每个员工对应的数据结构，之后深度优先搜索。起初考虑先排序，但是排序的时间复杂度会高于哈希表。

```cpp
/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    unordered_map<int, Employee*> my_hash;
    int dfs(int id){
        int res = my_hash[id]->importance;
        for(int i = 0; i < my_hash[id]->subordinates.size(); i++){
            res += dfs(my_hash[id]->subordinates[i]);
        }
        return res;
    }
    int getImportance(vector<Employee*> employees, int id) {
        for(auto it : employees){
            my_hash[it->id] = it;
        }
        return dfs(id);
    }
};
```