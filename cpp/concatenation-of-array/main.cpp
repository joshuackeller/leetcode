#include <iostream>
#include <vector>

//  g++ -std=c++11 main.cpp && ./a.out

using namespace std;

class Solution {
public:
  vector<int> getConcatenation(vector<int> &nums) {
    int size = nums.size();
    for (int x = 0; x < size; x++) {
      nums.push_back(nums[x]);
    }

    return nums;
  }
};

int main() {
  Solution solution;

  vector<int> nums = {1, 3, 2, 1};
  vector<int> results = solution.getConcatenation(nums);
  for (int x = 0; x < results.size(); x++) {
    cout << results[x] << ", ";
  }

  return 0;
}
