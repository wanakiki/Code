## 142. Linked List Cycle II
##### 2018-05-07 11:32:49
##### 返回链表循环开始的节点
****
## 题目
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
## 分析
双指针法，感觉和数学的关系比较大，引用了部分网上的见解，然后做了些自己的修改。  ↓↓↓
>假设慢指针 slow 走过 x个节点和快指针 fast 在位置 s 相遇，此时快指针走过了 2x 个节点。如果慢指针再走 x 个节点，又会回到这个位置 s。
>
>当慢指针在位置 s 的时候，同时再来一个新的慢指针 new_slow 从起点出发，和慢指针同时再走过 x 个节点，它们也一定会在 s 相遇。重点来了，既然慢指针 slow 和 new_slow 在 s 相遇，因为两个行进速度相同，所以第一次相同的点就是循环开始的节点。

## 示例代码
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow=head , *fast=head;
        while(fast && fast->next){
            fast=fast->next->next;
            slow=slow->next;
            if(slow==fast){
                fast=head;
                while(slow!=fast){
                    slow=slow->next;
                    fast=fast->next;
                }
                return slow;
            }
        }
        return NULL;
    }
};
```
