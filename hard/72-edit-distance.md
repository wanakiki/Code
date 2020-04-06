## 72. 编辑距离

2020年4月6日

### 题目

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

- 插入一个字符
- 删除一个字符
- 替换一个字符
 

示例 1：
```no
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```
示例 2：
```no
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

来源：力扣（LeetCode）  
链接：https://leetcode-cn.com/problems/edit-distance


### 代码

二维DP，转移方程也比较容易推，但理解起来稍微有点麻烦。

设两个单词分别为A、B，则

1. A中插入字符与B中删除字符等价
2. B中插入字符与A中删除字符等价
3. A中替换字符与B中替换字符等价

故实际操作只有三种情况，当前计算的元素的取值对应情况为（设A横向B纵向）：

1. dp[i-1][j-1]，A、B当前位置字符相同则不需要操作，字符不同则需要进行替换
2. dp[i-1][j]，A删除或者B插入
3. dp[i][j-1], B删除或者A插入


```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int len1 = word1.size(), len2 = word2.size();
        int dp_table[len1+1][len2+1];

        // 基本情况
        for(int i = 0; i <= len1; i++)
            dp_table[i][0] = i;
        for(int i = 0; i <= len2; i++)
            dp_table[0][i] = i;
        
        for(int i = 1; i <= len1; i++)
        for(int j = 1; j <= len2; j++){
            if(word1[i-1] == word2[j-1]){
                dp_table[i][j] = min(dp_table[i-1][j-1]-1, min(dp_table[i-1][j], dp_table[i][j-1])) + 1;
            }
            else{
                dp_table[i][j] = min(dp_table[i-1][j-1], min(dp_table[i-1][j], dp_table[i][j-1])) + 1;
            }
        }
        return dp_table[len1][len2];
    }
};
```

在其基础上增加了记录路径的代码，从结果反向查找到边缘，并标记沿途的点，因为不同单词的插入与删除操作是等价的，所以可以进行额外的处理确保操作能够完成将A转化为B的任务。

```cpp
class Solution {
public:
    class Node{
    public:
        int value;
        int method;
        int from;
        Node(){
            value = 0;
            method = 0;
            from = -1;
        }
    };

    int directions[3][2] = {{0, -1}, {-1,-1}, {-1,0}};
    int minDistance(string word1, string word2) {
        int len1 = word1.size(), len2 = word2.size();
        Node dp_table[len1+1][len2+1];

        // 基本情况
        for(int i = 0; i <= len1; i++)
            dp_table[i][0].value = i;
        for(int i = 0; i <= len2; i++)
            dp_table[0][i].value = i;
        
        for(int i = 1; i <= len1; i++)
        for(int j = 1; j <= len2; j++){
            int from = -1;
            int next_value = INT_MAX;
            for(int k = 0; k < 3; k ++){
                int tmp = 0;
                if(k == 1){
                    tmp = dp_table[i-1][j-1].value;
                    if(word1[i] != word2[j]){
                        tmp += 1;
                    }
                }
                else{
                    tmp = dp_table[i+directions[k][0]][j+directions[k][1]].value + 1;
                }
                // 保存当前坐标的上一个点
                if(tmp < next_value){
                    next_value = tmp;
                    from = k;
                }
            }

            // 更新
            dp_table[i][j].value = next_value;
            dp_table[i][j].from = from;
        }

        // 逆向遍历，绘制路径
        int from = dp_table[len1][len2].from;
        int cur_i = len1, cur_j = len2;
        while(from!=-1){
            cur_i += directions[from][0];
            cur_j += directions[from][1];
            dp_table[cur_i][cur_j].show = true;
            dp_table[cur_i][cur_j].method = from+1;
            from = dp_table[cur_i][cur_j].from;
        }
        // 输出
        string methods[5] = {"n", "l", "s", "d"};
        for(int i = 1; i <= len1; i++){
            for(int j = 1; j <= len2; j++){
                cout << methods[dp_table[i][j].method] << '|';
            }
            cout << endl;
        }
        
        return dp_table[len1][len2].value;
    }
};
```