## 47. Permutations II
##### 2018-04-12 22:30:14
##### 回溯
****
## 1.题目
>Given a collection of numbers that might contain duplicates, return all possible unique permutations.   
给定可能包含重复项的数字集合，返回所有可能的唯一排列。

For example,  
[1,1,2] have the following unique permutations:
```
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

## 2.分析
寒假怎么都想不明白的一道题目，让别人指点一下发现也不是很难。  

题目要求把给出数列的所有排列情况都写出来，并且排列可以包括重复元素。 实际上添加重复元素并没有增加多少难度，采用回溯的写法遇到重复直接跳过就可以解决。  从零开始考虑这道题，最难的部分还是回溯的打造，因为每个元素只能用一次，而且必须用到。  

做法：从零开始遍历，将元素添加到用于暂存的temp的尾部，将使用过的元素标记，避免下一层使用，回溯到最后将temp添加到res的尾部。注意每层回溯过后将数据还原。

对于已使用元素的标记，我的做法是先将其 rease 掉，再将缺少元素的num传入下一层，结束之后再使用 insert 把使用的元素还原。  看到的另一种标记方式是另外定义一个数组，如果num中的元素被使用则定义函数对应位置的值发生改变达到标记的作用。比我的做法快一些。
## 3.代码
```cpp
class Solution {
public:
    void change(vector<int> &num,int len,vector<vector<int>> &res,vector<int> &temp){
      if(len==0){
        res.push_back(temp);
        return ;
      }
      for(int i=0;i<len;i++){
        if(i!=0 && num[i]==num[i-1])  continue;   //重复元素的处理
        int temp_num=num[i];
        temp.push_back(num[i]);
        num.erase(num.begin()+i);
        change(num,len-1,res,temp);
        temp.pop_back();
        num.insert(num.begin()+i,temp_num);
      }
    }
    
    vector<vector<int> > permuteUnique(vector<int> &num) {
        sort(num.begin(), num.end());
        vector<vector<int>>res;
        vector<int> temp;
        change(num,num.size(), res,temp);
        return res;
    }    
};
```

另外还有一种交换的方法，实现较乱，描述不出来。
```cpp
class Solution {
public:
    void recursion(vector<int> num, int i, int j, vector<vector<int> > &res) {
        if (i == j-1) {
            res.push_back(num);
            return;
        }
        for (int k = i; k < j; k++) {
            if (i != k && num[i] == num[k]) continue;
            swap(num[i], num[k]);
            recursion(num, i+1, j, res);
        }
    }
    vector<vector<int> > permuteUnique(vector<int> &num) {
        sort(num.begin(), num.end());
        vector<vector<int> >res;
        recursion(num, 0, num.size(), res);
        return res;
    }
};
```

