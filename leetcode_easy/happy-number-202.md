## 202. Happy Number
##### 2018-06-06 21:54:25
##### 快慢指针
***
## 题目
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 
```
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```
## 分析
如何计算这个数很简单，但是如何结束循环是个问题，我开始也没有想到，看了下别人的解法发现这里也用了类似快慢指针的方法，思路很清晰，是个简单题。
## 示例代码
```cpp
class Solution {
public:
    int helper(int n){
        int sum=0;
        while(n){
            sum+=pow(n%10,2);
            n/=10;
        }
        return sum;
    }
    bool isHappy(int n) {
        int fast,slow;
        fast=slow=n;
        do{
            slow=helper(slow);
            fast=helper(fast);
            fast=helper(fast);
        }while(fast !=slow); //出现1的时候就无线循环1
        if(fast == 1)
            return true;
        else
            return false;
    }
};
```

