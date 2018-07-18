## 26. Remove Duplicates from Sorted Array
##### 2018年02月05日14:52:24
##### 难得的一次成功的题目
***
### 题目
>Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.  
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.  
给定一个有序数组，删除重复内容，使每个元素只出现一次，并返回新的长度。 不要为其他数组分配额外的空间，您必须通过在O（1）额外的内存中就地修改输入数组来实现这一点。

### Example：
```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

```
### 分析
感觉题目的要求比较明确，难点就是在原数组中删除元素。我的做法是从第一个开始，逐个与后面的比较，每一次循环记录重复的个数，将不重复的部分提前，具体实现看代码。
### 代码
```c
int removeDuplicates(int* nums, int numsSize) {
for(int i=0;i<numsSize;i++){
  int index = 0;	//记录多少元素重复
  for(int j=i+1;j<numsSize;j++){
    if(nums[i]==nums[j])
      index++;  //如果重复，index加一继续与后面的比较
    else
      nums[j-index]=nums[j];  //不重复，则将该位前移,因为有index，所以对所有元素适用
  }
  numsSize-=index;	//循环结束之后记得把重复的减掉
}
return numsSize;
}
```
