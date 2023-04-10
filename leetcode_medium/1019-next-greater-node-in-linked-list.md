## 1019. 链表中的下一个更大节点

2023-04-10 20:01:44

### 题目

给定一个长度为 ``n`` 的链表 ``head``

对于列表中的每个节点，查找下一个 **更大节点** 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 **严格大于** 它的值。

返回一个整数数组 ``answer`` ，其中 ``answer[i]`` 是第 ``i`` 个节点( **从1开始** )的下一个更大的节点的值。如果第 ``i`` 个节点没有下一个更大的节点，设置 ``answer[i] = 0`` 。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext1.jpg" />

```

输入：head = [2,1,5]
输出：[5,5,0]
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext2.jpg" />

```

输入：head = [2,7,4,3,5]
输出：[7,0,5,5,0]
```

 

**提示：**


- 链表中节点数为 ``n``
- ``1 <= n <= 10<sup>4</sup>``
- ``1 <= Node.val <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/next-greater-node-in-linked-list/)

### 思路及代码

可能是最近一直在忙，这个题想了比较久的时间。实际上是一个经典的单调栈应用，感觉可以拿出来当例题讲。

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        int count = 0;
        ListNode* cur = head;
        while(cur){
            count++;
            cur = cur->next;
        }

        vector<int> res(count, 0);
        stack<pair<int,int>> stk;
        cur = head;
        int index = 0;
        while(cur){
            while(!stk.empty()){
                auto p = stk.top();

                if(p.second >= cur->val){
                    break;
                }
                else{
                    res[p.first] = cur->val;
                    stk.pop();
                }
            }
            
            stk.emplace(make_pair(index, cur->val));
            cur = cur->next;
            index++;
        }

        return res;
    }
};
```