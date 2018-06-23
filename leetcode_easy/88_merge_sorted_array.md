## Merge Sorted Array
##### 2018年2月11日17:04:25
##### 由于疏忽检查了一个小时....
***
### 题目
>Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
给定两个排序整数数组nums1和nums2，将nums2合并为nums1作为一个排序数组。 注意：您可能会认为nums1有足够的空间（大小大于或等于m + n）来保存nums2中的其他元素。 在nums1和nums2中初始化的元素的数量分别是m和n。

### 分析
题目要求合并两个有序数组，题目告诉我们可以直接在sums1里面合并，但是我们也可以新建数组。  
为了简便，我采取的前者，并且从大数到小数的顺序判断。但是因为求简单，直接用了m、n，但是循环结束的条件写成了m、n大于0，找了很长时间才发现......  
题目很简单，贴下代码
### 代码
```c
//我的比较丑的代码
void merge(int* nums1, int m, int* nums2, int n) {
 int i=m+n-1;
        while(i>=0){
                if(n<1)
                        break;
                else if(m<1){
                        nums1[i]=nums2[n-1];
                        n--;
                }
                else {if(nums1[m-1]<nums2[n-1]){
                        nums1[i]=nums2[n-1];
                        n--;
                }
                else{
                        nums1[i]=nums1[m-1];
                        m--;
                }
                }
                i--;
        }

}

//别人的代码
 int k;
  for( k=m+n-1;k>=0;k--)
    {
        if ((nums1[m-1]>nums2[n-1]&&m>0)||n<=0)
        {
            nums1[n+m-1]=nums1[m-1];
            m--;
        }
        else
        {
             nums1[n+m-1]=nums2[n-1];
             n--;
        }
        
    }
```
