#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int uniquePaths(int m, int n) {
    int row = m;
    int col = n;
    vector<vector<int>> grid(m, vector<int>(n, 1));

    for (int r = 1; r < row; r++) {
      for (int c = 1; c < col; c++) {
        grid[r][c] = grid[r - 1][c] + grid[r][c - 1];
      }
    }

    return grid[row - 1][col - 1];
  }
};

int main() {

  Solution solution;

  cout << solution.uniquePaths(3, 2);

  return 0;
}
