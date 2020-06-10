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
### 遗留的问题
##### 2018年02月03日11:32:16
***
之后把大部分时间都用在了今天要交的脚本上面，到现在补下遗留的问题
- 可能是leetcode本身的错误，-2147447412一定是一个回文数字，早在2015年大家就已经开始讨论这个问题了.......但是解释是``-``不等于``2``
- 直接翻转的方法存在整形溢出的问题，翻转后一旦溢出上述解决方法就出现了错误，但是实际上如果这个数是回文数，反转一定不会溢出
- 之前翻转数字的经验让我直接想到了``long long``型，但是这使我对题目要求产生了疑惑：**引入新的变量应该也属于引用了额外的空间**
- 不管怎样，这道题还是就回文数的判断提供了很多思路
   1. 转化为字符串进行判断，可能这就是程序员的习惯，看的很多解答都是先想到了这个方法
   2. 反转判断是否相等，虽然有溢出问题，但是也是个好方法
   3. 求一半的回文数，两部分比较，奇数位数时去掉中间
   4. 我的第一个想法，把每位数分别存放到数组里，前后同时比较


### 2020年6月10日

### 题目
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例 1:**

```
输入: 121
输出: true
```

**示例 2:**

```
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```

**示例 3:**

```
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
```

**进阶:**

你能不将整数转为字符串来解决这个问题吗？

### 思路及代码

两年过去了，力扣对这个题目的描述进行了更改，如果一个数是负数，由于符号不与任何数字相等，故一定不是回文数。另外发现之前我的做法存在反转后溢出的问题，但是还是成功提交了，看来有人补上了相关的数据。将数据的类型定义为``long long``就能避免溢出：

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0)
            return false;
        long long  temp1 = 0, temp2 = x;
        while(x){
            temp1 = temp1 * 10 + x % 10;
            x /= 10;
        }
        return temp1 == temp2;
    }
};
```

这个题目使用字符串的方法很简单，将整数转化为字符串，然后双指针比较即可：

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        string num = to_string(x);
        int left = 0, right =  num.size() - 1;
        while(left < right){
            if(num[left] != num[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;   
    }
};
```

但是不使用字符串的最佳做法应该是只反转一般的整数，大致做法如下：首先排除负数，之后设置一个临时变量``reverse_num``（不需要考虑越界）用来记录反转一般的数据，初始值为零。对x进行模十操作，将最后一位累加到反转数据上，然后除以十。重复这个过程直到x不大于反转变量为止。

假设x是一个回文数字，则根据x的长度有下面两种情况：

- x长度为奇数，循环停止后reverse_num的值会大于x，但抹去reverse_num的最后一位后二者相等
- x长度为偶数，循环停止后reverse_num与x相等

如果x不是一个回文数字的话，则根据x的长度循环结束后同样会有两种情况：

- x长度为奇数，循环停止后reverse_num的位数必然大于x，二者不等，并且reverse_num抹去最后一位后二者同样不等
- x长为偶数，循环停止后reverse_num的位数大于或者等于x，这又对应两种情况：
    1. 若reverse_num的位数大于x，由于x长度为偶数，reverse_num必然比x多两位，抹去最后一位之后二者仍然不等
    2. 若reverse_num的位数等于x，由于初始x的值不是回文数字，所以循环结束后reverse_num与x的值必然不等，在抹去reverse_num的最后一位后二者同样不等。

结合上面的分析，可以用 ``x == reverse_num || x == (reverse_num / 10)``这一条件来判断原数字是否为回文数字。

但是上面的分析存在一个漏洞，由于reverse_num的初始值是0，在x的末尾存在0的情况下，反转之后x与reverse_num位数之和会小于x，这时之前所做的分析便没有了参考价值。但好在除了0以外末尾是零的数字一定不是回文数，我们可以先把这一部分数据排除后再按照反转一般的方法来做。

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0))   return false;
        int reverse_num = 0;
        while(reverse_num < x){
            reverse_num = reverse_num * 10 + x % 10;
            x /= 10;
        }
        return x == reverse_num || x == (reverse_num / 10);
    }
};
```