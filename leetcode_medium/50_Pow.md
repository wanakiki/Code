## 50. Pow(x, n)
##### 2018-03-03 
##### 递归
*****
## 分析
要实现自己的pow函数，第一个想法就是直接累乘，只需要考虑部分特殊情况就可以完成代码。  
但是的确是自己想得太简单，累乘法超时，看了下别人的代码，发现是用递归处理的，也很清晰。  
注意，在C语言中，``double``型的输入为 %lf ，输出时用%f  

## 代码
```c
double myPow(double x,int n)
{
    double b=1.0;
    if(n==0)
        return 1.0;
    if(n>0){
    for(int i=0;i<n;i++)
        b*=x;
    }
    else{
    n=-n;
    for(int i=0;i<n;i++)
        b*=1/x;
    }
    return b;
}


double myPow(double x, int n){  
   if(n == 0)
     return 1;
   double t = myPow(x, n/2);
   if(n % 2 == 0)
        return t*t;
   else{
      if(n > 0)
         return x*t*t;
      else 
        return (t*t) / x;
  }
}
```
