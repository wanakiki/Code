## 953. 仅仅反转字母

2022-02-23 08:58:15

### 题目

给你一个字符串 ``s`` ，根据下述规则反转字符串：


- 所有非英文字母保留在原有位置。
- 所有英文字母（小写或大写）位置反转。


返回反转后的 ``s``<em> 。</em>






**示例 1：**

```
输入：s = "ab-cd"
输出："dc-ba"
```




**示例 2：**

```
输入：s = "a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
```




**示例 3：**

```
输入：s = "Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
```



**提示**


- ``1 <= s.length <= 100``
- ``s`` 仅由 ASCII 值在范围 ``[33, 122]`` 的字符组成
- ``s`` 不含 ``'\"'`` 或 ``'\\'``



[LeetCode链接](https://leetcode-cn.com/problems/reverse-only-letters/)

### 思路及代码

双指针对左右两侧元素进行标记，如果左右两侧均为字母则进行交换，交换后索引位置移动。如果不满足交换条件，则左右两侧至少有一侧为非字母，对其进行判断并改变索引位置。

```cpp
class Solution {
public:
    string reverseOnlyLetters(string s) {
        int left = 0, right = s.size() - 1;
        while(left < right){
            if(isalpha(s[left]) && isalpha(s[right])){
                swap(s[left], s[right]);
                left++;
                right--;
            }

            if(!isalpha(s[left])){
                left++;
            }
            if(!isalpha(s[right])){
                right--;
            }
        }
        return s;
    }
};
```