#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int rob(vector<int> &nums) {
    if (nums.size() == 1) {
      return nums[0];
    }

    for (int x = 0; x < nums.size(); x++) {
      if (x != 0 && x != 1) {
        if (x == 2) {
          nums[x] = nums[x] + nums[x - 2];
        } else {
          nums[x] = nums[x] + max(nums[x - 2], nums[x - 3]);
        }
      }
    }

    return max(nums[nums.size() - 1], nums[nums.size() - 2]);
  }
};

int main() {
  vector<int> nums = {3, 11, 4, 100, 114, 2, 3};

  Solution solution;

  cout << solution.rob(nums);

  return 0;
}
