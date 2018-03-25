## 50. Pow(x, n)
##### 2018-03-25 
*****
## 1.题目
>Implement pow(x, n). 
>实现自己的pow函数，输入输出为double

## 2.分析
很早就看到的题目，一开始采取for循环逐级相乘，题目果断没这么简单，报错超时。  
讨论区看到，只要二次方来处理，运用递归就能省去很多时间。但是还是不太清楚为什么整形最小值的情况需要单独考虑。

下面有代码，递归
## 3.代码
```c
double myPow(double x,int n){
  if(n == 0) return 1;
    if(n == INT_MIN){
        x = x * x;
        n = n/2;
    }
    if(n < 0) {
        n = -n;
        x = 1/x;
    }
    return (n%2 == 0) ? myPow(x * x, n/2) : x *  myPow(x * x, n/2);
}
