## 191. Number of 1 Bits
##### 2018-6-2
##### 位运算
***
## 题目
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:
```
Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
```
Example 2:
```
Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
```
## 分析
相对简单的位运算题目，看代码。
## 示例代码
```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int sum=0;
        for(int i=0;i<32;i++){
            if(n & 1)
                sum++;
            n >>=1;
        }
        return sum;
    }
};
```

