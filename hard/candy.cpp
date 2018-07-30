#include<iostream>
#include<string>
#include<vector>
#include <algorithm>
#include<sstream>
using namespace std;
class Solution {
public:
    int candy(vector<int>& ratings) {
        int len = ratings.size();
        vector<int> res(1, len);
        for(int i = 1; i < len; i++){
            if(ratings[i] > ratings[i-1] && res[i] < res[i-1]){
                res[i] = res[i-1] + 1;
            }
        }
        int sum = 0;
        for(int i = 0; i < len; i++){
            sum += res[i];
        }
        return sum;
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}
int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> ratings;
        for(int i =0;i<line.size();i++){
            if(line[i]!=',')
                ratings.push_back(line[i]-'0');
        }
        int ret = Solution().candy(ratings);
        //string out = to_string(ret);
        cout << ret << endl;
    }
    return 0;
}
