## 2123. 游戏中弱角色的数量

2022-01-28 12:19:50

### 题目

你正在参加一个多角色游戏，每个角色都有两个主要属性：**攻击** 和 **防御** 。给你一个二维整数数组 ``properties`` ，其中 properties[i] = [attack<sub>i</sub>, defense<sub>i</sub>] 表示游戏中第 ``i`` 个角色的属性。

如果存在一个其他角色的攻击和防御等级 **都严格高于** 该角色的攻击和防御等级，则认为该角色为 **弱角色** 。更正式地，如果认为角色 ``i`` **弱于** 
存在的另一个角色 ``j`` ，那么 attack<sub>j</sub> > attack<sub>i</sub> 且 defense<sub>j</sub> > defense<sub>i</sub> 。

返回 **弱角色** 的数量。



**示例 1：**

```
输入：properties = [[5,5],[6,3],[3,6]]
输出：0
解释：不存在攻击和防御都严格高于其他角色的角色。
```

**示例 2：**

```
输入：properties = [[2,2],[3,3]]
输出：1
解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
```

**示例 3：**

```
输入：properties = [[1,5],[10,4],[4,3]]
输出：1
解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
```



**提示：**


- ``2 <= properties.length <= 10<sup>5</sup>``
- ``properties[i].length == 2``
- 1 <= attack<sub>i</sub>, defense<sub>i</sub> <= 10<sup>5</sup>



[LeetCode链接](https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game/)

### 思路及代码

对攻击力升序排序，对于攻击力相同的情况按照防御力升序排序，在此基础上从后向前遍历数组，保留历史最大防御力和当前攻击力数值对应子集的最大防御力，在攻击力数值发生变化时更新历史最大防御力。

```cpp
class Solution {
public:
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        sort(properties.begin(), properties.end(), [&](vector<int>& a, vector<int>& b){
            if(a[0] == b[0])    return a[1] < b[1];
            return a[0] < b[0];
        });

        int history_max = 0;
        int cur_max = 0;
        int res = 0;
        for(int i = properties.size() - 1; i >= 0; i--){
            if(i < properties.size() - 1 && properties[i][0] != properties[i+1][0]){
                history_max = max(history_max, cur_max);
                cur_max = 0;
            }

            if(properties[i][1] < history_max)  res ++;
            cur_max = max(cur_max, properties[i][1]);
        }
        return res;
    }
};
```