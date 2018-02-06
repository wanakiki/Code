##  Search Insert Position（寻找插入位置）
##### 2018年02月06日21:53:44
##### 恕我直言，这道题炒鸡简单
***
### 题目
>Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.  
You may assume no duplicates in the array.  
给定一个有序数组和目标值，如果找到目标，则返回索引。如果没有，则返回索引，如果按顺序插入的话。 你可能会认为没有重复的数组。  

### 分析
由于数组是有序的，所以从前往后遍历就可以解决问题。当找到大于等于目标值的元素时就返回该位置（因为比目标值小的元素可能有很多），如果找不到就返回数组长度，插在最后面。
起初我的写法是找到大于目标值的元素时返回位置加一，但实际上就应该插入到该位置，解决完这个之后成功提交。

注：我所说的位置指的是从零开始的数组中的元素位置。
### 代码
```c
int searchInsert(int* nums, int numsSize, int target) {
    for(int i=0;i<numsSize;i++){   
                if(nums[i]>=target)
                        return i;	 //  大于等于就可以插入到该位置
        }
        return numsSize;	//循环结束代表全体小于，直接插在最后 
}
```
