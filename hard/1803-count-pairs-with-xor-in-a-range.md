## 1803. 统计异或值在范围内的数对有多少

2023-01-06 10:35:43

### 题目

给你一个整数数组 ``nums`` （下标 **从 0 开始** 计数）以及两个整数：``low`` 和 ``high`` ，请返回 **漂亮数对** 的数目。

**漂亮数对** 是一个形如 ``(i, j)`` 的数对，其中 ``0 <= i < j < nums.length`` 且 ``low <= (nums[i] XOR nums[j]) <= high`` 。

 

**示例 1：**

```
输入：nums = [1,4,2,7], low = 2, high = 6
输出：6
解释：所有漂亮数对 (i, j) 列出如下：
    - (0, 1): nums[0] XOR nums[1] = 5 
    - (0, 2): nums[0] XOR nums[2] = 3
    - (0, 3): nums[0] XOR nums[3] = 6
    - (1, 2): nums[1] XOR nums[2] = 6
    - (1, 3): nums[1] XOR nums[3] = 3
    - (2, 3): nums[2] XOR nums[3] = 5
```

**示例 2：**

```
输入：nums = [9,8,4,2,1], low = 5, high = 14
输出：8
解释：所有漂亮数对 (i, j) 列出如下：
​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
    - (0, 3): nums[0] XOR nums[3] = 11
    - (0, 4): nums[0] XOR nums[4] = 8
    - (1, 2): nums[1] XOR nums[2] = 12
    - (1, 3): nums[1] XOR nums[3] = 10
    - (1, 4): nums[1] XOR nums[4] = 9
    - (2, 3): nums[2] XOR nums[3] = 6
    - (2, 4): nums[2] XOR nums[4] = 5
```

 

**提示：**


- ``1 <= nums.length <= 2 * 10<sup>4</sup>``
- ``1 <= nums[i] <= 2 * 10<sup>4</sup>``
- ``1 <= low <= high <= 2 * 10<sup>4</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/count-pairs-with-xor-in-a-range/)

### 思路及代码

初见题目只能想到暴力算法，在官方提示的帮助下勉勉强强实现了代码。其实题目整体思路并不复杂，暴力算法下需要对多个数据进行异或运算，但异或结果与边界进行比较时是从最高位开始的，例如上界的最高位为1，则在最高位异或结果为0的全部数对都是满足条件的，不需要对后续二进制位的异或结果进行判断。但需要注意计算最高位异或结果为1但后续二进制位异或结果满足小于边界值的数对个数。这个过程可以递归执行，直到找到所有满足条件的数。

上述比较过程可以使用只有两个子节点的前缀树实现，代码中只要实现添加数字和查找异或结果小于等于 k 的数对个数两个功能即可。

设 CountK(k) 函数能够查找异或结果小于等于 k 的数对个数，则本题要求的数值范围可以使用 CountK(high) - CountK(low - 1) 计算得到。

下面是手动实现前缀树的代码：

```cpp
class Node{
public:
    Node* left;
    Node* right;    // 右节点代表1
    int count;
    bool flag;  // 自身对应为1或0的标志

    Node(bool _flag){
        left = nullptr;
        right = nullptr;
        count = 1;
        flag = _flag;
    }
};

class Tree{
public:
    Node* root;
    Tree(){ root = new Node(false); }

    void insert(int n, int index){
        Node* cur_node = root;
        while(index >= 0){
            // 判断数值对应位是否为1并添加节点
            int cur_flag = n & (1 << index);
            index--;

            if(cur_flag){
                if(cur_node->right){
                    cur_node = cur_node->right;
                    cur_node->count++;
                }
                else{
                    cur_node->right = new Node(cur_flag);
                    cur_node = cur_node->right;
                }
            }
            else{
                if(!cur_node->left){
                    cur_node->left = new Node(cur_flag);
                    cur_node = cur_node->left;
                }
                else{
                    cur_node = cur_node->left;
                    cur_node->count++;
                }
                
            }
        }
        return ;
    }

    int countK(int k, int n, int index){
        return helperCountK(root, k, n, index);
    }

    int getChild(Node* cur_node, bool flag){
        // 获取左右节点的个数 如果节点为空则返回0
        if(flag){
            if(cur_node->right) return cur_node->right->count;
            else    return 0;
        }
        else{
            if(cur_node->left)  return cur_node->left->count;
            else    return 0;
        }
    }
    int helperCountK(Node* cur_node, int k, int n, int index){
        if(cur_node == nullptr) return 0;
        if(index < 0){
            return cur_node->count;
        }
        // 如果k中当前位为1，则需要返回当前位异或后为0的个数 + 当前位异或后为1且在k的下一位满足条件的数字个数
        // 如果k当前位为0，需要返回当前位异或后为0且在下一位满足条件的数字个数

        // 根据异或的特性对n的取值做特殊判断

        int k_flag = k & (1 << index);
        int n_flag = n & (1 << index);
        index--;

        if(k_flag){
            if(n_flag){
                // return cur_node->right->count + helperCountK(cur_node->left, k, n, index);
                return getChild(cur_node, true)+ helperCountK(cur_node->left, k, n, index);
            }
            else{
                // return cur_node->left->count + helperCountK(cur_node->right, k, n, index);
                return getChild(cur_node, false) + helperCountK(cur_node->right, k, n, index);
            }
        }
        else{
            if(n_flag){
                return helperCountK(cur_node->right, k, n, index);
            }
            else{
                return helperCountK(cur_node->left, k, n, index);
            }
        }
        return 0;
    }
};
class Solution {
public:
    int countPairs(vector<int>& nums, int low, int high) {
        // 16 位二进制数可以包含题目数据范围
        Tree tree;
        int res = 0;
        low -= 1;
        int mask = 14;

        for(int i = nums.size() - 1; i >= 0; i--){
            int high_count = tree.countK(high, nums[i], mask);
            int low_count = tree.countK(low, nums[i], mask);
            res += high_count - low_count;
            tree.insert(nums[i], mask);
            cout << high_count << ' ' << low_count << endl;
        }
        return res;
    }
};
```