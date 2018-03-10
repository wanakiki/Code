## 55.Jump Game
##### 2018-03-10
##### 理解题意以及简化方法
***
## 1.题目
>Given an array of non-negative integers, you are initially >positioned at the first index of the array.
>
>Each element in the array represents your maximum jump length at that position.
>
>Determine if you are able to reach the last index.  
给定一个非负整数数组，您最初定位在数组的第一个索引处。 数组中的每个元素都表示该位置的最大跳转长度。 确定是否能够达到最后一个索引。
>
>For example:
A = [2,3,1,1,4], return true.
>
>A = [3,2,1,0,4], return false.

## 2.分析
理解问题十分关键，起初以为要求必须达到最后一个索引的位置，并且每个元素只能移动对应的距离。  
所以认为题目很简单，从零开始进行了操作，看到最后能否到numsSIze-1的位置。可以说跟原来的题目差的多的多😑  

修改多次之后终于发现了问题的所在，数组的值是最大的移动范围，我们只要找到数组最终移动范围的最大值并且与数组的长度相比较就可以得到结果。  

📜怎么比较呢.....  
1. 定义一个变量reach表示当前到达的位置，只要数组的索引小于reach，就一定可以从0位置跳跃到reach。
2. reach的初始值为零，初始元素的索引也是零，我们将每个索引位于reach内的元素与reach相比较，如果i+nums[i]大于reach,则表示跳跃能够到达的位置被扩大，当遍历完reach内的所有元素后，reach的值就一定会被增加到跳跃的最大范围。

📌上述过程其实是reach的不断扩充的过程，伴随reach的扩充，被访问的元素越来越多

## 3.代码

```c
bool canJump(int *nums,int numsSize){
  int reach=0;
  for(int i=0;i<=reach && i<numsSize;i++){
    if(i+nums[i]>reach)
      reach=i+nums[i];
  }
  if(reach>=numsSIze-1)
    return true;
  else
    return false;
}
```
炒鸡简单好吧
