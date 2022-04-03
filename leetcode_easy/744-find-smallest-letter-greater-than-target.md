## 745. 寻找比目标字母大的最小字母

2022-04-03 19:38:31

### 题目

给你一个排序后的字符列表 ``letters`` ，列表中只包含小写英文字母。另给出一个目标字母 ``target``，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：


- 如果目标字母 ``target = 'z'`` 并且字符列表为 ``letters = ['a', 'b']``，则答案返回 ``'a'``




**示例 1：**

```
输入: letters = ["c", "f", "j"]，target = "a"
输出: "c"
```

**示例 2:**

```
输入: letters = ["c","f","j"], target = "c"
输出: "f"
```

**示例 3:**

```
输入: letters = ["c","f","j"], target = "d"
输出: "f"
```



**提示：**


- ``2 <= letters.length <= 10<sup>4</sup>``
- ``letters[i]`` 是一个小写字母
- ``letters`` 按非递减顺序排序
- ``letters`` 最少包含两个不同的字母
- ``target`` 是一个小写字母



[LeetCode链接](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/)

### 思路及代码

遍历数组，如果能够遇到大于目标值的字符直接返回，如果遇不到则返回首个元素。由于数组是有序的，可以使用二分查找对边界进行搜索，效率会更高。

```cpp
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        for(auto c : letters){
            if(c > target){
                return c;
            }
        }
        return letters[0];
    }
};
```