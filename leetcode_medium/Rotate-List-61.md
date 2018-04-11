## 61. Rotate List
##### 2018-04-11 23:21:42
***
## 1.题目
>Given a list, rotate the list to the right by k places, where k is non-negative.  
给定一个列表，将列表向右旋转k个地方，其中k是非负数。

Example:
```
Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
```
## 2.分析
英语不大好，看完题目没明白什么意思，看了解决方案才知道。  
我的理解是，将给出的链表连成环，像抽奖罗盘那样指着固定的位置，然后向右旋转k，选到的就是新的头。   

看了别人的代码，注定还要反工一次，不过自己没考虑到 k%len 防止转好几圈的情况，还有这种题目用于控制循环的数字一定要搞明白。
## 3.代码
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
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head) return head;
        ListNode *res,*tmp;
        res=tmp=head;
        int len=1;
        while(tmp->next){
            len++;
            tmp=tmp->next;
        }
        tmp->next=head;
        if(k %=len){
            for(int i=0;i<len-k;i++)
                tmp=tmp->next;
        }
        res=tmp->next;
        tmp->next=NULL;
        return res;
    }
};
```
