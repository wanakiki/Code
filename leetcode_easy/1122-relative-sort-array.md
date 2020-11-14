## 1122. 数组的相对排序

2020年11月14日

### 题目

给你两个数组，``arr1`` 和 ``arr2``，       


- ``arr2`` 中的元素各不相同
- ``arr2`` 中的每个元素都出现在 ``arr1`` 中


对 ``arr1`` 中的元素进行排序，使 ``arr1`` 中项的相对顺序和 ``arr2`` 中的相对顺序相同。未在 ``arr2`` 中出现过的元素需要按照升序放在 ``arr1`` 的末尾。



**示例：**

```
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
```



**提示：**


- ``arr1.length, arr2.length <= 1000``
- ``0 <= arr1[i], arr2[i] <= 1000``
- ``arr2`` 中的元素 ``arr2[i]`` 各不相同
- ``arr2`` 中的每个元素 ``arr2[i]`` 都出现在 ``arr1`` 中


### 思路及代码

自定义排序，遍历arr2，用哈希表记录元素出现的位置，便于后续查找，之后自定义函数，对arr1进行排序。

比较难的地方在于如果在函数外定义排序函数的话，哈希表没办法正确传入，看了别人的做法，使用lambda表达式声明匿名函数，实现了该功能。

```cpp

class Solution {
public:
    unordered_map<int, int> myhash;
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        int count = 0;
        
        for(int i = 0; i < arr2.size(); i++){
            if(i == 0){
                myhash[arr2[i]] = count;
            }
            else if(arr2[i] != arr2[i-1]){
                myhash[arr2[i]] = count;
            }
            count++;
        }

        sort(arr1.begin(), arr1.end(), [this](int a, int b){
             int real_a = 0;
        int real_b = 0;

        if(myhash.find(a) != myhash.end()){
            real_a = myhash[a];
        }
        else{
            real_a = 1000 + a;
        }
        if(myhash.find(b) != myhash.end()){
            real_b = myhash[b];
        }
        else{
            real_b = 1000 + b;
        }
        return real_a < real_b;
        });
        return arr1;
    }
};
```