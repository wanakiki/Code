## 203. Remove Linked List Elements
##### 2018-06-07 10:41:03
##### 链表去重
***
## 题目

Remove all elements from a linked list of integers that have value val.

Example:
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
````
## 分析
定义一个新的指针指向整个链表，然后对每个元素进行判断，相等就删去，要注意继续判断下一个节点，指针不会移动。
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
    ListNode* removeElements(ListNode* head, int val) {
        if(!head)
            return head;
        
        ListNode * newhead,*ptr;
        newhead = new ListNode(0);
        newhead->next=head;
        ptr = newhead;
        while(ptr -> next){
            if(ptr->next->val == val){
                ptr->next= ptr->next->next;
                continue;   //指针不移动 继续判断
            }
            ptr=ptr->next;
        }
        return newhead->next;
    }
};
```
