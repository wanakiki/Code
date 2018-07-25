## 241. Different Ways to Add Parentheses
##### 2018年7月25日
***
### 题目
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:
```
Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
```
Example 2:
```
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
```
### 分析
这道题明明可以更难，但是他选择了简单....输出数组允许重复项，解题简单多了。

很明显，这道题可以用递归来解决，查找到一个运算符之后就从这个位置将数组分为两个部分进行递归，再将两个数组中所有的元素按照运算符进行操作并添加到返回数组。

要注意的一点是只有一个数字也要将它添加到返回数组，并且**因为函数是递归调用的，只要把所剩的字符串转化为整数就可以**，不用管有几位数字。

### 示例代码
C++：
```cpp
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> res;
        for(int i = 0; i < input.size(); i++){
            if(input[i] < '0'){
                vector<int> left = diffWaysToCompute(input.substr(0,i));
                vector<int> right = diffWaysToCompute(input.substr(i + 1));
                for(int j = 0; j < left.size(); j++)
                    for(int k = 0; k < right.size(); k++){
                        if(input[i] == '+')
                            res.push_back(left[j] + right[k]);
                        else if(input[i] == '-')
                            res.push_back(left[j] - right[k]);
                        else
                            res.push_back(left[j] * right[k]);
                    }
            }
        }
        if(res.empty())
            //res.push_back(input[0] - '0');  开始以为只有一位...
            res.push_back(atoi(input.c_str()));  //最佳方式
            //res.push_back(stoi(input.substr(l, r - l + 1)))  //有了意识，但是没有理解递归
        return res;
    }
};
```
