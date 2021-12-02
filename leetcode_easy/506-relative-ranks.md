## 506. 相对名次

2021-12-02 16:47:41

### 题目

给你一个长度为 ``n`` 的整数数组 ``score`` ，其中 ``score[i]`` 是第 ``i`` 位运动员在比赛中的得分。所有得
分都 **互不相同** 。

运动员将根据得分 **决定名次** ，其中名次第 ``1`` 的运动员得分最高，名次第 ``2`` 的运动员得分第 ``2`` 高
，依此类推。运动员的名次决定了他们的获奖情况：


- 名次第 ``1`` 的运动员获金牌 ``"Gold Medal"`` 。
- 名次第 ``2`` 的运动员获银牌 ``"Silver Medal"`` 。
- 名次第 ``3`` 的运动员获铜牌 ``"Bronze Medal"`` 。
- 从名次第 ``4`` 到第 ``n`` 的运动员，只能获得他们的名次编号（即，名次第 ``x`` 的运动员获得编号 ``"x"`` 
）。


使用长度为 ``n`` 的数组 ``answer`` 返回获奖，其中 ``answer[i]`` 是第 ``i`` 位运动员的获奖情况。



**示例 1：**

```
输入：score = [5,4,3,2,1]
输出：["Gold Medal","Silver Medal","Bronze Medal","4","5"]
解释：名次为 [1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup>, 4<sup>th</sup>, 5<sup>th</sup>] 。
```     

**示例 2：**

```
输入：score = [10,3,8,9,4]
输出：["Gold Medal","5","Bronze Medal","Silver Medal","4"]
解释：名次为 [1<sup>st</sup>, 5<sup>th</sup>, 3<sup>rd</sup>, 2<sup>nd</sup>, 4<sup>th</sup>] 。        
```



**提示：**


- ``n == score.length``
- ``1 <= n <= 10<sup>4</sup>``
- ``0 <= score[i] <= 10<sup>6</sup>``
- ``score`` 中的所有值 **互不相同**



[LeetCode链接](https://leetcode-cn.com/problems/relative-ranks/)

### 思路及代码

存储每个数对应的索引，然后将分数降序排序，依照降序排序后的结果将排名对应到数组位置上。

```cpp
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<pair<int, int>> arr;
        for(int i = 0; i < score.size(); i++){
            arr.push_back(make_pair(-score[i], i));
        }
        sort(arr.begin(), arr.end());   // 将得分以负数形式添加即可使用默认排序算法
        vector<string> res(arr.size());

        vector<string> medals = {"Gold Medal", "Silver Medal", "Bronze Medal"};
        for(int i = 0; i < arr.size(); i++){
            auto p = arr[i];
            if(i > 2){
                res[p.second] = to_string(i+1);
            }
            else{
                res[p.second] = medals[i];
            }
        }
        return res;
    }
};
```