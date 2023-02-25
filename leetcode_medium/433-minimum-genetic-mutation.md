## 433. 最小基因变化

2022-05-07 10:13:51

### 题目

基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 ``'A'``、``'C'``、``'G'`` 和 ``'T'`` 之一。

假设我们需要调查从基因序列 ``start`` 变为 ``end`` 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。


- 例如，``"AACCGGTT" --> "AACCGGTA"`` 就是一次基因变化。


另有一个基因库 ``bank`` 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。

给你两个基因序列 ``start`` 和 ``end`` ，以及一个基因库 ``bank`` ，请你找出并返回能够使 ``start`` 变化为 ``end`` 所需的最少变化次数。如果无法完成此基因变化，返回 ``-1`` 。

注意：起始基因序列 ``start`` 默认是有效的，但是它并不一定会出现在基因库中。



**示例 1：**

```
输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1
```

**示例 2：**

```
输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2
```

**示例 3：**

```
输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
输出：3
```



**提示：**


- ``start.length == 8``
- ``end.length == 8``
- ``0 <= bank.length <= 10``
- ``bank[i].length == 8``
- ``start``、``end`` 和 ``bank[i]`` 仅由字符 ``['A', 'C', 'G', 'T']`` 组成



[LeetCode链接](https://leetcode-cn.com/problems/minimum-genetic-mutation/)

### 思路及代码

题目数据量比较小，可以直接进行广搜。可以在搜索前直接计算出 bank 中满足跳转关系的点，直接以图的形式存储，可以减少一些额外判断。

```cpp
class Solution {
public:
    unordered_map<string, int> hash;

    int minMutation(string start, string end, vector<string>& bank) {
        hash[start] = 1;
        for(auto s : bank){
            hash[s] = 1;
        }
        if(hash.find(end) == hash.end())    return -1;  // 终止序列需要在 bank 内

        queue<string> q;
        q.emplace(start);
        int count = 0;
        bool flag = true;
        while(!q.empty() && flag){
            int n = q.size();
            count++;
            while(n--){
                string cur = q.front();
                q.pop();

                if(cur == end){
                    flag = false;
                    break;
                }

                if(hash.find(cur) != hash.end() && hash[cur] == 1){
                    for(int i = 0; i < 8; i++){
                        for(auto c : {'A', 'C', 'G', 'T'}){
                            if(cur[i] != c){
                                string tmp = cur;
                                tmp[i] = c;
                                q.push(tmp);
                            }
                        }
                    }
                    hash[cur] = 0;
                }
            }
        }

        if(flag)    return -1;
        else    return count-1;
    }
};
```