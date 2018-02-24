## 19. Remove Nth Node From End of List
##### 2018年2月24日22:02:45
##### 链表双指针
***
### 题目
>Given a linked list, remove the nth node from the end of list and return its head.  
For example,
```
  Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
```
>**Note**:
Given n will always be valid.
Try to do this in one pass.

### 分析
本来打算先遍历得到长度，但是不满足要求，说一下更方便的双指针方法。
此处两个指针之间的距离是n，当快指针走到末尾时，满指针所在的位置就是要去掉的位置。但是为了方便去除，我们需要设置终止位置为fast->next==NULL，这样我们就能方便的去除了。  
还要注意，当需要去除的是第一位时，fast已经是NULL了。
### 代码
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode*slow=head,*fast=head;
    for(int i=0;i<n;i++){
        fast=fast->next;
    }
    if(fast==NULL){
        head=head->next;
        return head;
    }
    while(fast->next!=NULL){
        fast=fast->next;
        slow=slow->next;
    }	//特例
    slow->next=slow->next->next;
    return head;
}
```
别人的（提交之后看到的）
```c
struct ListNode* front = head;
struct ListNode* behind = head;

while (front != NULL) {
    front = front->next;
    
    if (n-- < 0) behind = behind->next;
}
if (n == 0) head = head->next;
else behind->next = behind->next->next;
return head;
}
```
