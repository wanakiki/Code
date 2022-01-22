## 1447. 跳跃游戏 IV

2022-01-22 16:55:11

### 题目

给你一个整数数组 ``arr`` ，你一开始在数组的第一个元素处（下标为 0）。

每一步，你可以从下标 ``i`` 跳到下标：


- ``i + 1`` 满足：``i + 1 < arr.length``
- ``i - 1`` 满足：``i - 1 >= 0``
- ``j`` 满足：``arr[i] == arr[j]`` 且 ``i != j``


请你返回到达数组最后一个元素的下标处所需的 **最少操作次数** 。

注意：任何时候你都不能跳到数组外面。



**示例 1：**

```
输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
输出：3
解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。 
```

**示例 2：**

```
输入：arr = [7]
输出：0
解释：一开始就在最后一个元素处，所以你不需要跳跃。
```

**示例 3：**

```
输入：arr = [7,6,9,6,9,6,9,7]
输出：1
解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
```

**示例 4：**

```
输入：arr = [6,1,9]
输出：2
```

**示例 5：**

```
输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
输出：3
```



**提示：**


- ``1 <= arr.length <= 5 * 10^4``
- ``-10^8 <= arr[i] <= 10^8``



[LeetCode链接](https://leetcode-cn.com/problems/jump-game-iv/)

### 思路及代码

元素之间存在负载的引用关系，直接使用动态规划尝试找到走到位置i的最短步数不是很现实。

尝试使用广度优先搜索，发现卡在了较大的具有相同数值的输入上，需要对相同元素子集进行额外处理。由于问题的本质原因在于相同元素子集为完全图，节点与节点之间存在较多的连接数目，需要对节点间连接进行处理，避免重复加入。

总体思路如下：

使用哈希表存储相同元素子集，从首个节点开始广度优先搜索数组，遇到元素后，将相同元素子集中的所有元素添加到下一层的搜索当中，并删除当前相同元素子集避免重复访问，其余步骤和常见BFS一致，在搜索过程中一旦找到最终节点即可返回当前步数。

```cpp
class Solution {
public:
    int minJumps(vector<int>& arr) {
        // 统计具有相同值的元素对应索引
        unordered_map<int, vector<int>> hash;
        
        for(int i = 0; i < arr.size(); i++){
            if(hash.find(arr[i]) == hash.end()){
                hash[arr[i]] = {i};
            }
            else{
                hash[arr[i]].push_back(i);
            }
        }


        // 广度优先搜索查找路径
        queue<int> q;
        vector<int> steps(arr.size(), -1);  // 标记访问到对应元素的最短路径
        q.push(0);
        int cur_step = 0;

        while(!q.empty()){
            int count = q.size();
            while(count--){
                int cur_index = q.front();
                q.pop();

                // 如果已经访问则不进行处理
                // 如果是最终元素则返回当前步数
                // 如果是其他未访问元素则增加叶子节点
                if(steps[cur_index] != -1)  continue;
                else if(cur_index == arr.size() - 1)    return cur_step;
                else {
                    steps[cur_index] = cur_step;
                    if(cur_index != 0)  q.push(cur_index - 1);
                    q.push(cur_index + 1);
                    
                    // 一旦访问到相同数值集中的元素 第一个元素对应步数为cur_step，其他元素对应步数为cur_step+1，需要在当前轮次入队
                    if(hash.find(arr[cur_index]) != hash.end() &&  hash[arr[cur_index]].size() != 1){
                        for(auto i : hash[arr[cur_index]]){
                            if(steps[i] != -1)  continue;
                            else{
                                q.push(i);
                            }
                        }
                    }

                    // 入队后删除当前相同数值集
                    // 此步骤很关键，避免了数值集中的元素频繁入队
                    hash.erase(arr[cur_index]);
                }
            }
            cur_step++;
        }
        return 0;
    }
};
```