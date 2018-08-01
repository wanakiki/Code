## Add Two Numbers
##### 2018年01月31日22:39:01
##### 侧重点：链表的建立
****
### 题目
>You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```
### 分析
题目相对简单,但是结构体掌握不熟练于是折回去看[结构体的相关知识](http://blog.csdn.net/u010784887/article/details/78072295)  
由于这篇文章讲的是c++中的操作，又发现了一系列问题(未取证):
- 定义结构体时在不用``typeof``的情况下，C语言需要一直使用``struct ``,而C++可以直接使用结构体名继续定义变量。
- ``new``、``delate``是C++中的关键字，涵盖了``malloc``、``free``（linux中需要使用头文件``<stdlib.h>``)的功能。
- Leetcode中的结构体的``head->val``是有值的！！！（由于博客的建立方法为空出头，提交时出现不少麻烦）
### 解题方法（已证明错误）
 **暴力**：直接写出将结构体还原为整数以及整数转化为结构体的函数（结构体的输入本来就需要函数），用这两个函数直接得到答案。

BUT  
**我是旺旺没有想到，这个题目的结构体的长度居然超过了``long long``......**

所以，老实逐位相加是最好的办法......（但是还没写）

### 贴下代码，创建链表（空头）的部分还是正确的
```c
#include<stdio.h>
#include<stdlib.h>
struct ListNode{
	int val;
	struct ListNode *next;
};

//链表创建函数
struct ListNode * create(int x){
	struct ListNode *head,*ptr,*newNode;
	head=(struct ListNode *)malloc(sizeof(struct ListNode));
	head->next = NULL;
	if(x==0){
		newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
		newNode->val = 0;
		newNode->next = NULL;
		head->next =newNode;
		return head;
	}
	ptr = head;
	for (int i=0;x>0;i++){
		int temp=x%10;
		x/=10;
		newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
		newNode->val = temp;
		newNode->next = NULL;
		ptr->next = newNode;
		ptr = ptr -> next;
	}
	return head;
}

//链表输出函数
void display(struct ListNode *head){
	struct ListNode *ptr;
	ptr = head->next;
	while(ptr!=NULL){
		printf("%d", ptr->val);
		ptr = ptr->next;
	}
}

//还原函数
int restore(struct ListNode *head){
	struct ListNode *ptr;
	int temp=0,i=1;
	ptr=head ->next;
	while(ptr!=NULL){
			temp+=i*ptr->val;
			i*=10;
		ptr=ptr->next;
	}
	return temp;
}
struct ListNode * addTwoNumbers(struct ListNode *l1,struct ListNode *l2){
	int temp=restore(l1)+restore(l2);
	struct ListNode *head;
	head=create(temp);
	return head;
}

int main()
{
	struct ListNode *head1,*head2,*head3;
	int a=0,b=0;
	scanf("%d %d",&a,&b);
	//直接输入整数，传递给创建函数
	head1=create(a);
	head2=create(b);
	head3=addTwoNumbers(head1,head2);
	display(head3);
}
```

## Add Two Numbers后续
##### 2018年02月01日22:22:25
****
经过之前的分析，由于整数是逆向存储的，所以从两个链表的第一个节点开始逐个相加并保存在新建的链表里面就能解决问题。 

但是需要注意：**读取到的两个整数相加是可以大于9的**。所以还要考虑大于九如何存储。  

解决方法很简单：取模保存在该位，将十位数带到下一个循环。并且这样写每个循环需要存储的数的最大值为 9+9+1=19，不会出现其他情况。  

因为有了明确的想法，讲道理一切都应该顺顺利利地进行下去，但是出现了一个很严重的问题，导致桌面卡死两次.......  

### 致命的错误
由于个人偷懒，产生了直接用一个函数完成节点数据的读取与自动指向下一个节点的想法。但由于传入的指针不会被修改，导致函数无法完成该任务。（说的可能不太清楚，具体看代码↓↓↓）
```c
int read(struct ListNode *head){	//幻想中的read函数
  int num=0;
  if(head==NULL)
    return 0;
  else{
    num= head->val;
    head=head->next;	//此处操作并不会导致原来的head发生改变！！！
    return num;
  }
}
//while(l1!=NULL || l2!=NULL || temp!=0)
//这是创建链表循环的判断条件，temp为上一个节点十位的值
//这个循环因为read函数的错误，一直读取到相同的值
//因而持续不断的添加链表的节点，不会终止
```
找到问题，对其进行了纠正（强制关机了两次.......)
### 正确的代码
```c
struct ListNode * addTwoNumbers(struct ListNode *l1,struct ListNode *l2){
  int temp=0,flag=0;
  struct ListNode *head,*ptr,*newNode;
  head=(struct ListNode *)malloc(sizeof(struct ListNode));
  head->next=NULL;
  ptr=head;
  while(l1!=NULL || l2!=NULL || temp!=0){
    if(l1!=NULL){
            temp+= l1->val;
            l1= l1->next;
    }
    if(l2!=NULL){
            temp+= l2->val;
            l2= l2->next;
    }
    int temp2=temp%10;
    temp/=10;
    if(flag==0){
      ptr->val = temp2;
      flag=1;
      continue;
    }
    newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
                newNode->val = temp2;
                newNode->next = NULL;
                ptr->next = newNode;
                ptr = ptr -> next;
  }
  return head;
}
```
感觉值得一提的是在这个函数里面temp的循环利用

Python(2018年8月1日):

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        temp = result
        carry = 0
        while (l1 != None or l2 != None or carry !=0):
            sum = 0
            if l1 != None:
                sum+=l1.val
                l1 = l1.next

            if l2 != None:
                sum+=l2.val
                l2 = l2.next

            if carry != 0:
                sum+=carry

            temp.next = ListNode(sum % 10)
            temp = temp.next
            carry = sum // 10

        return result.next  
```

反序存放真的很容易处理🤔
