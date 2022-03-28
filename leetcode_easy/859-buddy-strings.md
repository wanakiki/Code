## 889. 亲密字符串

2021-11-23 21:27:55

### 题目

给你两个字符串 ``s`` 和 ``goal`` ，只要我们可以通过交换 ``s`` 中的两个字母得到与 ``goal`` 相等的结果，就返
回 ``true`` ；否则返回 ``false`` 。

交换字母的定义是：取两个下标 ``i`` 和 ``j`` （下标从 ``0`` 开始）且满足 ``i != j`` ，接着交换 ``s[i]`` 和 ``s[j]`` 处的字符。


- 例如，在 ``"abcd"`` 中交换下标 ``0`` 和下标 ``2`` 的元素可以生成 ``"cbad"`` 。




**示例 1：**

```

输入：s = "ab", goal = "ba"
输出：true
解释：你可以交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 相等。```

**示例 2：**

```

输入：s = "ab", goal = "ab"
输出：false
解释：你只能交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 不相等。```

**示例 3：**

```

输入：s = "aa", goal = "aa"
输出：true
解释：你可以交换 s[0] = 'a' 和 s[1] = 'a' 生成 "aa"，此时 s 和 goal 相等。
```

**示例 4：**

```

输入：s = "aaaaaaabc", goal = "aaaaaaacb"
输出：true
```



**提示：**


- ``1 <= s.length, goal.length <= 2 * 10<sup>4</sup>``
- ``s`` 和 ``goal`` 由小写英文字母组成



[LeetCode链接](https://leetcode-cn.com/problems/buddy-strings/)

### 思路及代码

又臭又长的代码，受问题限制，解法很难被优化，很难变得简练。

```
class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if(s.size() != goal.size()) return false;

        vector<int> count_a(26, 0);
        vector<int> diff;
        for(int i = 0; i < s.size(); i++){
            count_a[s[i] - 'a']++;

            if(s[i] != goal[i]){
                diff.push_back(i);

                if(diff.size() > 2) return false;
            }
        }

        if(diff.size() == 0){
            // 判断字符串中是否有个数大于2的字母
            bool flag = false;
            for(int i = 0; i < count_a.size(); i++){
                if(count_a[i] > 1){
                    flag = true;
                    break;
                }
            }

            if(flag == false)   return false;
        }
        else{
            if(diff.size() != 2 || (s[diff[0]] != goal[diff[1]]) || (s[diff[1]] != goal[diff[0]]))    return false;
        }
        return true;
    }
};
```