##  Single Number
##### 2018年2月22日13:43:38
##### 异或XOR
***
### 题目
>Given an array of integers, every element appears twice except for one. Find that single one.  
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?  
给定一个整数数组，除了一个元素外，每个元素都会出现两次。找到那一个。 注意： 您的算法应该具有线性运行时复杂性。你可以实现它，而不使用额外的内存？

### 分析
遍历全部可以解决这个题目，但最好还是用异或来解决。
- 异或属于位运算符
- 异或运算是指：如果参与运算的两个值，如果对应位相同则结果为0，不同为1。如：0^0=0,0^1=1;（相等为零，不等为一）
- 可以用来使某些特定位反转，可以实现两个值的交换而不用临时变量。
- 运算法则：
  1. a ^ b = b ^ a
  2. a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c
  3. d = a ^ b ^ c 可以推出 a = d ^ b ^ c
  4. a ^ b ^ a = b

### 代码
```c
int singleNumber(int* nums, int numsSize) {
    for(int i=1;i<numsSize;i++)
        nums[0]^=nums[i];
    return nums[0];
}
```
