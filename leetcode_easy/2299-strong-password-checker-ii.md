## 2299. 强密码检验器 II

2023-01-19 09:30:08

### 题目

如果一个密码满足以下所有条件，我们称它是一个 **强** 密码：


- 它有至少 ``8`` 个字符。
- 至少包含 **一个小写英文** 字母。
- 至少包含 **一个大写英文** 字母。
- 至少包含 **一个数字** 。
- 至少包含 **一个特殊字符** 。特殊字符为：``"!@#$%^&amp;*()-+"`` 中的一个。
- 它 **不** 包含 ``2`` 个连续相同的字符（比方说 ``"aab"`` 不符合该条件，但是 ``"aba"`` 符合该条件）。


给你一个字符串 ``password`` ，如果它是一个 **强** 密码，返回 ``true``，否则返回 ``false`` 。

 

**示例 1：**

```
输入：password = "IloveLe3tcode!"
输出：true
解释：密码满足所有的要求，所以我们返回 true 。
```

**示例 2：**

```
输入：password = "Me+You--IsMyDream"
输出：false
解释：密码不包含数字，且包含 2 个连续相同的字符。所以我们返回 false 。
```

**示例 3：**

```
输入：password = "1aB!"
输出：false
解释：密码不符合长度要求。所以我们返回 false 。
```

 

**提示：**


- ``1 <= password.length <= 100``
- ``password`` 包含字母，数字和 ``"!@#$%^&amp;*()-+"`` 这些特殊字符。



[LeetCode链接](https://leetcode-cn.com/problems/strong-password-checker-ii/)

### 思路及代码

扫描字符串，并判断题目给出的条件是否满足。

```cpp
class Solution {
public:
    bool strongPasswordCheckerII(string password) {
        if(password.size() < 8) return false;
        bool low_flag = false;
        bool up_flag = false;
        bool digit_flag = false;
        bool special_flag = false;

        for(int i = 0; i < password.size(); i++){
            if(!low_flag){
                if('a' <= password[i] && password[i] <= 'z'){
                    low_flag = true;
                }
            }

            if(!up_flag){
                if('A' <= password[i] && password[i] <= 'Z'){
                    up_flag = true;
                }
            }

            if(!digit_flag){
                if('0' <= password[i] && password[i] <= '9'){
                    digit_flag = true;
                }
            }

            if(!special_flag){
                string target = "!@#$%^&*()-+";
                for(auto t : target){
                    if(t == password[i]){
                        special_flag = true;
                        break;
                    }
                }
            }

            if(i != 0 && password[i] == password[i-1]){
                return false;
            }
        }
        return low_flag & up_flag & digit_flag & special_flag;
    }
};
```