## 682. 棒球比赛

2020年2月26日

### 题目

你现在是棒球比赛记录员。
给定一个字符串列表，每个字符串可以是以下四种类型之一：
1. 整数（一轮的得分）：直接表示您在本轮中获得的积分数。
2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。

每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
你需要返回你在所有回合中得分的总和。

示例 1:
```no
输入: ["5","2","C","D","+"]
输出: 30
解释: 
第1轮：你可以得到5分。总和是：5。
第2轮：你可以得到2分。总和是：7。
操作1：第2轮的数据无效。总和是：5。
第3轮：你可以得到10分（第2轮的数据已被删除）。总数是：15。
第4轮：你可以得到5 + 10 = 15分。总数是：30。
```
示例 2:
```no
输入: ["5","-2","4","C","D","9","+","+"]
输出: 27
解释: 
第1轮：你可以得到5分。总和是：5。
第2轮：你可以得到-2分。总数是：3。
第3轮：你可以得到4分。总和是：7。
操作1：第3轮的数据无效。总数是：3。
第4轮：你可以得到-4分（第三轮的数据已被删除）。总和是：-1。
第5轮：你可以得到9分。总数是：8。
第6轮：你可以得到-4 + 9 = 5分。总数是13。
第7轮：你可以得到9 + 5 = 14分。总数是27。
```

注意：

- 输入列表的大小将介于1和1000之间。
- 列表中的每个整数都将介于-30000和30000之间。

来源：力扣（LeetCode）  
链接：https://leetcode-cn.com/problems/baseball-game

### 代码

执行用时:8ms,在所有C++提交中击败了70.51%的用户  
内存消耗:10.8MB,在所有C++提交中击败了5.43%的用户

```cpp
class Solution {
public:
    int calPoints(vector<string>& ops) {
        int sum = 0;
        stack<int> store;
        for(int i = 0; i < ops.size(); i++){
            if(ops[i] == "C"){
                int temp = store.top();
                store.pop();
                sum -= temp;
            }
            else if(ops[i] == "D"){
                int temp = store.top();
                temp *= 2;
                sum += temp;
                store.push(temp);
            }
            else if(ops[i] == "+"){
                int temp1 = store.top();
                store.pop();
                int temp2 = store.top();
                temp2 += temp1;
                store.push(temp1);
                store.push(temp2);
                sum += temp2;
            }
            else{
                int temp = atoi(ops[i].c_str());
                //或者是stoi
                sum += temp;
                store.push(temp);
            }
        }
        return sum;
    }
};
```

2022年3月26日

```cpp
class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> nums(1000, 0);
        int real_index = 0;
        for(auto s : ops){
            if(s == "C"){
                real_index--;
            }
            else if(s == "D"){
                nums[real_index] = nums[real_index - 1] * 2;
                real_index++;
            }
            else if(s == "+"){
                nums[real_index] = nums[real_index - 1] + nums[real_index - 2];
                real_index++;
            }
            else{
                nums[real_index] = stoi(s);
                real_index++;
            }
        }
        int res = 0;
        for(int i = 0; i < real_index; i++){
            res += nums[i];
        }
        return res;
    }
};
```