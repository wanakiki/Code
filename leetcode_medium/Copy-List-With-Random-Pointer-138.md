## 138. Copy List with Random Pointer
##### 2018-05-06 23:57:13
##### 深拷贝
***
## 题目
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
## 分析
要求是深拷贝，但是每个节点会不确定的指向其他的位置......  自己一开始的想法出现错误，采用map的方法我感觉也不是真正意思上的深复制，不能解决节点出现相同值的情况.....先这样吧
## 题目
```cpp
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {

        RandomListNode *node, *newNode;
        map<int, RandomListNode*> nodesMap;
        for (node = head; node != NULL; node = node->next) {
            newNode = new RandomListNode(node->label);
            nodesMap[node->label] = newNode;
        }
        RandomListNode *newHead = NULL;
        for (node = head; node != NULL; node = node->next) {
            newNode = nodesMap[node->label];
            newHead = newHead ? newHead : newNode;
            newNode->next = node->next ? nodesMap[node->next->label] : NULL;
            newNode->random = node->random ? nodesMap[node->random->label] : NULL;
        }
        return newHead;
        }
};

```
