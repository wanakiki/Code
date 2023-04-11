## 1041. 困于环中的机器人

2023-04-11 10:09:50

### 题目

在无限的平面上，机器人最初位于 ``(0, 0)`` 处，面朝北方。注意:


- **北方向** 是y轴的正方向。
- **南方向** 是y轴的负方向。
- **东方向** 是x轴的正方向。
- **西方向** 是x轴的负方向。


机器人可以接受下列三条指令之一：


- ``"G"``：直走 1 个单位
- ``"L"``：左转 90 度
- ``"R"``：右转 90 度


机器人按顺序执行指令 ``instructions``，并一直重复它们。

只有在平面中存在环使得机器人永远无法离开时，返回 ``true``。否则，返回 ``false``。

 

**示例 1：**

```
输入：instructions = "GGLLGG"
输出：true
解释：机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“G”:移动一步。位置:(0,2).方向:北。
“L”:逆时针旋转90度。位置:(0,2).方向:西。
“L”:逆时针旋转90度。位置:(0,2)方向:南。
“G”:移动一步。位置:(0,1)方向:南。
“G”:移动一步。位置:(0,0)方向:南。
重复指令，机器人进入循环:(0,0)——>(0,1)——>(0,2)——>(0,1)——>(0,0)。
在此基础上，我们返回true。
```

**示例 2：**

```
输入：instructions = "GG"
输出：false
解释：机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“G”:移动一步。位置:(0,2).方向:北。
重复这些指示，继续朝北前进，不会进入循环。
在此基础上，返回false。
```

**示例 3：**

```

输入：instructions = "GL"
输出：true
解释：机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“L”:逆时针旋转90度。位置:(0,1).方向:西。
“G”:移动一步。位置:(- 1,1)方向:西。
“L”:逆时针旋转90度。位置:(- 1,1)方向:南。
“G”:移动一步。位置:(- 1,0)方向:南。
“L”:逆时针旋转90度。位置:(- 1,0)方向:东方。
“G”:移动一步。位置:(0,0)方向:东方。
“L”:逆时针旋转90度。位置:(0,0)方向:北。
重复指令，机器人进入循环:(0,0)——>(0,1)——>(- 1,1)——>(- 1,0)——>(0,0)。
在此基础上，我们返回true。
```

 

**提示：**


- ``1 <= instructions.length <= 100``
- ``instructions[i]`` 仅包含 ``'G', 'L', 'R'``



[LeetCode链接](https://leetcode-cn.com/problems/robot-bounded-in-circle/)

### 思路及代码

指令是在循环执行的，不会出现环的条件是指令单次执行完毕后方向不变，且不能回到原点。不能回到原点比较容易理解，相当于每次循环的位移为零。而要求方向不变的原因是，方向的可能情况只有四种，且每次执行之后位移大小确定，如果方向每次都发生固定改变，则必然会回到原来的位置。

```cpp
class Solution {
public:
    bool isRobotBounded(string instructions) {
        vector<vector<int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int cur_direction = 0;
        int cur_posx = 0;
        int cur_posy = 0;

        for(auto c : instructions){
            if(c == 'G'){
                cur_posx += directions[cur_direction][0];
                cur_posy += directions[cur_direction][1];
            }
            else if(c == 'L'){
                cur_direction -= 1;
                cur_direction = (cur_direction + 4) % 4;
            }
            else{
                cur_direction += 1;
                cur_direction = (cur_direction + 4) % 4;
            }
        }

        // cout << cur_direction << endl;
        if(cur_direction == 0 && (cur_posx != 0 || cur_posy != 0))  return false;
        else    return true;
    }
};
```