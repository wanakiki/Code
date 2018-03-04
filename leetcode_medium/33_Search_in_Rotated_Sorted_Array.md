## 33. Search in Rotated Sorted Array
##### 2018-03-04
##### 简单搜索
***
## 1. 题目
>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).  
You are given a target value to search. If found in the array return its index, otherwise return -1.  
You may assume no duplicate exists in the array.  
假设按照升序排列的数组在预先未知的某个关键点上旋转。  
（即0 1 2 4 5 6 7可能变成4 5 6 7 0 1 2）。  
你会得到一个目标值来搜索。如果在数组中发现它返回其索引，否则返回-1。  
您可能会认为数组中没有重复。

## 2.分析
首先试了次遍历所有元素，提交显示并没有超时。之后对解法进行优化，因为旋转之前的数组是排列好的，所以在最大值最小值交接的位置进行一次判断可以减少时间。很清晰，直接写代码。
## 3.代码
```c
int search(int *nums,int numsSize,int target)
{
    int index=-1;
    for(int i=0;i<numsSize;i++){
        if(nums[i]==target)
            return i;
	if(i>0){
        if(nums[i]<nums[i-1]){
            if(target>nums[i-1]||target<nums[i])
                return -1;
        }
        else
            if(target>nums[i]&&target<nums[i-1])
                return -1;
	}
    }
    return index;
}
```
## 4.二分搜索法
因为看到解答中有人使用了这种方法自己也不那么了解，所以去搜了下。  
有递归非递归两种实现方式
```c
int binary_search(const int arr[], int start, int end, int khey) {
    int ret = -1;       // 未搜索到数据返回-1下标
    
	int mid;
	while (start <= end) {
		mid = start + (end - start) / 2; //直接平均可能會溢位，所以用此算法
		if (arr[mid] < khey)
			start = mid + 1;
		else if (arr[mid] > khey)
			end = mid - 1;
		else {            // 最後檢測相等是因為多數搜尋狀況不是大於要不就小於
			ret = mid;  
            break;
        }
	}
	
	return ret;     // 单一出口
}


//递归
int binary_search(const int arr[], int start, int end, int khey) {
	if (start > end)
		return -1;

	int mid = start + (end - start) / 2;    //直接平均可能會溢位，所以用此算法
	if (arr[mid] > khey)
		return binary_search(arr, start, mid - 1, khey);
	else if (arr[mid] < khey)
		return binary_search(arr, mid + 1, end, khey);
	else
	    return mid;        //最後檢測相等是因為多數搜尋狀況不是大於要不就小於
}
```
[维基链接](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2%E7%AE%97%E6%B3%95)
