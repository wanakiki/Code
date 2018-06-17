## 190. Reverse Bits
##### 2018-6-2
##### 位运算
***
## 题目
Reverse bits of a given 32 bits unsigned integer.

Example:
```
Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
```
Follow up:
If this function is called many times, how would you optimize it?
## 分析
题目重点看位运算，做法是将n的最右一位不断提出，加到返回变量上，再将返回变量左移，如此循环32次就可以了。
## 示例代码
```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res;
        for (int i = 0; i < 32; i++) {
            res <<= 1;
            res += n & 1; //n&1返回值就是n最右一位
            n >>= 1;
        }
        return res;
    }
};
```
