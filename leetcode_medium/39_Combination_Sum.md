##  39. Combination Sum
##### 2018-03-07
***
## 1.题目
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.   
The same repeated number may be chosen from C unlimited number of times.  
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

## 2.分析
### 解析
题目要求我们将所给数组元素任意组合，使其加和等于目标数。数组中的元素可以重复使用，同时数组元素全部为正整数。   

看到题目，很容易就想到了递归的解决方案，但是存在一个较难解决的问题：**递归不方便存储已经遍历过的元素**

### 解决问题（已证明错误，但是部分适用）
用
```
sum=sum*10+nums[i]
```
将遍历过的元素加到sum的尾部，当满足最后需要的的时候，
```
while(sum){
	temp=sum%10;
	sum/=10;
}
```
将保存的元素逐个释放.。
因为只有正整数所以可以满足部分情况，但是当元素大于九时，由于是逐位分离，并不能得到正确结果。  

最后想到了用字符串存储，用'.'来分隔每一个元素，用atoi、itoa函数实现转化。（Linux下不能使用itoa，需要用sprintf函数替代）

## 3.代码
因为没有很好的办法，所以仅写了第一种处理方式。实现时出现了部分问题，由于是递归的细节处理，没有单独列出，直接注释。
```c
#include <stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
int count(int x){
    if(x==0)
        return 0;
    int num=0;
    while(x){
        num++;
        x/=10;
    }
    return num;
}
void find(int *candidates,int candidatesSize,int target,int **columnSizes,int *returnSize,int sum,int **res,int start   ){
                int temp=0;
    for(int i=start;i<candidatesSize;i++){

        if(candidates[i]>target||candidates[i]==0)
            continue;   //大于目标进行下一个
        else if(candidates[i]<target){

            temp=candidates[i]+(sum)*10;        //暂存sum并传递给下一次
            find(candidates,candidatesSize,target-candidates[i],columnSizes,returnSize,temp,res,i);
        }
        else if(candidates[i]==target){
            int temp=count(sum);
            columnSizes[0][*returnSize]=temp+1;
            res[*returnSize]=(int *)malloc(sizeof(int)*(temp+1));
                int temp2=sum;
            int tempnum[temp+1];
            for(int i=0;i<temp;i++){
                tempnum[i]=(temp2)%10;
                (temp2)/=10;
            }   //此处直接使用sum会导致后来的情况不能正常输出
            tempnum[temp]=candidates[i];
            memcpy(res[*returnSize],tempnum,sizeof(int)*(temp+1));
            printf("储存的数组：");
            for(int i=0;i<temp+1;i++)
                    printf("%d",res[*returnSize][i]);
            (*returnSize)++；
        }
    }
}
int** combinationSum(int* candidates, int candidatesSize, int target, int** columnSizes, int* returnSize) {
    int ** res;
    res=(int **)malloc(sizeof(int*)*1000);
    printf("res建立完成\n");
    //columnSizes=(int **)malloc(sizeof(int*));
    columnSizes[0]=(int*)malloc(sizeof(int)*100000);
    printf("columnSizes建立完成\n");
    (*returnSize)=0;
    printf("返回大小已经重置\n");
    int sum=0;
    printf("开始递归：\n");
    find(candidates,candidatesSize,target,columnSizes,returnSize,sum,res,0);
    if(*returnSize==0)
        return NULL;
    else
        return res;
}

int main(){
  printf("numsSize target:");
  int numsSize=0,target=0;
  scanf("%d %d",&numsSize,&target);
  int nums[numsSize];
  for(int i=0;i<numsSize;i++)
    scanf("%d",&nums[i] );
  int returnSize=0;
  int ** columnSizes;
  columnSizes=(int**)malloc(sizeof(int*));
  //*columnSizes=(int *)malloc(sizeof(int)*1000);
  printf("进入函数：\n");
  int ** res=combinationSum(nums,numsSize,target,columnSizes,&returnSize);
  printf("size: %d\n",returnSize );
  //printf("%d",columnSizes[0][0]);
 /* for(int i=0;i<returnSize;i++){
          for(int j=0;j<columnSizes[0][i];j++){
                  printf("%d ",res[i][j]);
          }
          printf("\n");
  }*/
  for(int i=0;i<returnSize;i++)
          printf("%d ",columnSizes[0][i]);
}

