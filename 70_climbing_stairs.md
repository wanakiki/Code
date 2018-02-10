## Climbing Stairs
##### 2018年02月10日20:26:20
##### 印象深刻的递归题目（动态规划？？)
***
### 题目
>You are climbing a stair case. It takes n steps to reach to the top.  
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### 分析
做到这个题，提示了leetcode将在早上四点到六点维护（太平洋时间），
比我们晚16个小时。

不能提交就直接分析了，我对这个题目印象很深刻，是做过的第一道递归题。实质是斐波那契数列。
1. 假设当有n个台阶时假设有f(n)种走法。
3. 当最后一步跨1个台阶时有之前的f(n-1)种走法。
4. 当最后一步跨2个台阶时有之前的f(n-2 )种走法。
5. 所以n个台阶的走法等于前两种情况的走法之和即f(n)=f(n-1)+f(n-2)。

还发现了非递归的版本，一并贴上。
### 代码
```c
//递归
int climbStairs(int n) {
    if(n == 0 || n == 1) {
        return 1;
    } 
    if(n == 2) {
        return 2;
    }
    return climbStairs(n - 1) + climbStairs(n - 2);
} 

//非递归
int climbStairs(int n) {
    if(n == 0 || n == 1) {
        return 1;
    }
    if(n == 2) {
        return 2;
    }
    int a = 1;
    int b = 2;
    int c;
    for(int i = 3; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
	//也是(n-1)+(n-2)
    return c;
}
```
