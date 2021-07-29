## 1194. 二叉树寻路

2021-07-29 21:35:21

### 题目

在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 **逐行** 依次按 &ldquo;之&rdquo; 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行&hellip;&hellip;）中，按从左到右的顺序进行标记；        

而偶数行（即，第二行、第四行、第六行&hellip;&hellip;）中，按从右到左的顺序进行标记。

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/28/tree.png" style="height: 138px; width: 300px;">

给你树上某一个节点的标号 ``label``，请你返回从根节点到该标号为 ``label`` 节点的路径，该路径是由途经的节点标号所组成的。   



**示例 1：**

```
输入：label = 14
输出：[1,3,4,14]
```

**示例 2：**

```
输入：label = 26
输出：[1,2,6,10,26]
```



**提示：**


- ``1 <= label <= 10^6``



[LeetCode链接](https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree/)

### 思路及代码

首先不考虑偶数层反向编码，针对于完全二叉树而言，从根节点出发，从对应二进制数值第二位开始判断，遇到0左拐，遇到一右拐，便是通向某个数值的路径。

当采用反向编码之后，偶数层某一位置节点数值与完全二叉树对应值相加为一定值，假设完全二叉树中第一个元素值为n，则二者和为3n-1。

在此基础之上便可以通过一种相对繁琐的方法解决题目：首先判断数据对应二进制的位数，如果位于偶数层，按照上述规则求出标准完全二叉树中对应的数值，位于奇数层则不做修改。

之后从二进制第二位开始判断下一个值向左还是向右，过程中记录当前层数，对于偶数层保存反向编码后对应的值，奇数层则保留原值。


```cpp
class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        vector<int> res = {1};

        int cmp = 1;    // 用于比较的值
        int len = 1;
        while(cmp < label){
            cmp <<= 1;
            len++;
        }

        // 计算出真实位置对应值
        if(cmp == label ){
            if( len % 2 == 0) label = cmp * 3 - 1 - label;
            cmp >>= 1;
        }
        else if(cmp > label){
            if(len % 2 == 1)    label = 3 * (cmp / 2) - 1 - label;
            cmp >>= 2;
        }
        int last = 1;
        int level = 2;
        int first_n = 2;
        while(cmp){
            int cur = last * 2;
            if(label & cmp){
                cur = cur + 1;
            }
            last = cur;     //计算反向值之前保存

            // 偶数层计算反向值
            if(level % 2 == 0){
                cur = 3 * first_n - 1 - cur;
            }
            res.push_back(cur);

            cmp >>= 1;
            level+=1;
            first_n <<= 1;
        }
        return res;
    }
};
```