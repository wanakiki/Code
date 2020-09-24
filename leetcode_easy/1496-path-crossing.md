## 1496. 判断路径是否相交

2020年9月24日

### 题目

给你一个字符串 ``path``，其中 ``path[i]`` 的值可以是 ``'N'``、``'S'``、``'E'`` 或者 ``'W'``，分别表示向北、向南、向东、向西移动一个单位。

机器人从二维平面上的原点 ``(0, 0)`` 处开始出发，按 ``path`` 所指示的路径行走。

如果路径在任何位置上出现相交的情况，也就是走到之前已经走过的位置，请返回 ``True`` ；否则，返回 ``False`` 。

 

**示例 1：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/28/screen-shot-2020-06-10-at-123929-pm.png" style="height: 224px; width: 250px;">

```
输入：path = "NES"
输出：false 
解释：该路径没有在任何位置相交。```

**示例 2：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/28/screen-shot-2020-06-10-at-123843-pm.png" style="height: 212px; width: 250px;">

```
输入：path = "NESWW"
输出：true
解释：该路径经过原点两次。```

 

**提示：**


- ``1 <= path.length <= 10^4``
- ``path`` 仅由 ``{'N', 'S', 'E', 'W}`` 中的字符组成


### 思路及代码

这个题目之前在比赛的时候见到过，但是当时没有想到哈希的做法。看了官方题解之后，相对哈希函数的由来做一点补充。这个题目当中，官方题解给出的哈希函数为``f = x * 20001 + y``，为什么是这样呢？首先要知道，哈希函数最重要的成立条件是能保证单一映射，也就是说不同的输入进行运算后，得到的结果也是不同的。

在本题当中，路径数组的长度范围为1~10000，那么相对应横纵坐标的取值区间为[-10000, 10000]，共有20001种可能。这里借用之前微机原理中内存分片的概念，将20001*20001的空间分为20001片，每片长度为20001，片索引为x，片内偏移为y。只不过这里的索引可能为负数。



```cpp
class Solution {
public:
    bool isPathCrossing(string path) {
        auto pairHash = [](const pair<int, int>& o){
            return o.first * 20001 + o.second;
        };

        int x = 0, y = 0;
        unordered_set<pair<int, int>, decltype(pairHash)> visit(0, pairHash);
        visit.emplace(x, y);

        for(char dir: path){
            switch(dir){
                case 'N': ++y; break;
                case 'S': --y; break;
                case 'E': ++x; break;
                case 'W': --x; break; 
            }

            if(visit.find({x, y}) != visit.end()){
                return true;
            }
            else{
                visit.emplace(x, y);
            }
        }
        return false;
    }
};
```
