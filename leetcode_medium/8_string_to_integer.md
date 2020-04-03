##  String to Integer (atoi)
##### 2018年2月23日16:12:21
##### 写自己的atoi函数
***
### 分析
*题目要求实现atoi函数，并且给出了该函数的要求：*
- 函数要能够提取出字符串中的整数
- 函数需要丢弃字符串开头的空白，紧接着正负号，然后提取数字。（正负号非必须）
- 只提取第一个有效整数
- 当第一个非空白字符序列不是有效整数（包括正负号）时，或者字符串为空时返回零。
- 当整数溢出时，返回INT_MAX或者INT_MIN
- 例如：“       +45aaa12" 	返回45

*具体的思路就是逐个判断，没有什么好说的，说一点细节*
- 用``long``判断溢出，INT_MAX需要头文件``<limits.h>``
- ``isspace()、isdigit()``可以用来判断是否是空白、数字，头文件``<ctype.h>``
- **提交发现``+-2``返回值为0，但个人认为应为-2**，对于这个疑惑写了另一种判断方法解决（见代码）

### 代码
```c
#include<stdio.h>
#include<ctype.h>
#include<limits.h>
int myAtoi(char* str) {
    int flag=0;
    //用于标记符号，同时能够避免多个正负号的情况
    long num=0;   //做返回值，同时判断溢出
    while(isspace(*str))
        str++;
    if(*str=='-'||*str=='+'){
        if(*str=='-')
            flag-=1;
        else
            flag+=1;
        str++;
    }
    /*个人认为较正确的方法
    int flag=1;
    while(*str=='-'||*str=='+'){
        if(*str=='-')
            flag=-flag;
        str++;
    }*/
    if(!isdigit(*str))
        return 0;
    while(isdigit(*str) && num<=INT_MAX){
        num=num*10+*str-'0';
        str++;
    }
    if(num>INT_MAX)
        return flag<0? INT_MIN : INT_MAX;
    return flag<0? -num: num;

}
int main(){
    printf("测试自己的atoi函数\n");
    printf("输入字符串，20以内：");
    char a[20];
    gets(a);
    printf("结果是：%d",myAtoi(a));
}
```


### 2020年4月3日

遍历数组，找到第一个连续数字区间进行判断是一种比较不错的方法，但今天我又实现了另外一种只使用一个循环的方案，边界处理稍显复杂。但不得不说，直接判断过程中累加的数值是否超过INT_MAX来确定是否越界是个好思路。最终时间复杂度仍为O(n)。

```cpp
class Solution {
public:
    int myAtoi(string str) {
        bool flag = true, start = false;    // start表示是否已经进行计数
        long tmp = 0;
        for(int i = 0; i < str.size(); i++){
            if(!start && str[i] == ' ')
                continue;
            if(start && (str[i] < '0' || str[i] > '9'))
                break;
            if(str[i] >= '0' && str[i] <= '9'){
                start = true;
                tmp = tmp * 10 + str[i]-'0';
            }
            else if(str[i] == '+'){
                start = true;
            }
            else if(str[i] == '-'){
                flag = false;
                start = true;
            }
            else                        // 以字母打头的情况
                break;
            if(tmp > INT_MAX)           // 累加一次之后就应判断是否越界，提前返回
                return flag?INT_MAX:INT_MIN;
        }
        return flag?tmp:-tmp;
    }
};
```

官方题解中有限状态机的做法帮助也很大，和之前学过的电子系相关知识有很大的联系。根据题意，可以抽象出start、signed、in_number、end四种状态，状态转移字符的可能情况有number、+or-、ohter、space，状态机可表示为：

| | number | +or- | other | space|
| - | - | - | - | - |
| start | in_number | signed | end | start |
| signed | in_number | end | end | end |
| in_nubmer | in_number | end | end | end |
| end | end | end | end | end |

只要将上面的状态转换表写进代码，就能无误的完成本程序的边界处理。这里借用一下官方的代码，状态机封装的很好，不过感觉可以对get函数添加返回值用以提前结束遍历。

```cpp
class Automaton {
    string state = "start";
    unordered_map<string, vector<string>> table = {
        {"start", {"start", "signed", "in_number", "end"}},
        {"signed", {"end", "end", "in_number", "end"}},
        {"in_number", {"end", "end", "in_number", "end"}},
        {"end", {"end", "end", "end", "end"}}
    };

    int get_col(char c) {
        if (isspace(c)) return 0;
        if (c == '+' or c == '-') return 1;
        if (isdigit(c)) return 2;
        return 3;
    }
public:
    int sign = 1;
    long long ans = 0;

    void get(char c) {
        state = table[state][get_col(c)];
        if (state == "in_number") {
            ans = ans * 10 + c - '0';
            ans = sign == 1 ? min(ans, (long long)INT_MAX) : min(ans, -(long long)INT_MIN);
        }
        else if (state == "signed")
            sign = c == '+' ? 1 : -1;
    }
};

class Solution {
public:
    int myAtoi(string str) {
        Automaton automaton;
        for (char c : str)
            automaton.get(c);
        return automaton.sign * automaton.ans;
    }
};
```
作者：LeetCode-Solution  
链接：https://leetcode-cn.com/problems/string-to-integer-atoi/solution/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/

