## 92. Reverse Linked List II
##### 2018-03-31 22:35:17
##### 继续了解添头操作
***
## 1.题目
> Reverse a linked list from position m to n. Do it in-place and in one-pass.
>
>For example:
>Given 1->2->3->4->5->NULL, m = 2 and n = 4,
>
>return 1->4->3->2->5->NULL.
>
>Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.  
>反转从位置m到n的链接列表。在原地进行并一次完成。例如：给定1-> 2-> 3-> 4-> 5-> NULL，m = 2且n = 4，返回1-> 4-> 3-> 2-> 5-> NULL。注：给定m，n满足以下条件：1≤m≤n≤列表长度。

## 2.分析
尽管先做了链表反转，但是还是不熟悉解决方式，单向链表的反转还是比较费脑子的问题。  
看到别人的思路，用双指针处理，先遍历到反转的开始位置，记录，再进行添头操作（反转链表1），一直处理到反转结束的位置。  
**新建一个节点指向头是一个较好的处理方式。**

## 3.代码
```c
struct ListNode* reverseBetween(struct ListNode* head, int m, int n) {
    struct ListNode * newhead;
    newhead=(struct ListNode * )malloc(sizeof(struct ListNode));
    newhead->next=head;
    struct ListNode * pre = newhead;  //用来记录开始位置
    for(int i=0;i<m-1;i++)
      pre=pre -> next;
    struct ListNode * cur=pre->next;  //记录当前位置
    for(int i=0;i<n-m;i++){
      struct ListNode * move = cur ->next;
      cur->next=move->next;
      move->next=pre->next;
      pre->next=move;   //也是执行加头的操作
    }
    return newhead->next;
}
```
[参考代码](https://leetcode.com/problems/reverse-linked-list-ii/discuss/30668/12-lines-4ms-C++)
