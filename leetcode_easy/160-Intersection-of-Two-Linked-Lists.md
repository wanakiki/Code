## 160. Intersection of Two Linked Lists
##### 2018-03-15
***
## 1.题目
>Write a program to find the node at which the intersection of two singly linked lists begins.
Notes:
>
>  - If the two linked lists have no intersection at all, return null.
>  -  The linked lists must retain their original structure after the function - returns.
>  -   You may assume there are no cycles anywhere in the entire linked structure.
>  -  Your code should preferably run in O(n) time and use only O(1) memory.  

>编写一个程序来查找两个单链表的交集的起始点。  
注:如果两个链表没有交集，返回null。   链表在函数返回后必须保留原来的结构。  您可以假设在整个链接结构中没有任何环。  您的代码最好在o（n）时间运行，只使用o（1）内存。

For example, the following two linked lists:
```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```
begin to intersect at node c1.

## 2.分析
从上图不难看出，两个链表如果相交一定从某一位置开始重合，一直到链表末尾。  
针对这个特点，我的做法是分别算出两个链表的长度，对其进行处理，使两链表长度相等。  
之后开启同步判断，如果发现两指针相等，则该点就是交点，返回当前指针（两个都可以）。
用这种方法判断，如果没有交点，两个链表就会一直遍历到最后，此时返回的headA也为空。

感觉比较麻烦的办法打败了99%的提交😏
## 3.代码
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode*ptr;
    int len1=0,len2=0;
    ptr=headA;
    while(ptr){
        len1++;
        ptr=ptr->next;
    }
    ptr=headB;
    while(ptr){
        len2++;
        ptr=ptr->next;
    }

    if(len1>len2){
        int i=len1-len2;
        while(i){
            headA=headA->next;
            i--;
        }
    }
    else if(len1<len2){
        int i=len2-len1;
        while(i){
            headB=headB->next;
            i--;
        }
    }

    while(headA!=headB){
        headA=headA->next;
        headB=headB->next;
    }
    return headA;
}
```
