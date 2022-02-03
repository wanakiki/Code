## 1414. 和为 K 的最少斐波那契数字数目

2022-02-03 10:17:20

### 题目

给你数字 ``k`` ，请你返回和为 ``k`` 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：


- F<sub>1</sub> = 1
- F<sub>2</sub> = 1
- F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> ， 其中 n > 2 。


数据保证对于给定的 ``k`` ，一定能找到可行解。



**示例 1：**

```
输入：k = 7
输出：2
解释：斐波那契数字为：1，1，2，3，5，8，13，&hellip;&hellip;
对于 k = 7 ，我们可以得到 2 + 5 = 7 。```

**示例 2：**

```
输入：k = 10
输出：2
解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。
```

**示例 3：**

```
输入：k = 19
输出：3
解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。
```



**提示：**


- ``1 <= k <= 10^9``



[LeetCode链接](https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)

### 思路及代码


在周赛做过这道题，在做题的时候本来是想老老实实证明，发现证明起来很麻烦之后就尝试着莽一发贪心，最后过了。官方题解给了相关的证明，当时我只想到两个连续的斐波那契数可以用下一个数来代替，就感觉可以直接贪心做，跟具体的证明还有一定差距。

另外输入k不超过1e9，这个范围内的斐波那契数一共有44个，所以基本怎么做都不会超时。我在实现的时候对每个数都进行了一次求斐波那契数的过程，有一定的计算重复，更好的做法可以直接根据k算出可能的斐波那契数并保存下来。

```cpp
class Solution {
public:
    int findMinFibonacciNumbers(int k) {
        int res = 0;
        while(k != 0){
            
            int a = 1, b = 1;
            while(1){
                if(a > k){
                    k -= b;
                    break;
                }else{
                    int tmp = a+b;
                    b = a;
                    a = tmp;
                }
            }
            res+=1;
        }
        return res;
    }
};
```
先存储再查找版本，并没有快很多：

```cpp
class Solution {
public:
    int findMinFibonacciNumbers(int k) {
        vector<int> nums;
        int a = 1, b = 1;
        int res = 0;
        while(b <= k){
            nums.push_back(b);
            int tmp = a + b;
            a = b;
            b = tmp;
        }

        for(int i = nums.size() - 1; i >= 0; i--){
            while(k > 0 && nums[i] <= k){
                res++;
                k -= nums[i];
            }
        }
        return res;
    }
};
```