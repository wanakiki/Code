## 878. 第 N 个神奇数字

2022-11-22 11:13:52

### 题目

一个正整数如果能被 ``a`` 或 ``b`` 整除，那么它是神奇的。

给定三个整数 ``n`` , ``a`` , ``b`` ，返回第 ``n`` 个神奇的数字。因为答案可能很大，所以返回答案 **对 **``10<sup>9</sup> + 7`` **取模 **后的值。

 
**示例 1：**

```
输入：n = 1, a = 2, b = 3
输出：2
```

**示例 2：**

```
输入：n = 4, a = 2, b = 3
输出：6
```

 

**提示：**


- ``1 <= n <= 10<sup>9</sup>``
- ``2 <= a, b <= 4 * 10<sup>4</sup>``


[LeetCode链接](https://leetcode-cn.com/problems/nth-magical-number/)

### 思路及代码

显然，对于给定的a，b数值，神奇数字会以两者最小公倍数循环出现。将所有小于等于最小公倍数的a，b数值保存到nums数组，其长度对应循环周期，可进一步计算出第n个数据对应的具体数值。

```cpp
class Solution {
public:
    int nthMagicalNumber(int n, int a, int b) {
        if(a > b)   swap(a, b);

        vector<long> nums = {a, b};
        long sum_a = a;
        long sum_b = b;
        long mask = 1000000007;

        while(sum_a != sum_b){
            if(sum_b < sum_a){
                sum_b += b;
                nums.push_back(sum_b);
            }
            else{
                sum_a += a;
                nums.push_back(sum_a);
            }
        }
        sort(nums.begin(), nums.end());

        long len = nums.size() - 1;
        long max_val = sum_a;

        nums[len] = 0;  // sum_a 出现了两次
        long loop_count = n / len;
        long loop_left = (n % len) == 0 ? len : (n % len) - 1;

        long res = ((loop_count * max_val) % mask + nums[loop_left]) % mask;
        return res;

    }
};
```

上面代码压线通过了测试，主要问题有以下方面：
- 当第n个数值小于最小公倍数时进行了额外计算
- 计算最小公倍数数组时数据添加次序不正确，导致需要额外的排序

下面是官方题解的做法，更加优雅。

```cpp
class Solution {
public:
    const int MOD = 1e9 + 7;
    int nthMagicalNumber(int n, int a, int b) {
        int c = lcm(a, b);
        int m = c / a + c / b - 1;
        int r = n % m;
        int res = (long long) c * (n / m) % MOD;
        if (r == 0) {
            return res;
        }
        int addA = a, addB = b;
        for (int i = 0; i <  r - 1; ++i) {
            if (addA < addB) {
                addA += a;
            } else {
                addB += b;
            }
        }
        return (res + min(addA, addB) % MOD) % MOD;
    }
};

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/nth-magical-number/solution/di-n-ge-shen-qi-shu-zi-by-leetcode-solut-6vyy/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

从官方题解看到题目可以使用二分查找和容斥原理求解：
$$ f(x)=\left\lfloor\frac{x}{a}\right\rfloor+\left\lfloor\frac{x}{b}\right\rfloor-\left\lfloor\frac{x}{c}\right\rfloor $$

其中 $f(x)$ 代表小于等于 $x$ 的神奇数字个数，其等于小于等于 $x$ 中分别能被 a，b 整除的数字个数，减去能被二者最小公倍数整除的数字个数。