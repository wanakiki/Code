## Palindrome Number（回文数字）
##### 2018年02月01日22:30:52
****
### 题目
>Determine whether an integer is a palindrome. Do this without extra space.	判断一个整数是否是回文数，不使用其他的空间  
注意函数返回值为布尔类型

### 思路
第一眼的想法是把每位数分开储存在数组中，前后同时比较。但是发现了要求，采取了将整数翻转判断是否相等的写法。测试时发现-2147447412不能通过，于是将负数判断为``false``，成功提交！ 

**注意：C语言使用布尔型不采取“宏定义”的话需要添加头文件``<stdbool.h>``。**
### 代码
```c
bool isPalindrome(int x){
        if(x==0)
                return true;
        if(x<0)
                return false;
        int temp=0,temp2=x;
        while(x){
                temp=temp*10+x%10;
                x/=10;
        }
        if(temp==temp2)
                return true;
        else
                return false;
}
```
## 但实际上，问题远远没有解决←_←
