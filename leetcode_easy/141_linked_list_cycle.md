##  Linked List Cycle
##### 2018年2月22日17:01:58
##### 快慢指针
****	
### 题目
>Given a linked list, determine if it has a cycle in it.  
Follow up:
Can you solve it without using extra space?


### 分析
要求我们判断一个链表是否具有循环，比较标准的解法是快慢指针。  
我们知道，如果链表有环的话我们对链表进行遍历不会停止，但是如果我们用两个指针同时遍历并且让它们前进的速度不同，在有环的情况下一定会有相同的一天，如果没有循环的话就会出现NULL，这样就达到了目的。  

自然，我们也可以通过标记链表元素实现查找环的目的，这也是我最开始想到的,但是却没有好的标记方法。  
看到了这样的思路：  
将遍历过的 元素指向头，当我们再次发现头便说明存在环。我认为这个方法比快慢指针更好。
### 代码（仅有快慢指针）
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *fast=head,*slow=head;
    while(fast&&slow&&fast->next){
	//条件的fast->next避免了fast前进时指向空指针
        slow=slow->next;
        fast=fast->next->next;
        if(fast==slow)
            return true;
    }
    return false;
}
```
