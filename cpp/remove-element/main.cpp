#include <iostream>
#include <vector>

using namespace std;

//  g++ -std=c++11 main.cpp && ./a.out

class Solution {
public:
  int removeElement(vector<int> &nums, int val) {
    int count = 0;

    for (int x = 0; x < nums.size(); x++) {
      if (nums[x] != val) {
        nums[count] = nums[x];
        count++;
      }
    }
    return count;
  }
};

int main() {
  Solution solution;

  vector<int> nums = {0, 1, 2, 2, 3, 0, 4, 2};
  int val = 2;
  cout << solution.removeElement(nums, val);

  return 0;
}
