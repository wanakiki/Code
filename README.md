# Code
learn to learn

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
