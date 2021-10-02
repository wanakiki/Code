## 405. 数字转换为十六进制数

2021年10月2日

### 题目

给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

1. 十六进制中所有字母(a-f)都必须是小写。
2. 十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，3. 十六进制字符串中的第一个字符将不会是0字符。 
4. 给定的数确保在32位有符号整数范围内。
5. 不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

示例 1：
```no
输入:
26

输出:
"1a"
```
示例 2：
```no
输入:
-1

输出:
"ffffffff"
```
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal

### 思路及代码

提取二进制位，每四个一组转化为十六进制数。

下面是一年之前提交的，估计当时参考了别人的代码，直接和15进行与运算得到四位的方法挺不错。

```cpp
class Solution {
public:
    string toHex(int num) {
        unsigned int cur = num, tmp = 0;
        string str = "";
        char maps[16] = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};
        while(cur){
            tmp = cur & 15;
            cur >>= 4;
            str += maps[tmp];
        }
        if(str == "")
            return "0";
        string res(str.rbegin(), str.rend());
        return res;
    }
};
```


今天自己写的代码就挺朴实无华的，甚至有些丑陋：

```cpp
class Solution {
public:
    char helper(string cur){
        int count = 0;
        if(cur[0] == '1')   count += 8;
        if(cur[1] == '1')   count += 4;
        if(cur[2] == '1')   count += 2;
        if(cur[3] == '1')   count += 1;

        if(count < 10)  return '0' + count;
        else{
            return 'a' + count - 10;
        }
    }
    string toHex(int num) {
        string res = "";
        for(int i = 0; i < 32; i++){
            if(num & 1){
                res += '1';
            }
            else{
                res += '0';
            }
            num >>= 1;
        }
        reverse(res.begin(), res.end());

        string hex_res = "";
        bool flag = false;      // 零需要特殊判断，只有当此前出现整数或者是最后一位时才能添加零到结果字符串当中
        for(int i = 0; i < 8; i++){
            char cur = helper(res.substr(i * 4, 4));
            if(cur != '0'){
                hex_res += cur;
                flag = true;
            }
            else if(i == 7 || flag){
                hex_res += cur;
            }
        }

        return hex_res;
    }
};
```