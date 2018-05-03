## 134. Gas Station
##### 2018-05-03 21:58:58
##### 加油站 递归
***
## 题目
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

- If there exists a solution, it is guaranteed to be unique.
- Both input arrays are non-empty and have the same length.
- Each element in the input arrays is a non-negative integer.

Example 1:
```
Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```
Example 2:
```
Input:
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```
## 分析
挺简单的一道题目不知道为啥花费了半个多少小时的时间，可能是今天刚考完期中考试吧....

首先要注意到题目要求顺时针走完所有的加油站，这样可以大大简化题目（我就没注意到，写了很麻烦的回溯.....)
函数中从零开始遍历，将对应的先加再减的最终油量传入辅助函数，同时还要传入当前的编号以及下一个车站编号（顺时针，辅助函数内部处理回到开头的情况），根据辅助函数的返回值判断是否返回当前序号。
辅助函数的传参有两个数组，当前油量，本次循环开始的编号，当前应该处理的编号。如果油量为负数返回false，数组越界则将当前处理的编号变为零，如果变化后（有变化）的编号为循环开始编号则返回true，最后返回下一次处理的结果。
## 示例代码
```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        for(int i=0;i<gas.size();i++){
            if(helper(gas,cost,gas[i]-cost[i],i,i+1))
                return i;
        }
        return -1;
    }

    bool helper(vector<int>& gas,vector<int>& cost,int tank,int index,int now){
        if(tank<0)
            return false;
        if(now==gas.size())
            now=0;
        if(now==index)
            return true;
        return helper(gas,cost,tank+gas[now]-cost[now],index,now+1);
    }
};
```
写着还算简单但是运行很慢....
