## 726. 原子的数量 

2021-07-05 19:22:07

### 题目

给定一个化学式``formula``（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表 
达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式 ``formula`` ，返回所有原子的数量。格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1）， 
然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

 

**示例 1：**

```
输入：formula = "H2O"
输出："H2O"
解释：
原子的数量是 {'H': 2, 'O': 1}。
```

**示例 2：**

```
输入：formula = "Mg(OH)2"
输出："H2MgO2"
解释：
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
```

**示例 3：**

```
输入：formula = "K4(ON(SO3)2)2"
输出："K4N2O14S4"
解释：
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
```

**示例 4：**

```
输入：formula = "Be32"
输出："Be32"
```

 

**提示：**


- ``1 <= formula.length <= 1000``
- ``formula`` 由小写英文字母、数字 ``'('`` 和 ``')'`` 组成。
- ``formula`` 是有效的化学式。



[LeetCode链接](https://leetcode-cn.com/problems/number-of-atoms/)

### 思路及代码

单次扫描配合递归，写了一个多小时。

遍历字符串，遇到括号时将括号内子串提出，按照新的比例重复调用处理函数。过程中需要注意较多小细节，代码写得比较难看。

个人感觉使用栈来做可能更合适，保存每个元素名称和出现次数，压入栈中。根据两侧的括号判断是否需要乘额外的倍率。

```cpp
class Solution {
public:
    map<string, int> hash;

    // 辅助函数

    // 自动拆分括号 递归调用 
    void helper(string formula, int ratio = 1){
        bool flag = false;  // 标志是否正在查找括号
        int count = 0;      // 当前遇到额外左括号的数量

        int start_pos = 0;
        for(int i = 0; i < formula.size(); i++){
            if(flag){
                if(formula[i] == '('){
                    count ++;
                }

                if(formula[i] == ')'){
                    if(count != 0){
                        count --;
                        continue;
                    }

                flag = false;   // 清空查找状态

                // 找到右括号之后判断括号之后是否有数字，并更新索引位置
                int end_pos = i + 1;

                if(end_pos < formula.size() && formula[end_pos] <= '9' && formula[end_pos] >= '0'){
                    helper(formula.substr(start_pos + 1, end_pos - start_pos - 2), ratio * stoi(formula.substr(end_pos)));
                    i += 1;     // 有数字需要更新到数字位置 没有数字不需要更新
                }
                else{
                    helper(formula.substr(start_pos + 1, end_pos - start_pos - 2), ratio);
                }
                }
            }
            else{
                if(formula[i] == '('){
                    flag = true;
                    start_pos = i;
                }
                else if(formula[i] >= 'A' && formula[i] <= 'Z'){
                    // 只从大写字母位置开始判断
                    int cur_ratio = 1;
                    int start_pos = i, end_pos = formula.size() - 1;    // 结束位置默认为字符串末尾，遇到其他元素或数字缩短
                    for(int j = i + 1; j < formula.size(); j++){
                        // 遇到另外的大写字母或者括号表示到达末尾
                        if((formula[j] >= 'A' && formula[j] <= 'Z') || formula[j] == '(' || formula[j] == ')'){
                            end_pos = j - 1;
                            i = j - 1;
                            break;
                        }

                        if(isdigit(formula[j])){
                            cur_ratio = stoi(formula.substr(j));
                            i = j;
                            end_pos = j - 1;
                            break;
                        }
                    }

                    // 截取字符并保存
                    string cur_element = formula.substr(start_pos, end_pos - start_pos + 1);
                    // cout << formula << ' ' << start_pos << ' ' << end_pos << endl;
                    // cout << cur_element << ' ' << cur_ratio * ratio << endl;
                    hash[cur_element] += cur_ratio * ratio;
                }
            }
        }
    }

    string countOfAtoms(string formula) {
        helper(formula);
        string res = "";
        for(auto p : hash){
            res += p.first;
            if(p.second != 1){
                res += to_string(p.second);
            }
        }
        return res;
    }
};
```