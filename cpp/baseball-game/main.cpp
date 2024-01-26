#include <iostream>
#include <numeric>
#include <vector>

//  g++ -std=c++11 main.cpp && ./a.out

using namespace std;

class Solution {
public:
  int calPoints(vector<string> &operations) {
    vector<int> scores;
    for (int x = 0; x < operations.size(); x++) {
      if (operations[x] == "+") {
        scores.push_back(scores[scores.size() - 1] + scores[scores.size() - 2]);
      } else if (operations[x] == "D") {
        scores.push_back(2 * scores[scores.size() - 1]);
      } else if (operations[x] == "C") {
        scores.pop_back();
      } else {
        scores.push_back(stoi(operations[x]));
      }
    }
    return accumulate(scores.begin(), scores.end(), 0);
  }
};

int main() {
  Solution solution;

  vector<string> operations = {"5", "4", "C", "D", "+"};
  cout << solution.calPoints(operations);

  return 0;
}
