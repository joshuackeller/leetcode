#include <chrono>
#include <iostream>
#include <vector>

//  g++ -std=c++11 main.cpp && ./a.out

using namespace std;

class Solution {
public:
  int search(vector<int> &nums, int target) {
    int left = 0;
    int right = nums.size() - 1;

    // Not necessary but makes it faster for larger cases
    if (nums[left] > target || nums[right] < target) {
      return -1;
    }

    while (left <= right) {
      int middle = (left + right) / 2;

      // Not necessary but makes it faster for larger cases
      if (nums[left] == target) {
        return left;
      }
      if (nums[right] == target) {
        return right;
      }

      if (nums[middle] < target) {
        left = middle + 1;
      } else if (nums[middle] > target) {
        right = middle - 1;
      } else {
        return middle;
      }
    }

    return -1;
  }
};

int main() {
  Solution solution;

  vector<int> nums = {-5, -4, -3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int target = 11;

  cout << solution.search(nums, target) << "\n";

  return 0;
}
