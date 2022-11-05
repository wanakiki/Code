## 1106. 解析布尔表达式

2022-11-05 15:58:17

### 题目

给你一个以字符串形式表述的 <a href="https://baike.baidu.com/item/%E5%B8%83%E5%B0%94%E8%A1%A8%E8%BE%BE%E5%BC%8F/1574380?fr=aladdin" target="_blank">布尔表达式</a>（boolean） ``expression``，返回该式的运算结果。

有效的表达式需遵循以下约定：


- ``"t"``，运算结果为 ``True``
- ``"f"``，运算结果为 ``False``
- ``"!(expr)"``，运算过程为对内部表达式 ``expr`` 进行逻辑 **非的运算**（NOT）
- ``"&amp;(expr1,expr2,...)"``，运算过程为对 2 个或以上内部表达式 ``expr1, expr2, ...`` 进行逻辑 **与的运算**（AND）
- ``"|(expr1,expr2,...)"``，运算过程为对 2 个或以上内部表达式 ``expr1, expr2, ...`` 进行逻辑 **或的运算**（OR）


 

**示例 1：**

```
输入：expression = "!(f)"
输出：true
```

**示例 2：**

```
输入：expression = "|(f,t)"
输出：true
```

**示例 3：**

```
输入：expression = "&amp;(t,f)"
输出：false
```

**示例 4：**

```
输入：expression = "|(&amp;(t,f,t),!(t))"
输出：false
```

 

**提示：**


- ``1 <= expression.length <= 20000``
- ``expression[i]`` 由 ``{'(', ')', '&amp;', '|', '!', 't', 'f', ','}`` 中的字符组成。
- ``expression`` 是以上述形式给出的有效表达式，表示一个布尔值。



[LeetCode链接](https://leetcode-cn.com/problems/parsing-a-boolean-expression/)

### 思路及代码

括号匹配变形，感觉不是 hard 难度。

```cpp
class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> stk;
        for(auto c : expression){
            if(c == ')'){
                vector<bool> tmp;
                while(stk.top() != '('){
                    tmp.push_back(stk.top() == 't');
                    stk.pop();
                }

                stk.pop();
                char mode = stk.top();
                stk.pop();

                bool res;
                if(mode == '!'){
                    res = !tmp[0];
                }
                else if(mode == '|'){
                    res = 0;
                    for(auto t : tmp){
                        res |= t;
                    }
                }
                else{
                    res = true;
                    for(auto t : tmp){
                        res &= t;
                    }
                }

                if(res){
                    stk.push('t');
                }
                else{
                    stk.push('f');
                }
            }
            else if(c != ','){
                stk.push(c);
            }
        }
        return stk.top() == 't';
    }
};class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> stk;
        for(auto c : expression){
            if(c == ')'){
                vector<bool> tmp;
                while(stk.top() != '('){
                    tmp.push_back(stk.top() == 't');
                    stk.pop();
                }

                stk.pop();
                char mode = stk.top();
                stk.pop();

                bool res;
                if(mode == '!'){
                    res = !tmp[0];
                }
                else if(mode == '|'){
                    res = 0;
                    for(auto t : tmp){
                        res |= t;
                    }
                }
                else{
                    res = true;
                    for(auto t : tmp){
                        res &= t;
                    }
                }

                if(res){
                    stk.push('t');
                }
                else{
                    stk.push('f');
                }
            }
            else if(c != ','){
                stk.push(c);
            }
        }
        return stk.top() == 't';
    }
};
```