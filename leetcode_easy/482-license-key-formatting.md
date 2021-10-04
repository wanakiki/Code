## 482. 密钥格式化

2021-10-04 19:42:58

### 题目

有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1  
组。

给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。特别地，第一个分组包含的字
符个数必须小于等于 K，但至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有
的小写字母转换为大写字母。

给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。



**示例 1：**

```
输入：S = "5F3Z-2e-9-w", K = 4
输出："5F3Z-2E9W"
解释：字符串 S 被分成了两个部分，每部分 4 个字符；
     注意，两个额外的破折号需要删掉。
```

**示例 2：**

```
输入：S = "2-5g-3-J", K = 2
输出："2-5G-3J"
解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余 
部分皆为 2 个字符。
```



**提示:**


- S 的长度可能很长，请按需分配大小。K 为正整数。
- S 只包含字母数字（a-z，A-Z，0-9）以及破折号'-'
- S 非空





[LeetCode链接](https://leetcode-cn.com/problems/license-key-formatting/)

### 思路及代码

从后向前遍历字符串，字母个数等于k时添加破折号。需要提前开辟足够的空间存储最终字符串结果，直接使用``+``拼接字符串会造成额外的开销。

```cpp
class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        transform(s.begin(),s.end(),s.begin(),::toupper);   // 字符变大写
        bool falg = false;
        string res(s.size() + s.size() / k + 1, '-');
        int count = 0;
        int index = res.size() - 1;
        for(int i = s.size() - 1; i >= 0; i--){
            if(s[i] != '-'){
                res[index--] = s[i];
                count++;

                if(count == k && i != 0){
                    res[index--] = '-';
                    count = 0;
                }
            }
        }

        // 剔除字符串开头的破折号
        int pos = 0;
        for(; pos < res.size(); pos++){
            if(res[pos] != '-'){
                break;
            }
        }
        return res.substr(pos);
    }
};
```