#include <chrono>
#include <iostream>
#include <queue>
#include <vector>

//  g++ -std=c++11 main.cpp && ./a.out

using namespace std;

class Solution {
public:
  // #1 - Heap
  int findKthLargest(vector<int> &nums, int k) {
    priority_queue<int> heap(nums.begin(), nums.end());

    for (int x = 0; x < k - 1; x++) {
      heap.pop();
    }

    return heap.top();
  }
};

int main() {
  Solution solution;

  vector<int> nums = {6, 2, 4, 1, 3};
  int k = 2;

  auto start = chrono::high_resolution_clock::now();
  cout << solution.findKthLargest(nums, k) << "\n";
  auto end = chrono::high_resolution_clock::now();

  chrono::duration<double> duration = end - start;

  cout << "Finished in " << duration.count() << " seconds \n";

  return 0;
}
