## 514. 自由之路   

2020-11-15 16:49:14

### 题目

电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。       

给定一个字符串 **ring**，表示刻在外环上的编码；给定另一个字符串 **key**，表示需要拼写的关键词。您需要算出能够拼写关键词中 
所有字符的**最少**步数。

最初，**ring**的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 **key**的一个字符在 12:00 方向对齐，然后按
下中心按钮，以此逐个拼写完 **key**中的所有字符。

旋转 **ring**拼出 key 字符 **key[i]**的阶段中：


- 您可以将 **ring**顺时针或逆时针旋转**一个位置**，计为1步。旋转的最终目的是将字符串 **ring **的一个字符与 12:00 方向对齐
，并且这个字符必须等于字符 **key[i] 。**
- 如果字符 **key[i]**已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 **1 步**。按完之后，您可以开始拼写 **key**的下一个字符（下一阶段）, 直至完成所有拼写。


**示例：**

 

<center><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/ring.jpg" style="width: 26%;" /></center>
 

```

输入: ring = "godding", key = "gd"
输出: 4
解释:
 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。
 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
 当然, 我们还需要1步进行拼写。
 因此最终的输出是 4。
```

**提示：**


- **ring** 和 **key** 的字符串长度取值范围均为 1 至 100；
- 两个字符串中都只有小写字符，并且均可能存在重复字符；
- 字符串 **key** 一定可以由字符串 **ring** 旋转拼出。



### 思路及代码

首先需要明确，这个题目是不能贪心去做的，因为当下最优的旋转方式可能会导致后面的字母需要进行额外的旋转。故一定要探索完所有可能情况。

采用动态规划方式进行探索，创建二维数组，横坐标代表key字符串中的每个字母，纵坐标代表该字母在ring字符串中的位置。逐层分析过程中保留最小值。

```cpp
class Solution {
public:
    static int getdistance(int a, int b, int len){
        if(a > b){
            int tmp = b;
            b = a;
            a = tmp;
        }
        return min(b - a, a + len - b);
    }
    int findRotateSteps(string ring, string key) {
        vector<int> pos[26];
        for(int i = 0; i < ring.size(); i++){
            pos[ring[i] - 'a'].push_back(i);
        }

        vector<vector<int>> dp(key.size(), vector<int>(ring.size(), 100000));
        int len = ring.size();
        int res = INT_MAX;
        for(int i = 0; i < key.size(); i++){
            if(i == 0){
                for(int j = 0; j < pos[key[i] - 'a'].size(); j++){
                    int next_pos = pos[key[i] - 'a'][j];

                    // 获取旋转距离
                    dp[i][next_pos] = min(next_pos, len - next_pos) + 1;
                    
                }
            }
            else{
                for(int j = 0; j < ring.size(); j++){
                    if(dp[i-1][j] != 100000){
                        int last_pos = j;
                        
                        // 找到下一个节点
                        for(int k = 0; k < pos[key[i] - 'a'].size(); k++){
                            int next_pos = pos[key[i] - 'a'][k];

                            // 获取距离
                            int tmp_distance = getdistance(last_pos, next_pos, len) + 1 + dp[i-1][last_pos];
                            dp[i][next_pos] = min(dp[i][next_pos], tmp_distance);
                            if(i == key.size() -1){
                                res = min(res, dp[i][next_pos]);
                            }
                            //cout << i << ' '<< last_pos << ' ' << next_pos << ' ' << dp[i][next_pos] << endl;
                        }
                    }
                }
            }
        }
        return res;
    }
};
```