## 56. Merge Intervals
##### 2018-03-11
##### 操作数据时记得先排列
****
## 1.题目
>Given a collection of intervals, merge all overlapping intervals.   
给定间隔的集合，合并所有重叠间隔。
>
>For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

## 2.过程
开始认为题目很简单，写好之后果断错误了，有很多情况没有想到。  
#### 📌难点
1. 合并后元素的去除
2. 所给元素并不是排好序的，所以需要考虑类似``[[2,4][0,0]]``的情况。

之前做过去除元素的题目，但是印象不够深刻想不到当时的思路，所以这次的做法是直接将原数组复制一份，标记新数组的索引，对原数组进行遍历。当然，长度为零或一的时候直接返回原数组就可以。

**注意**：由于是复制的数组，所以需要对比的不只是``end``，还有``start``。

看看我最开始的比较做法:
```c
if(res[index].end>=intervals[i].start){
      res[index].end=intervals[i].end;
    }
    else{
      res[index+1]=intervals[i];
      index++;
    }
```
对于``[[2,4][0,0]]``的情况并不好解决，后来换了很多方式，总不能很好的解决....
### ❗直接对原数组排序不就行了嘛


## 3.代码
（qsort排序😏）
```c
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 * };
 */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int compare(const void*a,const void*b){
  struct Interval *c=(struct Interval*)a;
  struct Interval *d=(struct Interval*)b;
  return c->start-d->start;
}
struct Interval* merge(struct Interval* intervals, int intervalsSize, int* returnSize) {
    struct Interval *res;
  int i=0,index=0; //计数，索引
  res=(struct Interval *)malloc(sizeof(struct Interval)*intervalsSize);
  if(intervalsSize==1 || intervalsSize==0){
    *returnSize=intervalsSize;
    res=intervals;
    return res;
  }
    qsort(intervals,intervalsSize,sizeof(intervals[0]),compare);
  res[0]=intervals[0];
  for(i=1;i<intervalsSize;i++){
    if(res[index].end<intervals[i].start){
      res[index+1]=intervals[i];
      index++;
    }
    else{
      if(intervals[i].start<res[index].start){
        res[index].start=intervals[i].start;
      }
      if(intervals[i].end>res[index].end){
        res[index].end=intervals[i].end;
      }
    }
  }
  *returnSize=index+1;
  return  res;
}
```
