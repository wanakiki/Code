## 61. Rotate List
##### 2018-03-13 
***
## 1.题目
>Given a list, rotate the list to the right by k places, where k is non-negative.  
给定一个链表，将链表向右旋转k个地方，其中k是非负数。  
Example:
Given 1->2->3->4->5->NULL and k = 2,
>
>return 4->5->1->2->3->NULL.

## 2.分析
搞不懂题目的实现方式，为什么会有[1] 99 这种神奇的输入方式，对代码进行了修改但是还得不到结果，但是对于k小于等于链表长的情况都做到实现了。

## 3.代码
```c
struct ListNode *rotateRight(struct ListNode *head, int k) {
    if (!head || k == 0) return head;
    int len=0;
    struct ListNode *ptr,*newhead;
    while(ptr){
      ptr=ptr->next;
      len++;
    }
    ptr=head;
    for(int i=0;i<k;i++)
      ptr=ptr->next;

    newhead=ptr->next;
    ptr->next=NULL;

    ptr=newhead;
    for(int i=0;i<len-k-2;i++)  //推导关系...
    {
      ptr=ptr->next;
    }
    ptr->next=head;

    return newhead;
}
```

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
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head)   return head;

        // 统计长度
        int len = 0;
        ListNode* cur = head;
        while(cur){
            len++;
            cur = cur->next;
        }

        k %= len;
        if(k == 0)  return head;

        int new_head_index = len - k - 1;
        int cur_pos = 0;
        cur = head;
        ListNode* new_head;

        // 找到分割位置
        while(cur){
            if(new_head_index == cur_pos){
                new_head = cur->next;
                cur->next = nullptr;
                break;
            }
            cur = cur->next;
            cur_pos++;
        }

        // 拼接原有链表
        cur = new_head;
        while(cur->next){
            cur = cur->next;
        }
        cur->next = head;
        
        return new_head;
    }
};
```

最好在第一次遍历获取长度的时候就把链表的首尾连接起来。