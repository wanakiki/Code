## 42. Trapping Rain Water
##### 2018-05-31 23:18:02
##### 第一个困难题（原因：看错了...)
***
## 题目
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![tupian](http://www.leetcode.com/static/images/problemset/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```
## 分析
我的想法是假设有一块木板，从左边压上去，如果能够闭合，下面都有水。对应的，木板的右边所接触的位置就是下一次放木板开始的位置。事实证明，这个方法是错误的...
不过我认为，如果按照这个过程，反过来操作一次，应该就是
## 示例代码
~~错误代码：~~
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int len=height.size(),index=0,h;
        int sum=0; 
        while(index<len-1){
            for(int i=index;i<len;i++){
                if(height[i]>=height[index]){
                     if(i-1>=0 && height[index-1] > height[index] )
                         h=height[i];
                    else
                        h=height[index];//这里 还自作聪明地多加了一步判断之前高度的过程
                    
                        for(int j=index;j<i;j++)
                            sum+=h-height[j];
                    index=i;
                }
            }
            index++;
        }
        return sum;
        
    }
};
```
正确代码：
```cpp
class Solution {
public:
   int trap(vector<int>& height) {
        int len=height.size(),index=0,h;
        int sum=0; 
        //正向遍历
        while(index<len-1){
            for(int i=index+1;i<len;i++){
                if(height[i]>=height[index]){
                	h=height[index];
                    for(int j=index+1;j<i;j++){
                    	sum+=h-height[j];
                    	height[j]=h;
                    }
                    index=i-1;
                    break; 
                } 
            }
            index++;
        }
        //反向遍历
        while(index>0){
        	for(int i=index-1;i>=0;i--){
				if(height[i]>=height[index]){
					h=height[index];
					for(int j=index-1;j>i;j--){
						sum+=h-height[j];
					}
					index=i+1;
					break;
				}
			}
			index--; 
		}
        return sum;
    }
};
```
*** 
##### 2018-6-2-15:55
下面是看了解析之后的做法，用的是类似双指针的做法，左右两边同时操作，更新最大高度，同时不断填满空缺。
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        //int len=height.size();
		int l=0,r=height.size()-1;
		int l_max=0,r_max=0,sum=0;
		while(l<r){
			if(height[l]<height[r]){    //注意比较的对象是当前指向的左右两个值
				height[l]>l_max	? (l_max = height[l]) : (sum+=l_max-height[l]);
				l++;
			}
			else{
				height[r]>r_max ? (r_max = height[r]) : (sum += r_max-height[r]);
				r--;
			}
		}
		return sum; 
    }
};
```
