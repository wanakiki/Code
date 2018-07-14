## 234. Palindrome Linked List
##### 2018年7月14日
##### 回文链表
***
## 题目
Given a singly linked list, determine if it is a palindrome.

Example 1:
```
Input: 1->2
Output: false
```
Example 2:
```
Input: 1->2->2->1
Output: true
```
Follow up:
Could you do it in O(n) time and O(1) space?
## 思路
把链表元素存储到一个vector内，然后两边同时判断并移动。尽管这种做法占用空间较多，但是运行还是比较快的。
## 示例代码
C++：
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
    bool isPalindrome(ListNode* head) {
        if(!head)
            return true;
        vector<int> line;
        while(head){
            line.push_back(head -> val);
            head = head -> next;
        }
        auto l = line.begin(), r = line.end()-1;
        while(l < r){
            if(*l != *r)
                return false;
            l++; r--;            
        }
        return true;
    }
};
```
