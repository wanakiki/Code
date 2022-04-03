## 1710. 找到处理最多请求的服务器

2022-03-30 14:12:34

### 题目

你有 ``k`` 个服务器，编号为 ``0`` 到 ``k-1`` ，它们可以同时处理多个请求组。每个服务器有无穷的计算能力但是 **不能同时处理超过一个请求** 。请求分配到服务器的规则如下：


- 第 ``i`` （序号从 0 开始）个请求到达。
- 如果所有服务器都已被占据，那么该请求被舍弃（完全不处理）。
- 如果第 ``(i % k)`` 个服务器空闲，那么对应服务器会处理该请求。
- 否则，将请求安排给下一个空闲的服务器（服务器构成一个环，必要的话可能从第 0 个服务器开始继续找下一个空闲的服务器）。比方说，如果第 ``i`` 个服务器在忙，那么会查看第 ``(i+1)`` 个服务器，第 ``(i+2)`` 个服务器等等。


给你一个 **严格递增** 的正整数数组 ``arrival`` ，表示第 ``i`` 个任务的到达时间，和另一个数组 ``load`` ，其中 ``load[i]`` 表示第 ``i`` 个请求的工作量（也就是服务器完成它所需要的时间）。你的任务是 
找到 **最繁忙的服务器** 。最繁忙定义为一个服务器处理的请求数是所有服务器里最多的。

请你返回包含所有 **最繁忙服务器** 序号的列表，你可以以任意顺序返回这个列表。



**示例 1：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/03/load-1.png" style="height: 221px; width: 389px;" />

```
输入：k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]
输出：[1]
解释：
所有服务器一开始都是空闲的。
前 3 个请求分别由前 3 台服务器依次处理。
请求 3 进来的时候，服务器 0 被占据，所以它被安排到下一台空闲的服务器，也就是服务器 1 。
请求 4 进来的时候，由于所有服务器都被占据，该请求被舍弃。
服务器 0 和 2 分别都处理了一个请求，服务器 1 处理了两个请求。所以服务器 1 是最忙的服务器。
```

**示例 2：**

```
输入：k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
输出：[0]
解释：
前 3 个请求分别被前 3 个服务器处理。
请求 3 进来，由于服务器 0 空闲，它被服务器 0 处理。
服务器 0 处理了两个请求，服务器 1 和 2 分别处理了一个请求。所以服务器 0 是最忙的服务器。
```

**示例 3：**

```
输入：k = 3, arrival = [1,2,3], load = [10,12,11]
输出：[0,1,2]
解释：每个服务器分别处理了一个请求，所以它们都是最忙的服务器。
```

**示例 4：**

```
输入：k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
输出：[1]
```

**示例 5：**

```
输入：k = 1, arrival = [1], load = [1]
输出：[0]
```



**提示：**


- ``1 <= k <= 10<sup>5</sup>``
- ``1 <= arrival.length, load.length <= 10<sup>5</sup>``
- ``arrival.length == load.length``
- ``1 <= arrival[i], load[i] <= 10<sup>9</sup>``
- ``arrival`` 保证 **严格递增** 。



[LeetCode链接](https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests/)

### 思路及代码

个人看来题目更多考察的点是对于数据结构的利用，读完题目之后，很容易想到的是使用哈希表存储每个服务器的使用次数，使用堆存储当前的任务队列便于弹出已经结束的任务。起初我并没有想到如何维护可用服务器列表，计划直接使用数组进行存储，容易想到的是在程序执行一段时间之后，可用服务器列表可能会变得比较零散，此时进行查找会伴随较多无用操作。

set 是我平时做题时比较少用的一种数据结构，看了官方题解之后才回想起来 set 具备 lower_bound 这样的查找功能，恰好满足本题目维护空闲服务器列表的要求。

剩下的工作便是使用上述数据结构对整个过程进行模拟。

```cpp
class Solution {
public:
    struct cmp{
        bool operator()(pair<int,int>& a, pair<int,int>& b){
            return a.first > b.first;
        }
    };
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        vector<int> count(k, 0);
        set<int> free_server;
        priority_queue<pair<int,int>, vector<pair<int,int>>, cmp> q;
        int max_val = 0;


        // 将所有的服务器添加到空闲服务器中
        for(int i = 0; i < k; i++){
            free_server.emplace(i);
        }

        // 对于每个到来的请求时间，将堆中已空闲的服务器移动到set中，并在set中查找满足服务器使用条件的服务器
        for(int i = 0; i < arrival.size(); i++){
            // 清除堆中任务结束时间小于等于新请求到达时间的服务器
            while(!q.empty()){
                auto p = q.top();
                if(p.first <= arrival[i]){
                    free_server.emplace(p.second);
                    q.pop();
                }
                else{
                    break;
                }
            }

            // for(auto it = free_server.begin(); it != free_server.end(); it++){
            //     cout << *it << endl;
            // }
            // cout << endl;
            // 在set中选择对应服务器
            // 首先查找不小于目标值的第一个元素 如果查找不到则返回最小元素 或者没有空闲服务器 丢弃
            auto it = free_server.lower_bound(i % k);
            if(it != free_server.end()){
                int server_id = *it;
                count[server_id]++;
                max_val = max(max_val, count[server_id]);
                q.emplace(make_pair(arrival[i] + load[i], server_id));

                free_server.erase(it);
            }
            else{
                // 查找不到可能已经为空
                if(free_server.empty()){
                    continue;
                }
                else{
                    int server_id = *free_server.begin();
                    count[server_id]++;
                    max_val = max(max_val, count[server_id]);
                    q.emplace(make_pair(arrival[i] + load[i], server_id));

                    free_server.erase(free_server.begin());
                }
            }
        }
        vector<int> res;
        for(int i = 0; i < count.size(); i++){
            if(count[i] == max_val){
                res.push_back(i);
            }
        }
        return res;
    }
};
```