## 872. 将数组拆分成斐波那契序列

2020-12-08 14:33:51

### 题目

给定一个数字字符串 ``S``，比如 ``S = "123456579"``，我们可以将它分成斐波那契式的序列 ``[123, 456, 579]``。

形式上，斐波那契式序列是一个非负整数列表 ``F``，且满足：


- ``0 <= F[i] <= 2^31 - 1``，（也就是说，每个整数都符合 32 位有符号整数类型）；
- ``F.length >= 3``；
- 对于所有的``0 <= i < F.length - 2``，都有 ``F[i] + F[i+1] = F[i+2]`` 成立。


另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。

返回从 ``S`` 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 ``[]``。

 

**示例 1：**

```
输入："123456579"
输出：[123,456,579]
```

**示例 2：**

```
输入: "11235813"
输出: [1,1,2,3,5,8,13]
```

**示例 3：**

```
输入: "112358130"
输出: []
解释: 这项任务无法完成。
```

**示例 4：**

```
输入："0123"
输出：[]
解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
```

**示例 5：**

```
输入: "1101111"
输出: [110, 1, 111]
解释: 输出 [11,0,11,11] 也同样被接受。
```

 

**提示：**


- ``1 <= S.length <= 200``
- 字符串 ``S`` 中只含有数字。



### 思路及代码

这是一个需要注意很多细节的题目，WA了三发之后终于过了，和官方题解相比代码显得比较散乱，但是相对朴实无华一点。

对于斐波那契数列，当前两个数字确定之后，后面的数字也都确定了。所以解决这个题目需要做的工作就是找到前两个数字的所有可能，并对其进行验证。

接下来看题目中给到的限制条件：

- 斐波那契数列中的数均符合32位有符号整数类型，也就是说在找前两个数的时候，我们查找的最大长度为10位，考虑到验证过程中的加法可能会导致超过这一范围，所以验证过程中直接使用``long long``进行计算，一旦超过范围直接终止验证。
- 所有的数字不支持前导零，除非是这个数本身：根据这点，我们在尝试前两个数所有可能情况时，一旦遇到一个前导零，即可放弃后续的一系列情况。

```cpp
class Solution {
public:
    vector<int> splitIntoFibonacci(string S) {
        // 数列中的数最大为十位
        // 前两个数确定之后后面的数字也自然确定了
        vector<int> res;
        int len = S.size();
        int num1, num2;
        for(int i = 1; i < 11; i++){
            for(int j = 1; j < 11; j++){
                int cur_len = i + j;
                if(cur_len >= len){
                    break;
                }
                num1 = getNum(S, 0, i);
                num2 = getNum(S, i, j);
                long long a = num1, b = num2;
                int index = i + j;
                bool flag = true;
                int count = 0;  // 统计计算次数
                cout << a << ' ' << b << ' ' << index << endl;
                while(index < len){
                    long long int aim = a + b;
                    if(aim > INT_MAX){
                        flag = false;
                        break;
                    }
                    count++;
                    int next_len = getLen(aim);
                    if(aim != getNum(S, index, next_len)){
                        flag = false;
                        break;
                    }
                    index += next_len;
                    a = b;
                    b = aim;
                }
                if(flag && index == len){
                    res.push_back(num1);
                    res.push_back(num2);
                    while(count--){
                        int tmp = num1 + num2;
                        res.push_back(tmp);
                        num1 = num2;
                        num2 = tmp;
                    }
                    return res;
                }

                // 避免前导零
                if(num2 == 0){
                    break;
                }
            }

            // 避免前导零
            if(num1 == 0){
                break;
            }
        }
        return res;
    }
    int getNum(string& S, int start, int len){
        // 保证不会出现前导零 但需要对越界进行判断
        if(start + len > S.size()){
            return -1;
        }

        // 避免数字过大
        long long res = 0;
        while(len){
            res = res * 10 + S[start++] - '0';
            len--;
        }
        return res;
    }
    int getLen(int cur){
        if(cur == 0){
            return 1;
        }
        int count = 0;
        while(cur){
            count++;
            cur /= 10;
        }
        return count;
    }
};
```