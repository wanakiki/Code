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

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> ratings = stringToIntegerVector(line);

        int ret = Solution().candy(ratings);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
