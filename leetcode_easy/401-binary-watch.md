## 401. 二进制手表

2020年2月9日

### 题目

二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。![示意图](https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg)

例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

案例:

```no
输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
```

注意事项:

1. 输出的顺序没有要求。
2. 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
3. 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-watch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```cpp
class Solution {
public:
    vector<string> res;
    // 根据位数输出所有可能值
    vector<string> tmp;
    void helper(int n,  bool is_hour = true, int cur = 0, int index = 0){
        cout << is_hour << ' ' << cur << ' ' << n << endl;
        // 判断溢出
        if((is_hour && (cur > 11 || index > 4)) || (!is_hour && (cur > 59 || index > 6))){
            return ;
        }

        if(n == 0){
            if(is_hour){
                tmp.push_back(to_string(cur));
            }
            else{
                if(cur < 10){
                    tmp.push_back('0' + to_string(cur));
                }
                else{
                    tmp.push_back(to_string(cur));
                }
            }
        }
        else{
            helper(n - 1, is_hour, cur | (1 << index), index + 1);
            helper(n, is_hour, cur, index + 1);
        }
    }
    vector<string> readBinaryWatch(int turnedOn) {
        for(int i = 0; i <= turnedOn; i++){
            int h_count = i;
            int m_count = turnedOn - i;
            if(h_count >= 4 || m_count >= 6){
                continue;
            }

            // 分别判断时、分可能情况
            tmp.clear();
            helper(h_count);
            vector<string> hours(tmp);

            tmp.clear();
            helper(m_count, false);
            vector<string> minutes(tmp);

            for(auto h : hours){
                for(auto m : minutes){
                    res.push_back(h + ':' + m);
                }
            }
        }
        return res;
    }
};
```

枚举0-11、0-59的所有数字，获取其中二进制位1的个数，统计总数为num的情况。

```cpp
class Solution {
public:
    int helper(int n){
        int res = 0;
        while(n){
            n = n&(n-1);
            res++;
        }
        return res;
    }
    vector<string> readBinaryWatch(int num) {
        vector<string> res;
        for(int i = 0; i < 12; i++){
            int h = helper(i);
            // if(h > num)
            //     break;
            // else 
            if(h == num)
                res.push_back(to_string(i) + ":00");
            else{
                int min = num - h;
                for(int j = 0; j < 60; j++){
                    int m = helper(j);
                    // if(m > min)
                    //     break;
                    // else 
                    //数的大小与二进制1个数不成正比
                    if(m == min)
                        res.push_back(to_string(i) + (j < 10 ? ":0" + to_string(j) : ":" + to_string(j)));
                }
            }
        }
        return res;
    }
};
```

