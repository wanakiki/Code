## 82. Remove Duplicates from Sorted List II
##### 2018-03-28 
##### 双指针
***
## 1.题目
>Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
>给定有序链表，要求去除其中的所有重复元素。
>
>For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 

## 2.分析
与之前想到的统计法不同，这次了解到了双指针的方法，但是头节点的处理还没有写出来，睡醒补上.....

最开始尝试着去寻找一次遍历解决去头的方法，但还是失败了。
但是了解到了一个新思路，可以写一个包含单独的去头部分的代码，采用递归写法，返回f(第一个不相同的节点的指针)，另外有处理非头部重复的代码。

上面方法很好，但是感觉很难想到，采用了另一种实现的方法，设置一个**新节点**，让其下一个节点为head，  
接着，用这个节点为左指针，使用while循环，在循环中定义右指针并进行处理，最终返回新节点的next

## 3.代码
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
  struct ListNode *newhead=(struct ListNode *)malloc(sizeof(struct ListNode));
  newhead->next=head;
  struct ListNode * pre=newhead;
  while(pre->next){
    struct ListNode*cur=pre->next;
    while (cur->next && cur->next->val == cur->val) {
      cur=cur->next;
    }
    if(cur!=pre->next)
      pre->next=cur->next;
    else
      pre=pre->next;
  }
  return newhead->next;
}
```
