# 135.Candy

日期：2018年7月31日

## 题目

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Example 1:

```no
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
```

Example 2:

```no
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
```

## 思路

两个关键点，每个孩子至少有一个糖果，高分的孩子的糖果要比相邻低分的孩子糖果多。

假设我们用一个数组来记录每个孩子分配的糖果数量，第一个条件意味着数组元素至少为1，第二个条件是根据评分结果，高分孩子的数量要大于两侧低分孩子。

采用大众的思路，正向遍历一次，反向遍历一次，同时不断更新应该分配的糖果数量，反向遍历的时候同时统计总数。

经过我自己的测试，反向时max会比if快很多。

## 示例代码

C++:
```cpp
class Solution {
public:
    int candy(vector<int>& ratings) {
        int len = ratings.size();
        vector<int> res(len,0);
        res[0] = 1;
        for(int i = 1; i < len; i++){
            if(ratings[i] > ratings[i-1])
                res[i] = res[i-1] + 1;
            else
                res[i] = 1;
        }
        int sum = res[len-1];
        for(int j = len-2; j >= 0; j--){
            if(ratings[j] > ratings[j+1])
                res[j] = max(res[j+1]+1, res[j]);
                sum += res[j];
        }
        return sum;
    }
};
```