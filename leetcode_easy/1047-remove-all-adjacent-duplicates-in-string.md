## 1128. 删除字符串中的所有相邻重复项

2021-03-09 09:33:32

### 题目

给出由小写字母组成的字符串 ``S``，**重复项删除操作**会选择两个相邻且相同的
字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。



**示例：**

```
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一 
可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执
行重复项删除操作，所以最后的字符串为 "ca"。
```


**提示：**


- ``1 <= S.length <= 20000``
- ``S`` 仅由小写英文字母组成。


[LeetCode链接](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/)

### 思路及代码

冲动做题导致把简单的问题想复杂，本来可以直接用栈来存储数据，我却想用栈来存储每个被去除部分的左侧下标，越写越不对劲，忽然发现这不就是直接用栈的题吗，傻在当场。

```cpp
class Solution {
public:
    string removeDuplicates(string S) {
        string res;
        for(auto s : S){
            if(!res.empty() && s == res.back()){
                res.pop_back();
            }
            else{
                res.push_back(s);
            }
        }
        return res;
    }
};
```