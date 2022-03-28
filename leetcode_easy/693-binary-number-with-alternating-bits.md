## 693. 交替位二进制数

2022-03-28 09:06:18

### 题目

给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。



**示例 1：**

```
输入：n = 5
输出：true
解释：5 的二进制表示是：101
```

**示例 2：**

```
输入：n = 7
输出：false
解释：7 的二进制表示是：111.
```

**示例 3：**

```
输入：n = 11
输出：false
解释：11 的二进制表示是：1011.
```



**提示：**


- ``1 <= n <= 2<sup>31</sup> - 1``



[LeetCode链接](https://leetcode-cn.com/problems/binary-number-with-alternating-bits/)

### 思路及代码

当数据位数大于1位时，将数据与其左移一位之后的数字异或，判断最低位是否相同。

```cpp
class Solution {
public:
    bool hasAlternatingBits(int n) {
        while(n >1){
            int t = n >> 1;
            if(!((n ^ t) & 1)){
                return false;
            }
            n = t;
        }
        return true;
    }
};
```

上面的做法是通过循环实现的，但查看官解之后发现只需要一次异或，此时异或结果中为1的位置代表原数据对应位与其左侧二进位数值不同。因此满足所有相邻均不同的条件是异或结果全为1，可将异或结果与其加一之后的值进行与操作，判断是否全部为零即可。

```cpp
class Solution {
public:
    bool hasAlternatingBits(int n) {
        long a = n ^ (n >> 1);
        return (a & (a + 1)) == 0;
    }
};
```