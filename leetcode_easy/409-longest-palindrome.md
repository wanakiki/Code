## 409. 最长回文串

2020年3月19日

### 题目

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

**注意**:
假设字符串的长度不会超过 1010。

示例 1:
```no
输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
```
### 代码

哈希表存储字符个数，之后遍历计算长度。

```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char,int> hash;
        for(int i = 0; i < s.size(); i++){
            hash[s[i]]++;
        }
        int extral = 0;
        int res = 0;
        for(auto i = hash.begin(); i != hash.end(); i++){
            if(i->second % 2 == 0)
                res += i->second;
            else{
                res += i->second - 1;
                if(!extral)
                    extral = 1;
            }
        }
        return res + extral;
    }
};
```

但实际上可以只统计奇数个数字字母出现的次数，然后用字符串总长度减去个数减一。当然，如果全部都是偶数个则不用减。

class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char,int> hash;
        for(int i = 0; i < s.size(); i++){
            hash[s[i]]++;
        }
        int count = 0;
        for(auto i = hash.begin(); i != hash.end(); i++){
            if(i->second % 2 != 0)
                count++;
        }
        if(count)
            count--;
        return s.size()-count;
    }
};