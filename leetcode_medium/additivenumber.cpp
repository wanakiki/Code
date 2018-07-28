#include <iostream>
#include <string>
#include <stdlib.h>
#include <assert.h>
using namespace std;
class Solution {
public:
    bool helper(long long num_l1, long long num_l2, string num, int len, int start){
        if(len == start)
            return true;
        for(int l3 = 1; l3 <= len -start; l3++){
            string num3 = num.substr(start, l3);
            if(l3 > 1 && num3[0] == '0')
                break;
            long long num_l3 = atoi(num3.c_str());
            if(num_l1 + num_l2 == num_l3)
                if(helper(num_l2, num_l3, num, len, start+l3))
                    return true; 
        }
        return false;
    }
    bool isAdditiveNumber(string num) {
        int len = num.size();
        //l1、l2为截取的长度
        for (int l1 = 1; l1 < len; l1++){
            string num1 = num.substr(0,l1);
            if(l1 > 1 && num1[0] == '0')
                break;      //长度大于一并且以零开始的数不满足题目要求
            long long num_l1 = atoi(num1.c_str());

            for(int l2 = 1; l2 < len - l1; l2++){
                string num2 = num.substr(l1, l2);   //起始位置应该为l1
                if(l2 > 1 && num2[0] == '0')
                    break;
                long long num_l2 = atoi(num2.c_str());

                if(helper(num_l1, num_l2, num, len, l1 + l2))
                    return true;

            }
        }
        return false;
    }
};

string stringToString(string input) {
    assert(input.length() >= 2);
    string result;
    for (int i = 1; i < input.length() -1; i++) {
        char currentChar = input[i];
        if (input[i] == '\\') {
            char nextChar = input[i+1];
            switch (nextChar) {
                case '\"': result.push_back('\"'); break;
                case '/' : result.push_back('/'); break;
                case '\\': result.push_back('\\'); break;
                case 'b' : result.push_back('\b'); break;
                case 'f' : result.push_back('\f'); break;
                case 'r' : result.push_back('\r'); break;
                case 'n' : result.push_back('\n'); break;
                case 't' : result.push_back('\t'); break;
                default: break;
            }
            i++;
        } else {
          result.push_back(currentChar);
        }
    }
    return result;
}

string boolToString(bool input) {
    return input ? "True" : "False";
}

int main() {
    string line;
    while (getline(cin, line)) {
        string num = stringToString(line);
        
        bool ret = Solution().isAdditiveNumber(num);

        string out = boolToString(ret);
        cout << out << endl;
    }
}