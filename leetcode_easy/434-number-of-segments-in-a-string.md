## 434. 字符串中的单词数

2020年5月4日

### 题目

统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

**示例:**

```
输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
```

### 代码

设置一个布尔类型的变量flag用于标记当前状态，若flag为真表示上一个遍历到的字符为空格或者处于起始位置，flag为假表示上一个遍历到的字符不是空格。在此基础上遍历一遍字符串，过程中更新flag与统计变量。

```cpp
class Solution {
public:
    int countSegments(string s) {
        int res = 0, flag = true;
        for(int i = 0; i < s.size(); i++){
            if(s[i] != ' ' && flag){
                res++;
                flag = false;
            }
            if(s[i] == ' '){
                flag = true;
            }
        }
        return res;
    }
};
```