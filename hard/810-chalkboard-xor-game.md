## 828. 黑板异或游戏

2021-05-22 23:22:48

### 题目

黑板上写着一个非负整数数组 ``nums[i]`` 。Alice 和 Bob 轮流从黑板上擦掉一个数字，Alice 先手。如果擦除一个数字后，剩余的所有数字按位异或运算得出的结果等于 0 的话，当前玩家游戏失败。 (另外，如果只剩一个数字，按位异或运算得到它本身；如果无数字剩余，按位异或运算结果为 0。）

并且，轮到某个玩家时，如果当前黑板上所有数字按位异或运算结果等于 0，这个玩家获胜。

假设两个玩家每步都使用最优解，当且仅当 Alice 获胜时返回 ``true``。

 

**示例：**

```
输入: nums = [1, 1, 2]
输出: false
解释:
Alice 有两个选择: 擦掉数字 1 或 2。
如果擦掉 1, 数组变成 [1, 2]。剩余数字按位异或得到 1 XOR 2 = 3。那么 Bob 可以擦掉任意数字，因为 Alice 会成为擦掉最 
后一个数字的人，她总是会输。
如果 Alice 擦掉 2，那么数组变成[1, 1]。剩余数字按位异或得到 1 XOR 1 = 0。Alice 仍然会输掉游戏。
```


**提示：**

- ``1 <= N <= 1000``
- ``0 <= nums[i] <= 2^16``


[LeetCode链接](https://leetcode-cn.com/problems/chalkboard-xor-game/)

### 思路及代码

这个题目是之前竞赛时经常遇到的类型，一直没有好的解决方法（其实是自己懒）。今天看题解，题解给出的分析方式是，因为每个人都要固定取一个数字，所以每个人取数字时数字的总个数的奇偶性是确定的，可以从这点考虑，忽略掉过程。

对于A会输的情况，意味着A任意拿去一个数字后，所有数字的异或值会变为0。我们假设取数字之前的数字个数为n，对n的奇偶性进行讨论。

假如n为偶数，则有初始条件$S_i \oplus nums[i] = S \ne 0$。在任取一个数字之后，得到$S_i = S \oplus nums[i] = 0$。

由于多个0的异或结果仍未零，所以有：

$$\begin{aligned}
    0 &= S_0 \oplus S_1 \oplus \dotsb \oplus S_{n-1} \\
      &= (S \oplus nums[0]) \oplus (S \oplus nums[1]) \oplus \dotsb \oplus (S \oplus nums[n-1]) \\
      &= \underbrace{(S \oplus S \oplus \dotsb \oplus S)} _{n}\oplus (nums[0] \oplus \dotsb \oplus nums[n-1])    \\
      &= \underbrace{(S \oplus S \oplus \dotsb \oplus S)} _{n+1}
\end{aligned}$$

由于n为偶数，上式得到 $0 = S$，与最初的条件矛盾，所以当数字个数为偶数时A必然不会输。

当n为奇数时同样可以进行上述推导，但此时任意的非零S取值均满足条件，也就是说n为奇数时存在必输的可能，而B的操作数为偶数，偶数已经证明必然不输。

因此A必胜的条件是数组的全部异或结果为0，或者数组的长度为偶数。

```cpp
class Solution {
public:
    bool xorGame(vector<int>& nums) {
        if(nums.size() % 2 == 0){
            return true;
        }
        int res = 0;
        for(auto n : nums){
            res ^= n;
        }
        return res == 0;
    }
};
```