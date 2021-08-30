## 528. 按权重随机选择

2021-08-30 10:50:51

### 题目

给定一个正整数数组 ``w`` ，其中 ``w[i]`` 代表下标 ``i`` 的权重（下标从 ``0`` 开始），请写一个函数 ``pickIndex`` ，它可以随
机地获取下标 ``i``，选取下标 ``i`` 的概率与 ``w[i]`` 成正比。




例如，对于 ``w = [1, 3]``，挑选下标 ``0`` 的概率为 ``1 / (1 + 3) = 0.25`` （即，25%），而选取下标 ``1`` 的概率为 ``3 / (1 
+ 3) = 0.75``（即，75%）。

也就是说，选取下标 ``i`` 的概率为 ``w[i] / sum(w)`` 。



**示例 1：**

```
输入：
["Solution","pickIndex"]
[[[1]],[]]
输出：
[null,0]
解释：
Solution solution = new Solution([1]);
solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。
```

**示例 2：**

```
输入：
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
输出：
[null,1,1,1,1,0]
解释：
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。

由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
诸若此类。
```



**提示：**


- ``1 <= w.length <= 10000``
- ``1 <= w[i] <= 10^5``
- ``pickIndex`` 将被调用不超过 ``10000`` 次



[LeetCode链接](https://leetcode-cn.com/problems/random-pick-with-weight/)

### 思路及代码

此前没接触到产生随机数的题目，读完题之后没有多少想法。查看官方题解之后发现问题其实蛮简单的，假设所有数字的和为total，本题目的要求便是把长度为total的区间划分为n个小区间，n为原始数组的长度。小区间的长度需要和原始数组对应的权值相同，接下来随机生成一个数字，看该数字位于哪个区间便返回该区间对应的索引。不难看出划分结果的每个区间起点和终点可以使用前缀和来表示，题目便化身成前缀数组配合二分查找方法查找边界的问题。

```cpp
class Solution {
public:
    vector<int> pre;
    Solution(vector<int>& w) {
        pre.assign(w.begin(), w.end());
        // 计算前缀
        for(int i = 1; i < pre.size(); i++){
            pre[i] += pre[i - 1];
        }
    }
    
    int pickIndex() {
        int target = random() % pre[pre.size() - 1] + 1;
        // 二分查找大于等于target的第一个位置
        int left = 0, right = pre.size() - 1;
        while(left < right){
            int mid = left + (right - left) / 2;
            if(pre[mid] < target){
                left = mid + 1;
            }
            else{
                right = mid;
            }
        }
        return left;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
 ```

 上面代码采用的是很朴实无华的写法，但是官方题解给出的代码大量使用了新函数：

 ```cpp
 class Solution {
private:
    mt19937 gen;
    uniform_int_distribution<int> dis;
    vector<int> pre;

public:
    Solution(vector<int>& w): gen(random_device{}()), dis(1, accumulate(w.begin(), w.end(), 0)) {
        partial_sum(w.begin(), w.end(), back_inserter(pre));
    }
    
    int pickIndex() {
        int x = dis(gen);
        return lower_bound(pre.begin(), pre.end(), x) - pre.begin();
    }
};
/*
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/random-pick-with-weight/solution/an-quan-zhong-sui-ji-xuan-ze-by-leetcode-h13t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
```

有老哥在评论区给出了不常见函数的解释：

> C++STL说明：
>
> - mt19937头文件是<random> 是伪随机数产生器，用于产生高性能的随机数
>- uniform_int_distribution 头文件在<random>中，是一个随机数分布>类，参数为生成随机数的类型，构造函数接受两个值表示区间段
>- accumulate 头文件在<numeric>中，求特定范围内所有元素的和。
>- spartial_sum函数的头文件在<numeric>，对(first, last)内的元素逐个求累计和，放在result容器内
>- back_inserter函数头文件<iterator>，用于在末尾插入元素。
>- lower_bound头文件在<algorithm>，用于找出范围内不大于num的第一个元素