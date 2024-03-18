#include <iostream>
#include <queue>
#include <vector>

//  g++ -std=c++11 main.cpp && ./a.out

using namespace std;

class Solution {
public:
  int lastStoneWeight(vector<int> &stones) {
    priority_queue<int> heap(stones.begin(), stones.end());

    while (!heap.empty()) {
      int y = heap.top();
      heap.pop();

      if (!heap.empty()) {
        int x = heap.top();
        heap.pop();

        if (x < y) {
          heap.push(y - x);
        }
      } else {
        return y;
      }
    }

    return 0;
  }
};

int main() {
  Solution solution;

  vector<int> stones = {7, 6, 7, 6, 9};
  cout << solution.lastStoneWeight(stones);
}
