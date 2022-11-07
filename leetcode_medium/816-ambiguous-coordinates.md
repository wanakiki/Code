## 816. 模糊坐标

2022-11-07 10:28:44

### 题目

我们有一些二维坐标，如 ``"(1, 3)"`` 或 ``"(2, 0.5)"``，然后我们移除所有逗号，小数点和空格，得到一个字符串``S``。返回所有可能的原始字符串到一个列表中。

原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现&ldquo;.1&rdquo;形式的数字。

最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。

 

```
示例 1:
输入: "(123)"
输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
```

```
示例 2:
输入: "(00011)"
输出:  ["(0.001, 1)", "(0, 0.011)"]
解释: 
0.0, 00, 0001 或 00.01 是不被允许的。
```

```
示例 3:
输入: "(0123)"
输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
```

```
示例 4:
输入: "(100)"
输出: [(10, 0)]
解释: 
1.0 是不被允许的。
```

 

**提示: **


- ``4 <= S.length <= 12``.
- ``S[0]`` = "(", ``S[S.length - 1]`` = ")", 且字符串 ``S`` 中的其他元素都是数字。


 


[LeetCode链接](https://leetcode-cn.com/problems/ambiguous-coordinates/)

### 思路及代码

数据范围比较小，直接考虑所有可拆分情况判断即可。注意的点是，以零开头的字符串只能生成小数，以零结尾的字符串只能生成整数。

```cpp
class Solution {
public:
    vector<string> helper(string source){
        vector<string> res;
        if(source.size() == 1 && source[0] == '0')  res.push_back("0");
        
        // 不以零开头则可以成为整数
        if(source[0] != '0'){
            res.push_back(source);
        }

        // 以零结尾不能成为小数
        if(source[source.size() - 1] != '0'){
            // 小数的检查规则是避免整数部分出现全为零的情况 需要对前导零的个数进行检查
            if(source[0] == '0'){
                res.push_back("0." + source.substr(1));
            }
            else{
                for(int i = 1; i < source.size(); i++){
                    res.push_back(source.substr(0, i) + "." + source.substr(i));
                }
            }
        }
        return res;
    }
    vector<string> ambiguousCoordinates(string s) {
        int mid = 1;
        int right = s.size() - 2;
        int left = 1;
        vector<string> res;
        for(mid = 1; mid < s.size() - 2; mid++){
            // 如果字符串长度大于1并且两侧都是零，不满足分配条件
            if((left != mid && s[left] == '0' && s[mid] == '0') || (mid + 1 != right && s[mid+1] == '0' && s[right] == '0')){
                continue;
            }
            else{
                vector<string> left_part = helper(s.substr(1, mid - left + 1));
                vector<string> right_part = helper(s.substr(mid + 1, right - mid));

                for(auto left_s : left_part){
                    for(auto right_s : right_part){
                        res.push_back( "(" + left_s + ", " + right_s + ")" );
                    }
                }
            }
        }
        return res;
    }
};
```