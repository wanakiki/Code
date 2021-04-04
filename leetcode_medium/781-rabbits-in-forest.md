## 797. 森林中的兔子

2021-04-04 11:48:00 

### 题目

森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 ``answers`` 数组里。

返回森林中兔子的最少数量。

```
示例:
输入: answers = [1, 1, 2]
输出: 5
解释:
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。

输入: answers = [10, 10, 10]
输出: 11

输入: answers = []
输出: 0
```

**说明:**


- ``answers`` 的长度最大为``1000``。
- ``answers[i]`` 是在 ``[0, 999]`` 范围内的整数。



[LeetCode链接](https://leetcode-cn.com/problems/rabbits-in-forest/)

### 思路及代码

```cpp
class Solution {
public:
    // 根据相同回答的个数计算可能的最小兔子数量
    int helper(int ans, int count){
        int res = 0;
        int real_num = ans + 1;     // 每一个回答对应的相同颜色个数应该加上本身

        int total_group = count / real_num;
        if(count % real_num){
            total_group += 1;
        }
        res += total_group * real_num;
        return res;
    }
    int numRabbits(vector<int>& answers) {
        int res = 0;
        if(answers.size() == 0) return res;

        sort(answers.begin(), answers.end());
        int count = 1, last = answers[0];

        for(int i = 1; i < answers.size(); i++){
            if(answers[i] == last){
                count++;
            }
            else{
                res += helper(last, count);
                last = answers[i];
                count = 1;
            }
        }
        res += helper(last, count);
        return res;
    }
};
```

类似脑筋急转弯的题，上面的做法可以解决，但是很多地方可以进行优化。首先可以不排序，直接使用哈希表来统计数字的出现次数，其次，在实现向上取整时可以使用``(count + ans) / (ans + 1)``写法。