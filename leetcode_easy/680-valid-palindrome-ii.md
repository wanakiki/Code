## 680. 验证回文字符串 Ⅱ

2020年5月19日

### 题目

给定一个非空字符串 ``s``，**最多**删除一个字符。判断是否能成为回文字符串。

**示例 1:**

```
输入: "aba"
输出: True
```

**示例 2:**

```
输入: "abca"
输出: True
解释: 你可以删除c字符。
```

**注意:**

- 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

### 代码

和普通的验证回文字符串问题相比，这个题目新增了一个删除字母的可选项，要求判断给定字符串是否能够变成回文，当然如果本身是回文不需要做额外的处理。

解题的方法很简单，用双指针从两端对比字符串的每个字母，如果找不到不同的字符，该字符串便为回文字符串。如果发现了不同，则记录下不同点的位置，此时可以删除的字符有两个，分别是最左边和最右边的字符。

将指针分别跳过左端和右端的值，对剩余部分继续进行普通的回文字符串判断方法，最后返回这两个调用结果的或值。

```cpp
class Solution {
public:

    bool helper(string& s, int left, int right){
        while(left < right){
            if(s[left] != s[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    bool validPalindrome(string s) {
        int left = 0, right = s.size()-1;
        int left2, right2;
        bool flag = true;
        while(left < right){
            if(s[left] != s[right]){
                flag = false;
                right2 = right-1;
                left2 = left;
                left += 1;
                break;
            }
            left++;
            right--;
        }

        if(flag){
            return true;
        }
        else{
            return helper(s, left, right) || helper(s, left2, right2);
        }
    }
};
```
