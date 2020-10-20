## 143. Reorder List
##### 2018-05-08 12:44:36
##### 链表重新排序
***
## 题目
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
```
Given 1->2->3->4, reorder it to 1->4->2->3.
```
Example 2:
```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```
## 分析
两个例子已经把排序方法说的很清楚了，我的做法是先遍历一次，然后将所有的指针压入栈中，再从头开始，将栈顶部的元素插入到前面来。

根据节点个数的奇偶性，可能出现的终止情况有两种，第一种是遇到两个指针相等，第二种是当前便利到的指针的下一个元素就是栈顶元素，分别对这两种情况操作，将结尾的节点对应的next改为NULL，就可以解决这个题目。
## 示例代码
我的代码是分两次书写的，有点乱，还可以优化，不过这时候的运行速度就已经很快了，97%
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
    void reorderList(ListNode* head) {
        if(!head )
            return ;
        stack<ListNode *> stk;
        ListNode * tmp1=head,*tmp2=head;
        while(tmp1){
            stk.push(tmp1);
            tmp1=tmp1->next;
        }
        while(tmp2!=stk.top()){   //相等终止循环
            if(tmp2->next == stk.top()){
                stk.top()->next=NULL;
                return ;
            }   //遇到相连则顶部元素的next指向空并终止
            stk.top()->next=tmp2->next;
            tmp2->next=stk.top();
            tmp2=tmp2->next->next;
            stk.pop();
        }
        tmp2->next=NULL;
        return ;
    }
};
```

首先遍历链表，找到中间节点，之后将右半部分链表反转，之后遍历两部分链表，按照题目要求的顺序进行合并。

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
    void reorderList(ListNode* head) {
        if(head == NULL || head->next == NULL || head->next->next == NULL){
            return ;
        }
        // 找到中间节点
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }

        // 反转链表
        ListNode* cur = slow->next;
        ListNode* tmp = cur->next;
        slow->next = NULL;
        cur->next = NULL;
        while(tmp){
            ListNode* last = cur;
            cur = tmp;
            tmp = cur->next;
            cur->next = last;
        }

        // 后半段的头是cur
        ListNode* left = head;
        ListNode* right = cur;
        while(left && right){
            ListNode* l_next = left->next;
            ListNode* r_next = right->next;
            left->next = right;
            right->next = l_next;

            right = r_next;
            left = l_next;
        }
        return ;
    }
};
```