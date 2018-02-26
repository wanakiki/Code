## 24. Swap Nodes in Pairs
##### 2018年2月26日22:43:40
##### 链表
****
### 题目
>Given a linked list, swap every two adjacent nodes and return its head.  
For example,  
Given 1->2->3->4, you should return the list as 2->1->4->3.  
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.  
给定一个链表，交换每两个相邻节点并返回它的头部。 例如， 给定1-> 2-> 3-> 4，您应该返回列表2-> 1-> 4-> 3。 你的算法应该只使用恒定的空间。您不能修改列表中的值，只有节点本身可以​​更改。

### 分析
题目很简单，熟悉链表的操作通过递归就可以解决。当存在两个连续节点就可以交换。  
开始写的时候将``head``的值赋给了新指针``ptr``然后对``ptr``进行了操作，尽管ptr是正确的，但是返回的head却没有改变。  
想到这点，改变了递归的条件，写出了正确的代码。  
也看到了非递归解决方式，不过没有记录。
### 代码
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode *ptr,*temp;
    ptr=head;
    if(ptr!=NULL&&ptr->next!=NULL){
        temp=ptr->next->next;
        ptr->next->next=ptr;
        ptr=ptr->next;
        ptr->next->next=temp;
        head=ptr;
        head->next->next=swapPairs(head->next->next);
    }
    return head;
}
```
