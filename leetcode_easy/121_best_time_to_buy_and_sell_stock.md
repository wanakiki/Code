## 121. Best Time to Buy and Sell Stock
##### 2018年2月22日11:31:36
##### Kadane算法
***
### 题目
>Say you have an array for which the ith element is the price of a given stock on day i.  
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.   
假设你有一个数组，其中第i个元素是第i天给定股票的价格。 如果您只允许完成至多一笔交易（即买入一只股票并出售一只股票），则设计一种算法以找到最大利润。

### Example
```
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
```
### 分析
由题目，自然而然的可以想到遍历整个数组的解法。  
但是由于利润计算的特殊性，问题可以转化为求利润构成的数组中最大的子阵列。（53题 maxmium Subarray,Kadane算法）
### 代码
```c
int maxProfit(int* prices, int pricesSize) {
    int max=0;
    for(int i=0;i<pricesSize-1;i++)
    for(int j=i+1;j<pricesSize;j++){
        int temp=prices[j]-prices[i];
        if(temp>max)
            max=temp;
    }
return max;
}


//Kadane算法
int maxProfit(int* prices,int pricesSize){
	int max=0,temp=0;
	for(int i=1;i<pricesSize;i++){
		temp+=prices[i]-prices[i-1];
		if(temp<0)
			temp=0;
		if(temp>max)
			max=temp;
	}
return max;
}
```
***
2020年3月9日

实践证明kadane算法在当时做过之后没有记住...

重新做这个题目，想到的是动态规划的解法。题目可以转化为寻找最大连续子序列和的问题：

1. 首先将数组中的每个元素与其之前的元素求差，保存为diff数组
2. 初始化dp数组为0，并从第二个元素进行递归
3. dp[i] = max(0, dp[i-1]+diff[i])，按此公式进行计算，并不断更新最大值max

算法时间复杂度为O(n)，执行时间为8ms，击败了80%，但代码还是比较臃肿，有可以优化的地方。进行优化之后便能得到kadane算法。

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> diff(prices.size(), 0);
        vector<int> dp(prices.size(), 0);
        int res = 0;
        for(int i = 1; i < diff.size(); i++){
            diff[i] = prices[i] - prices[i-1];
        }
        for(int i = 1; i < dp.size(); i++){
            dp[i] = max(0, dp[i-1] + diff[i]);
            res = max(dp[i], res);
        }
        return res;
    }
};
```

## 122. Best Time to Buy and Sell Stock II
##### 2018年2月22日12:04:56
##### 贪心算法
***
### 题目
>Say you have an array for which the ith element is the price of a given stock on day i.  
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

### 分析
与上一题不同，我们可以进行多次买入卖出，问题变得更加简单.....  
还是由于利润计算的特殊性，我们直接算出相邻两天的利润，大于零就相加。
### 代码
```c
int maxProfit(int* prices, int pricesSize) {
    int max=0;
    for(int i=0;i<pricesSize-1;i++){
        int temp=prices[i+1]-prices[i];
        if(temp>0)
            max+=temp;
    }
    return max;
}
```
