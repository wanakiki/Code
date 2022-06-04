## 464. 我能赢吗

2022-05-22 13:32:28

### 题目

在 "100 game" 这个游戏中，两名玩家轮流选择从 ``1`` 到 ``10`` 的任意整数，累计整数和，先使得累计整数和 **达到或超过**  100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家 **不能** 重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定两个整数 ``maxChoosableInteger`` （整数池中可选择的最大数）和 ``desiredTotal``（累计和），若先出手的玩家是否能稳赢则返回 ``true`` ，否则返回 ``false`` 。假设两位玩家游戏时都表现
 **最佳** 。



**示例 1：**

```
输入：maxChoosableInteger = 10, desiredTotal = 11
输出：false
解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
```

**示例 2:**

```
输入：maxChoosableInteger = 10, desiredTotal = 0
输出：true
```

**示例 3:**

```
输入：maxChoosableInteger = 10, desiredTotal = 1
输出：true
```



**提示:**


- ``1 <= maxChoosableInteger <= 20``
- ``0 <= desiredTotal <= 300``



[LeetCode链接](https://leetcode-cn.com/problems/can-i-win/)

### 思路及代码

本以为是一道数学题目，但并不能找到规律，尝试用搜索方法进行求解。由于最大可选择的数字不超过 20，因此可以使用一个整数表示目前选择的整数，对搜索空间进行压缩。考虑到双方均采用最佳策略，因此只要有一个策略能够取得正确的结果便可直接返回，需要注意的是，当新选择的数据达不到目标值时，其对应的二进制为以该状态进行搜索时的相反数（即对手失败意味着自己成功）。

```cpp
class Solution {
    public :
unordered_map<int,bool> hash;

    bool helper(int cur_num, int cur_sum, int maxChoosableInteger, int desiredTotal){

        if(!hash.count(cur_num)){
            for(int i = 0; i < maxChoosableInteger; i++){
                if(!((cur_num >> i) & 1)){
                    if(cur_sum + i + 1 >= desiredTotal){
                        hash[cur_num] = true;
                        break;
                    }
                    else{
                        bool tmp = !helper(cur_num | (1 << i), cur_sum + i + 1, maxChoosableInteger, desiredTotal);
                        if(tmp){
                            hash[cur_num] = true;
                            break;
                        }
                    }
                }
            }
        }
        return hash[cur_num];
    }
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if((maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal)  return false;

        return helper(0, 0,maxChoosableInteger, desiredTotal);
    }
};
```