## Merge Two Sorted ListsMerge Two Sorted Lists
##### 2018年02月04日16:44:05
##### 简单的题目需要更好的想法
*****
### 题目
>Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.  
  合并两个已排序的链接列表并将其作为新列表返回。新列表应通过将前两个列表的节点拼接在一起来完成。

### example
```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

### 分析
题目很简单，根据传入的链表进行判断，用一个``while``循环就就解决了问题。提交一次之后排除了两个空链表的情况，AC。 

提交之后感觉代码非常臃肿，  
在讨论区发现了更酷的递归实现方式，取个人感觉思路清晰的， 留下来参考：  
C
```c
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if (l1 == NULL) return l2;
    if (l2 == NULL) return l1;
    if (l1->val <= l2->val) {
        l1->next = mergeTwoLists(l1->next, l2);
        return l1;
    } else {
        l2->next = mergeTwoLists(l1, l2->next);
        return l2;
    }
}
```
**感觉递归实现的代码都炒鸡强！**

Python3(2018年8月5日)：

```py
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        merged = ListNode(-1)
        copy = merged
        while l1 and l2:
            if l1.val <= l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        while l1:
            merged.next = l1
            l1 = l1.next
            merged = merged.next
        while l2:
            merged.next = l2
            l2 = l2.next
            merged = merged.next
        return copy.next
```

最快的

```py
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None):
            return l2
        if(l2 == None):
            return l1
        mList = ListNode(None)
        mListWalker = mList
        while(l1 and l2):
            if(l1.val < l2.val):
                mListWalker.next = l1
                l1 = l1.next
            else:
                mListWalker.next = l2
                l2 = l2.next
            mListWalker = mListWalker.next
        if(l1):
            mListWalker.next = l1
        if(l2):
            mListWalker.next = l2
        return mList.next    
```

递归写法🎈

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        if (l1.val <= l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```