## 86. Partition List
##### 2018-04-04 23:33:06
***
## 1.题目
>Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
>
>You should preserve the original relative order of the nodes in each of the two partitions.
>
>For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
>
>给定一个链表和一个值x，对它进行分割，使得所有小于x的节点都在节点大于或等于x之前。  
>应该保留两个分区中每个分区中节点的原始相对顺序。

## 2.分析
我的做法是找到第一个大于等于x的节点，记录之前的节点l，然后再创建一个指针r从下一个节点开始遍历，当发现小于x的节点则插入到l之后，将l后移一位，连接丢失节点的部分继续遍历。  
对于头部的处理，开始设置的指针指向节点的下一个节点赋值为head，这样可以有效避免。在后期插入的时候如果l->next是head，则对head赋新值。  
最后返回head。
## 3.代码
```c
struct ListNode* partition(struct ListNode* head, int x) {
        if(!head)   return head;
        struct ListNode *l,*r;
        l=(struct ListNode *)malloc(sizeof(struct ListNode));
        r=(struct ListNode*)malloc(sizeof(struct ListNode));
        int flag=0;
        l->next=head;
        r=NULL;
        while(l->next){
            if(l->next->val>=x){
                //return head;
                r=l->next;
                flag=1;
                break;
            }
            l=l->next;
        }
        while(r && r->next && flag){
            if(r->next->val < x){
                struct ListNode *temp=r->next->next;
                r->next->next=l->next;
                if(l->next==head){
                    head=r->next;
                }
                l->next=r->next;
                l=l->next;
                r->next=temp;
                continue;
            }
            r=r->next;
        }
        return head;
  }
  ```
