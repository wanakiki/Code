## 167. Two Sum II - Input array is sorted
##### 2018-04-02 20:37:52
##### vector
***
## 1.题目
>Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
>
>The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
>
>You may assume that each input would have exactly one solution and you may not use the same element twice.
>
>Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2   
>给定已按升序排序的整数数组，找到两个数字，使它们合计为特定的目标数字。函数twoSum应该返回这两个数字的索引，以便它们合计到目标，其中index1必须小于index2。  请注意，您返回的答案（index1和index2）不是从零开始的。每个输入都只有一个解决方案，并且不可以使用相同的元素两次。  输入：数字= {2,7,11,15}，目标= 9输出：索引1 = 1，索引2 = 2

## 2.分析
四月份，开始强迫自己用C++。这是转投到C++的第一题，题目很简单，了解了一下vector的用法，采用两头凑的方式遍历一次得到结果。  
要注意，本题一定会存在满足题意的数。
## 3.代码
```c
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left=0,right=numbers.size()-1;
        while(left<right){
            if(numbers[left]+numbers[right]==target){
                vector<int> res{left+1,right+1};
                return res;
            }
            else{
                if(numbers[left]+numbers[right]<target)
                    left++;
                else
                    right--;
        }
        }
    }
};
```
