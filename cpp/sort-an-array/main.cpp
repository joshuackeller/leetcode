#include <iostream>
#include <vector>

using namespace std;

//  g++ -std=c++11 main.cpp && ./a.out

class Solution {
public:
  void mergeArray(vector<int> &nums, int start, int end) {
    if (end - start <= 0) {
      return;
    }

    int middle = ((end - start) / 2) + start;

    mergeArray(nums, start, middle);
    mergeArray(nums, middle + 1, end);

    merge(nums, start, middle, end);
  }

  void merge(vector<int> &nums, int start, int middle, int end) {
    vector<int> nums_a(nums.begin() + start, nums.begin() + middle + 1);
    vector<int> nums_b(nums.begin() + middle + 1, nums.begin() + end + 1);
    int a = 0;
    int b = 0;
    int x = start;

    while (a < nums_a.size() && b < nums_b.size()) {
      if (nums_a[a] < nums_b[b]) {
        nums[x] = nums_a[a];
        a++;
      } else {
        nums[x] = nums_b[b];
        b++;
      }
      x++;
    }

    while (a < nums_a.size()) {
      nums[x] = nums_a[a];
      a++;
      x++;
    }
    while (b < nums_b.size()) {
      nums[x] = nums_b[b];
      b++;
      x++;
    }
  }

  vector<int> sortArray(vector<int> &nums) {
    mergeArray(nums, 0, nums.size() - 1);

    return nums;
  }
};

int main() {

  Solution solution;

  vector<int> nums = {5, 4, 2, 2, 1, 0, 0, 0, 1, 1, 2, 1, 1};
  vector<int> results = solution.sortArray(nums);

  for (int x = 0; x < results.size(); x++) {
    cout << results[x];
  }

  return 0;
}
