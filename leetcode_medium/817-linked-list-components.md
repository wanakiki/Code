## 817. 链表组件

2022-10-12 09:57:03

### 题目

给定链表头结点 ``head``，该链表上的每个结点都有一个 **唯一的整型值** 。同时给定列表 ``nums``，该列表是上述链表中整型值的一个子集。

返回列表 ``nums`` 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 ``nums`` 中）构成的集合。



**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom1.jpg" />

```
输入: head = [0,1,2,3], nums = [0,1,3]
输出: 2
解释: 链表中,0 和 1 是相连接的，且 nums 中不包含 2，所以 [0, 1] 是 nums 的一个组件，同理 [3] 也是一个组件，故返回 2。
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom2.jpg" />

```
输入: head = [0,1,2,3,4], nums = [0,3,1,4]
输出: 2
解释: 链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。
```



**提示：**


- 链表中节点数为``n``
- ``1 <= n <= 10<sup>4</sup>``
- ``0 <= Node.val < n``
- ``Node.val`` 中所有值 **不同**
- ``1 <= nums.length <= n``
- ``0 <= nums[i] < n``
- ``nums`` 中所有值 **不同**



[LeetCode链接](https://leetcode-cn.com/problems/linked-list-components/)

### 思路及代码

使用哈希表统计 nums 中的所有数字，遍历链表并计数。

可以使用 ``unordered_set<int>(nums.begin(), nums.end())`` 直接初始化。

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
    int numComponents(ListNode* head, vector<int>& nums) {
        unordered_map<int,int> hash;
        for(auto n : nums){
            hash[n]++;
        }

        int res = 0;
        bool last_flag, cur_flag;
        last_flag = false;
        while(head){
            if(hash.find(head->val) != hash.end()){
                cur_flag = true;
            }
            else{
                cur_flag = false;
            }

            if(cur_flag == true && last_flag == false)  res++;

            last_flag = cur_flag;
            head = head->next;
        }
        return res;
    }
};
```