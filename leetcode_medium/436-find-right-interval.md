## 436. 寻找右区间

2022-05-20 09:37:30

### 题目

给你一个区间数组 ``intervals`` ，其中 ``intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]`` ，且每个 ``start<sub>i</sub>`` 都 **不同** 。 

区间 ``i`` 的 **右侧区间** 可以记作区间 ``j`` ，并满足 ``start<sub>j</sub>```` >= end<sub>i</sub>`` ，且 ``start<sub>j</sub>`` **最小化**。

返回一个由每个区间 ``i`` 的 **右侧区间** 的最小起始位置组成的数组。如果某个区间 ``i`` 不存在对应的 **右侧区间** ，则下标 ``i`` 处的值设为 ``-1`` 。


**示例 1：**

```
输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。
```

**示例 2：**

```
输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。
```

**示例 3：**

```
输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
```



**提示：**


- ``1 <= intervals.length <= 2 * 10<sup>4</sup>``
- ``intervals[i].length == 2``
- ``-10<sup>6</sup> <= start<sub>i</sub> <= end<sub>i</sub> <= 10<sup>6</sup>``
- 每个间隔的起点都 **不相同**



[LeetCode链接](https://leetcode-cn.com/problems/find-right-interval/)

### 思路及代码

需要注意，题目数据中每个间隔的左端点均不相同。

将原数组备份一份，之后按照数据左端点进行升序排序。使用哈希表分别存储排序后数组和排序前数组左右端点值对应的索引（左端点唯一），遍历备份数组，对于每个元素找到其在排序后数组中的位置及其对应的下一个区间，根据是否存在下一个区间向结果中添加数值。

```cpp
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        vector<vector<int>> backup = intervals;
        sort(intervals.begin(), intervals.end(), [&](const vector<int> a, const vector<int> b){
            return a[0] < b[0];
        });

        unordered_map<int, int> hash;
        for(int i = 0; i < intervals.size(); i++){
            hash[intervals[i][0]] = i;
        }
        unordered_map<int, int> hash_backup;
        for(int i = 0; i < backup.size(); i++){
            hash_backup[backup[i][0]] = i;
        }

        vector<int> res;
        for(int i = 0; i < backup.size(); i++){
            int cur_index = hash[backup[i][0]];

            int cur_end = backup[i][1];
            bool flag = false;
            while(cur_index < backup.size()){
                if(intervals[cur_index][0] >= cur_end){
                    res.push_back(hash_backup[intervals[cur_index][0]]);
                    flag = true;
                    break;
                }
                cur_index++;
            }

            if(!flag)   res.push_back(-1);
        }
        return res;
    }
};
```

上面代码勉强通过了测试，但整体实现比较粗糙，排序后数组真正有意义的是左端点，因此可以将排序后数组的右端点值修改为原数组中的位置，节约哈希表的空间。在数据长度较大时，顺序搜索也将消耗较多循环，可以使用二分查找进行加速。