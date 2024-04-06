#include <chrono>
#include <iostream>
#include <unordered_map>

using namespace std;
using namespace std::chrono;

// SOLUTION #3: Bottom Up / True Dynamic Programming
class Solution {
private:
public:
  int climbStairs(int n) {
    int twoBack = 0;
    int oneBack = 1;
    int total = 0;

    for (int x = 0; x < n; x++) {
      total = oneBack + twoBack;
      twoBack = oneBack;
      oneBack = total;
    }

    return total;
  }
};

int main() {
  Solution solution;

  auto start = high_resolution_clock::now();

  int result = solution.climbStairs(5);

  cout << "result: " << result << endl;

  auto duration =
      duration_cast<milliseconds>(high_resolution_clock::now() - start);

  cout << duration.count() << " milliseconds" << endl;

  return 0;
}

// SOLUTION #2: Top Down Dynamic Programming
// class Solution {
// private:
//   unordered_map<int, int> cache;
//
// public:
//   int climbStairs(int n) {
//     if (cache.find(n) != cache.end()) {
//       return cache[n];
//     }
//
//     int count = 1;
//
//     for (int x = 2; x <= n; x++) {
//       int num = n - x;
//       cache[num] = climbStairs(num);
//       count += cache[num];
//     }
//
//     return count;
//   }
// };

// SOLUTION #1: Heaping pile of garbage
// class Solution {
// private:
//   unordered_map<int, int> cache;
//
// public:
//   int climbStairs(int n) {
//     int count = 0;
//     unordered_map<int, int> cache;
//     return solve(n, count);
//   }
//
//   int solve(int n, int &count) {
//     count++;
//
//     if (n <= 1) {
//       return count;
//     }
//
//     if (cache.find(n) != cache.end()) {
//       return cache[n];
//     }
//
//     for (int x = 2; x <= n; x++) {
//       int remaining = n - x;
//       int remainingSum = climbStairs(remaining);
//       count += remainingSum;
//       cache[remaining] = remainingSum;
//     }
//     return count;
//   }
// };
// 1 + 1 + 1 + 1 + 1
// 2 + 1 + 1 + 1
// 2 + 2 + 1
// 1 + 2 + 1 + 1
// 1 + 2 + 2
// 1 + 1 + 2 + 1
// 1 + 1 + 1 + 2

// 1 + 1 + 1 + 1 + 1
// 2 + 1 + 1 + 1
//// 2 + 2 + 1
//// 2 + 1 + 2
// 1 + 2 + 1 + 1
//// 1 + 2 + 2
// 1 + 1 + 2 + 1
// 1 + 1 + 1 + 2
