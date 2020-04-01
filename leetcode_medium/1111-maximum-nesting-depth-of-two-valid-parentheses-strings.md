## 1111. 有效括号的嵌套深度

2020年4月1日

### 题目

A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

- It is the empty string, or
- It can be written as AB (A concatenated with B), where A and B are VPS's, or
- It can be written as (A), where A is a VPS.

We can similarly define the nesting depth depth(S) of any VPS S as follows:

- depth("") = 0
- depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
- depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

 
Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length).

Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.

 

Example 1:
```no
Input: seq = "(()())"
Output: [0,1,1,1,1,0]
```

Example 2:
```no
Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]
```

Constraints:

- 1 <= seq.size <= 10000

来源：力扣（LeetCode）  
链接：https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings

### 代码

题目比较难理解，读懂题目之后解决问题的方法其实很简单。题目确保字符串有效，在此前提下，如何保证划分的两个子串的深度最小呢？借鉴官方题解的思路，在用栈进行括号匹配验证的基础上，只要保证栈中一半的括号属于A，另一半的括号属于B即可。故有下面解法：

时间复杂度为O(n)，执行时间4ms。

```cpp
class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int count = 0;  // 统计左括号个数
        vector<int> res(seq.size(), 0);
        for(int i = 0; i < seq.size(); i++){
            if(seq[i] == '('){
                count++;
                res[i] = count%2;
            }
            else{
                res[i] = count%2;
                count--;
            }
        }
        return res;
    }
};
```