#include <iostream>

//  g++ -std=c++11 main.cpp && ./a.out

using namespace std;

class Solution {
public:
  int fib(int n) {
    int first = 0;
    int second = 1;

    if (n == 0) {
      return 0;
    } else if (n == 1) {
      return 1;
    } else {
      for (int x = 2; x <= n; x++) {
        int previous_second = second;
        second = first + second;
        first = previous_second;
      }
      return second;
    }
  }
};

int main() {
  Solution solution;

  cout << solution.fib(5);

  return 0;
}
