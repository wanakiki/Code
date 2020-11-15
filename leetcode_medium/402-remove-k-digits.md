## 402. 移掉K位数字

2020-11-15 12:36:11

### 题目

给定一个以字符串表示的非负整数*num*，移除这个数中的*k*位数字，使得剩下的数字最小。

**注意:**


- *num* 的长度小于 10002 且&ge;*k。*
- *num* 不会包含任何前导零。


**示例 1 :**

```

输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
```

**示例 2 :**

```

输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
```

**示例 3 :**

```

输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。
```


### 思路及代码

如果要使删除之后的数有最小值，则要求删除之后靠前位置的数尽可能小，可以用单调栈来维护。

算法思路比较清晰，但是实现的时候需要注意一些细节：

1. 当维护递增序列之后并没有删除K个数，则需要去掉末尾部分数据
2. 最后取出数据时需要注意避免前导零
3. 若最后字符串为空，则应返回零


```cpp
class Solution {
public:
    string removeKdigits(string num, int k) {
        deque<int> q;
        for(int i = 0; i < num.size(); i++){
            int tmp = num[i] - '0';
            while(!q.empty() && tmp < q.back() && k){
                q.pop_back();
                k--;
            }
            q.push_back(tmp);
        }
        // 删除多余的节点
        while(k){
            q.pop_back();
            k--;
        }


        string res = "";
        bool flag = true;
        while(!q.empty()){
            int tmp = q.front();
            q.pop_front();
            if(flag && tmp == 0){
                continue;
            }
            if(tmp != 0){
                flag = false;
            }
            res += tmp + '0';
        }
        if(res == ""){
            return "0";
        }
        return res;
    }
};
```