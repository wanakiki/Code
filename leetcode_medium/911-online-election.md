## 911. 在线选举

2021-12-11 11:20:27

### 题目

给你两个整数数组 ``persons`` 和 ``times`` 。在选举中，第 ``i`` 张票是在时刻为 ``times[i]`` 时投给候选人 ``persons[i]`` 的。

对于发生在时刻 ``t`` 的每个查询，需要找出在 ``t`` 时刻在选举中领先的候选人的编号。

在 ``t`` 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。

实现 ``TopVotedCandidate`` 类：


- ``TopVotedCandidate(int[] persons, int[] times)`` 使用 ``persons`` 和 ``times`` 数组初始化对象。
- ``int q(int t)`` 根据前面描述的规则，返回在时刻 ``t`` 在选举中领先的候选人的编号。



**示例：**

```
输入：
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
输出：
[null, 0, 1, 1, 0, 0, 1]

解释：
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。
topVotedCandidate.q(12); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。
topVotedCandidate.q(25); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在平局的情况下，1 是最近获得投票的候选人）。
topVotedCandidate.q(15); // 返回 0
topVotedCandidate.q(24); // 返回 0
topVotedCandidate.q(8); // 返回 1
```



**提示：**


- ``1 <= persons.length <= 5000``
- ``times.length == persons.length``
- ``0 <= persons[i] < persons.length``
- ``0 <= times[i] <= 10<sup>9</sup>``
- ``times`` 是一个严格递增的有序数组
- ``times[0] <= t <= 10<sup>9</sup>``
- 每个测试用例最多调用 ``10<sup>4</sup>`` 次 ``q``



[LeetCode链接](https://leetcode-cn.com/problems/online-election/)

### 思路及代码

对数据进行预处理，使用哈希表保存所有人的累计票数，同时记录最大得票人，同时间存储到数组当中。数据处理结束后，数组按照时间升序存储，可以使用二分查找查询到任意时刻最大得票人。

```cpp
class TopVotedCandidate {
public:
    vector<pair<int, int>> res;

    TopVotedCandidate(vector<int>& persons, vector<int>& times) {
        int max_vote = 0;
        int max_id = -1;
        unordered_map<int, int> hash;
        
        for(int i = 0; i < times.size(); i++){
            int cur_person = persons[i];
            int cur_time = times[i];
            int cur_vote = 0;

            hash[cur_person]++;
            cur_vote = hash[cur_person];

            // 票数相等保存最近获得投票的人
            if(cur_vote >= max_vote){
                max_vote = cur_vote;
                max_id = cur_person;
            }
            res.push_back(make_pair(cur_time, max_id));
        }
    }
    
    int q(int t) {
        // 找到记录投票时间中小于等于当前时间的最大元素
        // 题目保证查找时必然有投票结果

        // 二分查找 已确保存在边界
        int left = 0, right = res.size() - 1;
        while(left < right){
            int mid = left + (right - left + 1) / 2;
            if(res[mid].first == t){
                left = mid;
                break;
            }
            else if(res[mid].first > t){
                right = mid - 1;
            }
            else{
                left = mid;
            }
        }

        return res[left].second;
    }
};

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate* obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj->q(t);
 */
 ```