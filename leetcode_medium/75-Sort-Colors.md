## 75.Sort Colors
##### 2018-03-17
***
## 1.题目
> Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
>
>Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.   
>
>给定一个数组，其中n个对象颜色为红色、白色或蓝色，对它们进行排序，使颜色相同的对象相邻，颜色按红色、白色和蓝色的顺序排列。 在这里，我们将使用整数0、1和2分别表示红色、白色和蓝色。     
>Note:
You are not suppose to use the library's sort function for this problem. 

## 2.分析
本质还是排序，有很多种实现方法。  
可能是因为熟悉了qsort函数，看了这个题目之后直接写起来了（🙃哈哈哈哈没看到不让用）  
```c
int compare(void *a,void *b){
    return *(int *)a-*(int*)b;
}
void sortColors(int* nums, int numsSize) {
    qsort(nums,numsSize,sizeof(int),compare);
}
```
一种简便的做法是设计变量遍历数组统计颜色的个数，然后再按照个数赋值。
```c
void sortColors(int* nums, int numsSize) {
    //int* numsPos = nums;
    int count0 = 0;
    int count1 = 0;
    int count2 = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) count0++;
        if (nums[i] == 1) count1++;
        if (nums[i] == 2) count2++;
    }
    for (int j = 1; j <= count0; j++) {
        *nums = 0;
        nums++;
    }
    for (int m = 1; m <= count1; m++) {
        *nums = 1;
        nums++;
    }
    for (int n = 1; n <= count2; n++) {
        *nums = 2;
        nums++;
    }
}
```
一种交换的方法是设置左右两个变量用来标记最右边的0和最左边的1，遍历数组，同时调整两个变量的值，当遍历到最左边的1的时候停止。  
```c
void sortColors(int* a, int n) {
    int left = 0;
    int right  = n-1;
    int i=0;
    
    while(i <= right && left <= right ){
        if(a[i] == 0){
            swap(&a[i],&a[left]);
            i++;
            left++;
        }
        else if(a[i] == 2){
            swap(&a[i],&a[right]);
            right--;
        }
        else{
            i++;
        }
    }
}
```
